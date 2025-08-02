from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Avg
from .models import Property, PropertyImage, Review, Booking
from .serializers import (
    PropertySerializer, PropertyCreateSerializer, PropertyImageSerializer,
    ReviewSerializer, BookingSerializer
)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['property_type', 'room_type', 'city', 'state', 'country', 'is_available', 'is_featured']
    search_fields = ['title', 'description', 'address', 'city', 'state', 'country']
    ordering_fields = ['price_per_night', 'created_at', 'average_rating']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return PropertyCreateSerializer
        return PropertySerializer
    
    def get_queryset(self):
        queryset = Property.objects.all()
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price_per_night__gte=min_price)
        if max_price:
            queryset = queryset.filter(price_per_night__lte=max_price)
        
        # Filter by number of guests
        guests = self.request.query_params.get('guests')
        if guests:
            queryset = queryset.filter(max_guests__gte=guests)
        
        # Filter by amenities
        amenities = self.request.query_params.getlist('amenities')
        if amenities:
            for amenity in amenities:
                queryset = queryset.filter(amenities__contains=[amenity])
        
        # Filter by date availability
        check_in = self.request.query_params.get('check_in')
        check_out = self.request.query_params.get('check_out')
        if check_in and check_out:
            conflicting_bookings = Booking.objects.filter(
                status__in=['pending', 'confirmed'],
                check_in_date__lt=check_out,
                check_out_date__gt=check_in
            ).values_list('property_id', flat=True)
            queryset = queryset.exclude(id__in=conflicting_bookings)
        
        return queryset
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_review(self, request, pk=None):
        property_obj = self.get_object()
        serializer = ReviewSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(property=property_obj, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def book(self, request, pk=None):
        property_obj = self.get_object()
        serializer = BookingSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(property=property_obj, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_properties = Property.objects.filter(is_featured=True, is_available=True)
        serializer = self.get_serializer(featured_properties, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({'error': 'Search query is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        properties = Property.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(city__icontains=query) |
            Q(state__icontains=query) |
            Q(country__icontains=query)
        ).filter(is_available=True)
        
        serializer = self.get_serializer(properties, many=True)
        return Response(serializer.data)


class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 