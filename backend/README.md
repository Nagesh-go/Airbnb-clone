# Airbnb Clone - Django Backend

A Django REST API backend for an Airbnb clone application.

## Features

- **Property Management**: Create, read, update, and delete properties
- **User Authentication**: Registration, login, logout, and profile management
- **Booking System**: Make and manage property bookings
- **Review System**: Rate and review properties
- **Search & Filtering**: Advanced search with multiple filters
- **Image Management**: Handle property images
- **Admin Interface**: Django admin for easy data management

## Tech Stack

- **Django 4.2.7**: Web framework
- **Django REST Framework**: API framework
- **SQLite**: Database (can be easily changed to PostgreSQL)
- **Django CORS Headers**: Handle cross-origin requests
- **Pillow**: Image processing

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## API Endpoints

### Authentication
- `POST /api/users/register/` - User registration
- `POST /api/users/login/` - User login
- `POST /api/users/logout/` - User logout
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/` - Update user profile
- `PUT /api/users/change-password/` - Change password

### Properties
- `GET /api/properties/` - List all properties
- `POST /api/properties/` - Create new property
- `GET /api/properties/{id}/` - Get property details
- `PUT /api/properties/{id}/` - Update property
- `DELETE /api/properties/{id}/` - Delete property
- `GET /api/properties/featured/` - Get featured properties
- `GET /api/properties/search/?q=query` - Search properties

### Bookings
- `GET /api/bookings/` - List user's bookings
- `POST /api/bookings/` - Create new booking
- `GET /api/bookings/{id}/` - Get booking details
- `PUT /api/bookings/{id}/` - Update booking
- `DELETE /api/bookings/{id}/` - Cancel booking

### Reviews
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create new review
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review

## Filtering and Search

### Property Filters
- `?property_type=apartment` - Filter by property type
- `?room_type=entire` - Filter by room type
- `?city=New York` - Filter by city
- `?min_price=100&max_price=500` - Filter by price range
- `?guests=4` - Filter by number of guests
- `?amenities=WiFi&amenities=Kitchen` - Filter by amenities
- `?check_in=2024-01-01&check_out=2024-01-05` - Filter by availability

### Search
- `?search=beach` - Search in title, description, and location
- `?ordering=price_per_night` - Sort by price
- `?ordering=-created_at` - Sort by newest first

## Database Models

### Property
- Basic info: title, description, address
- Location: city, state, country, coordinates
- Details: type, room type, price, capacity
- Features: amenities, availability status

### Booking
- Dates: check-in, check-out
- Details: guests, total price, status
- Relationships: property, user

### Review
- Rating: 1-5 stars
- Comment: text review
- Relationships: property, user

### User
- Standard Django User model
- Extended with profile functionality

## Admin Interface

Access the Django admin at `http://localhost:8000/admin/` to:
- Manage properties, bookings, and reviews
- View user data
- Monitor system activity

## Sample Data

You can create sample data using Django management commands or through the admin interface.

## Environment Variables

Create a `.env` file in the backend directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## Production Deployment

For production:
1. Change `DEBUG = False` in settings.py
2. Use a production database (PostgreSQL recommended)
3. Set up proper CORS settings
4. Configure static file serving
5. Use environment variables for sensitive data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is for educational purposes. 