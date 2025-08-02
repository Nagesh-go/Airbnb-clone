from rest_framework import serializers
from .models import Property, PropertyImage, Review, Booking
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image', 'caption', 'is_primary']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['user']


class PropertySerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    images = PropertyImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.ReadOnlyField()
    review_count = serializers.ReadOnlyField()
    primary_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'address', 'city', 'state', 'country', 'zip_code',
            'property_type', 'room_type', 'price_per_night', 'max_guests', 'bedrooms', 'bathrooms',
            'amenities', 'latitude', 'longitude', 'host', 'is_available', 'is_featured',
            'created_at', 'updated_at', 'images', 'reviews', 'average_rating', 'review_count',
            'primary_image'
        ]
        read_only_fields = ['host', 'created_at', 'updated_at']
    
    def get_primary_image(self, obj):
        primary_image = obj.images.filter(is_primary=True).first()
        if primary_image:
            return PropertyImageSerializer(primary_image).data
        # Return first image if no primary image is set
        first_image = obj.images.first()
        if first_image:
            return PropertyImageSerializer(first_image).data
        return None


class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'title', 'description', 'address', 'city', 'state', 'country', 'zip_code',
            'property_type', 'room_type', 'price_per_night', 'max_guests', 'bedrooms', 'bathrooms',
            'amenities', 'latitude', 'longitude', 'is_available', 'is_featured'
        ]
    
    def create(self, validated_data):
        validated_data['host'] = self.context['request'].user
        return super().create(validated_data)


class BookingSerializer(serializers.ModelSerializer):
    property = PropertySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    property_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'id', 'property', 'property_id', 'user', 'check_in_date', 'check_out_date',
            'guests', 'total_price', 'status', 'special_requests', 'created_at', 'duration'
        ]
        read_only_fields = ['user', 'total_price', 'status', 'created_at', 'duration']
    
    def create(self, validated_data):
        property_id = validated_data.pop('property_id')
        try:
            property_obj = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            raise serializers.ValidationError("Property not found")
        
        validated_data['property'] = property_obj
        validated_data['user'] = self.context['request'].user
        
        # Calculate total price
        duration = (validated_data['check_out_date'] - validated_data['check_in_date']).days
        validated_data['total_price'] = property_obj.price_per_night * duration
        
        return super().create(validated_data)
    
    def validate(self, data):
        # Check if check_out_date is after check_in_date
        if data['check_out_date'] <= data['check_in_date']:
            raise serializers.ValidationError("Check-out date must be after check-in date")
        
        # Check if property is available for the selected dates
        property_id = data.get('property_id')
        if property_id:
            try:
                property_obj = Property.objects.get(id=property_id)
                conflicting_bookings = Booking.objects.filter(
                    property=property_obj,
                    status__in=['pending', 'confirmed'],
                    check_in_date__lt=data['check_out_date'],
                    check_out_date__gt=data['check_in_date']
                )
                if conflicting_bookings.exists():
                    raise serializers.ValidationError("Property is not available for the selected dates")
            except Property.DoesNotExist:
                raise serializers.ValidationError("Property not found")
        
        return data 