from django.contrib import admin
from .models import Property, PropertyImage, Review, Booking


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'host', 'city', 'property_type', 'price_per_night', 'is_available', 'is_featured']
    list_filter = ['property_type', 'room_type', 'is_available', 'is_featured', 'city', 'state', 'country']
    search_fields = ['title', 'description', 'address', 'city', 'host__username']
    list_editable = ['is_available', 'is_featured']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'host')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'country', 'zip_code', 'latitude', 'longitude')
        }),
        ('Property Details', {
            'fields': ('property_type', 'room_type', 'price_per_night', 'max_guests', 'bedrooms', 'bathrooms')
        }),
        ('Features', {
            'fields': ('amenities', 'is_available', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ['property', 'caption', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    search_fields = ['property__title', 'caption']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['property', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['property__title', 'user__username', 'comment']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['property', 'user', 'check_in_date', 'check_out_date', 'guests', 'total_price', 'status']
    list_filter = ['status', 'check_in_date', 'check_out_date']
    search_fields = ['property__title', 'user__username']
    readonly_fields = ['created_at', 'updated_at', 'duration']
    
    fieldsets = (
        ('Booking Information', {
            'fields': ('property', 'user', 'check_in_date', 'check_out_date', 'guests')
        }),
        ('Financial', {
            'fields': ('total_price', 'status')
        }),
        ('Additional', {
            'fields': ('special_requests',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'duration'),
            'classes': ('collapse',)
        }),
    ) 