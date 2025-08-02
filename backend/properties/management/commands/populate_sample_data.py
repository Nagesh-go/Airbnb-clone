from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from properties.models import Property, PropertyImage, Review, Booking
from decimal import Decimal
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the database with sample data for the Airbnb clone'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create sample users
        users = self.create_sample_users()
        
        # Create sample properties
        properties = self.create_sample_properties(users)
        
        # Create sample reviews
        self.create_sample_reviews(properties, users)
        
        # Create sample bookings
        self.create_sample_bookings(properties, users)
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )

    def create_sample_users(self):
        users = []
        
        # Create a few sample users
        sample_users_data = [
            {
                'username': 'john_doe',
                'email': 'john@example.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'password': 'password123'
            },
            {
                'username': 'jane_smith',
                'email': 'jane@example.com',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'password': 'password123'
            },
            {
                'username': 'mike_wilson',
                'email': 'mike@example.com',
                'first_name': 'Mike',
                'last_name': 'Wilson',
                'password': 'password123'
            },
            {
                'username': 'sarah_jones',
                'email': 'sarah@example.com',
                'first_name': 'Sarah',
                'last_name': 'Jones',
                'password': 'password123'
            }
        ]
        
        for user_data in sample_users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults=user_data
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
            users.append(user)
            self.stdout.write(f'Created user: {user.username}')
        
        return users

    def create_sample_properties(self, users):
        properties = []
        
        sample_properties_data = [
            {
                'title': 'Cozy Beachfront Apartment',
                'description': 'Beautiful apartment with stunning ocean views. Perfect for a relaxing beach vacation.',
                'address': '123 Beach Road',
                'city': 'Miami',
                'state': 'Florida',
                'country': 'USA',
                'zip_code': '33139',
                'property_type': 'apartment',
                'room_type': 'entire',
                'price_per_night': Decimal('150.00'),
                'max_guests': 4,
                'bedrooms': 2,
                'bathrooms': 1,
                'amenities': ['WiFi', 'Kitchen', 'Pool', 'Beach Access', 'Air Conditioning'],
                'latitude': Decimal('25.7617'),
                'longitude': Decimal('-80.1918'),
                'is_featured': True
            },
            {
                'title': 'Luxury Mountain Cabin',
                'description': 'Rustic yet luxurious cabin in the mountains. Perfect for nature lovers and adventure seekers.',
                'address': '456 Mountain Trail',
                'city': 'Aspen',
                'state': 'Colorado',
                'country': 'USA',
                'zip_code': '81611',
                'property_type': 'cabin',
                'room_type': 'entire',
                'price_per_night': Decimal('250.00'),
                'max_guests': 6,
                'bedrooms': 3,
                'bathrooms': 2,
                'amenities': ['WiFi', 'Kitchen', 'Fireplace', 'Hot Tub', 'Mountain View'],
                'latitude': Decimal('39.1911'),
                'longitude': Decimal('-106.8175'),
                'is_featured': True
            },
            {
                'title': 'Modern Downtown Loft',
                'description': 'Stylish loft in the heart of downtown. Walking distance to restaurants, shops, and attractions.',
                'address': '789 Urban Street',
                'city': 'New York',
                'state': 'New York',
                'country': 'USA',
                'zip_code': '10001',
                'property_type': 'apartment',
                'room_type': 'entire',
                'price_per_night': Decimal('200.00'),
                'max_guests': 2,
                'bedrooms': 1,
                'bathrooms': 1,
                'amenities': ['WiFi', 'Kitchen', 'Gym', 'Doorman', 'City View'],
                'latitude': Decimal('40.7505'),
                'longitude': Decimal('-73.9934'),
                'is_featured': False
            },
            {
                'title': 'Charming Country House',
                'description': 'Beautiful country house with large garden. Perfect for families and peaceful retreats.',
                'address': '321 Country Lane',
                'city': 'Napa',
                'state': 'California',
                'country': 'USA',
                'zip_code': '94558',
                'property_type': 'house',
                'room_type': 'entire',
                'price_per_night': Decimal('180.00'),
                'max_guests': 8,
                'bedrooms': 4,
                'bathrooms': 3,
                'amenities': ['WiFi', 'Kitchen', 'Garden', 'BBQ', 'Wine Cellar'],
                'latitude': Decimal('38.2975'),
                'longitude': Decimal('-122.2869'),
                'is_featured': True
            },
            {
                'title': 'Elegant City Villa',
                'description': 'Luxurious villa with modern amenities and beautiful architecture.',
                'address': '654 Luxury Avenue',
                'city': 'Los Angeles',
                'state': 'California',
                'country': 'USA',
                'zip_code': '90210',
                'property_type': 'villa',
                'room_type': 'entire',
                'price_per_night': Decimal('350.00'),
                'max_guests': 10,
                'bedrooms': 5,
                'bathrooms': 4,
                'amenities': ['WiFi', 'Kitchen', 'Pool', 'Gym', 'Spa', 'Butler Service'],
                'latitude': Decimal('34.0736'),
                'longitude': Decimal('-118.4004'),
                'is_featured': True
            }
        ]
        
        for i, property_data in enumerate(sample_properties_data):
            property_obj = Property.objects.create(
                host=users[i % len(users)],
                **property_data
            )
            properties.append(property_obj)
            self.stdout.write(f'Created property: {property_obj.title}')
        
        return properties

    def create_sample_reviews(self, properties, users):
        sample_reviews = [
            {'rating': 5, 'comment': 'Amazing place! Highly recommended.'},
            {'rating': 4, 'comment': 'Great location and clean property.'},
            {'rating': 5, 'comment': 'Perfect for our family vacation.'},
            {'rating': 4, 'comment': 'Beautiful views and comfortable stay.'},
            {'rating': 5, 'comment': 'Exceeded our expectations!'},
        ]
        
        for property_obj in properties:
            # Create 2-4 reviews per property
            num_reviews = random.randint(2, 4)
            for i in range(num_reviews):
                review_data = random.choice(sample_reviews)
                user = random.choice(users)
                
                # Make sure user hasn't already reviewed this property
                if not Review.objects.filter(property=property_obj, user=user).exists():
                    Review.objects.create(
                        property=property_obj,
                        user=user,
                        rating=review_data['rating'],
                        comment=review_data['comment']
                    )
        
        self.stdout.write('Created sample reviews')

    def create_sample_bookings(self, properties, users):
        # Create some past and future bookings
        for property_obj in properties:
            # Past booking
            past_check_in = date.today() - timedelta(days=30)
            past_check_out = past_check_in + timedelta(days=3)
            
            Booking.objects.create(
                property=property_obj,
                user=random.choice(users),
                check_in_date=past_check_in,
                check_out_date=past_check_out,
                guests=random.randint(1, property_obj.max_guests),
                total_price=property_obj.price_per_night * 3,
                status='completed'
            )
            
            # Future booking
            future_check_in = date.today() + timedelta(days=15)
            future_check_out = future_check_in + timedelta(days=5)
            
            Booking.objects.create(
                property=property_obj,
                user=random.choice(users),
                check_in_date=future_check_in,
                check_out_date=future_check_out,
                guests=random.randint(1, property_obj.max_guests),
                total_price=property_obj.price_per_night * 5,
                status='confirmed'
            )
        
        self.stdout.write('Created sample bookings') 