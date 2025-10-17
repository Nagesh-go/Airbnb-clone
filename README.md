<<<<<<< HEAD
# Airbnb Clone - Full Stack Application

A full-stack Airbnb clone built with Django backend and React frontend.

## 🚀 Features

### Backend (Django)
- **RESTful API** with Django REST Framework
- **User Authentication** with token-based auth
- **Property Management** - CRUD operations for properties
- **Booking System** - Make and manage reservations
- **Review System** - Rate and review properties
- **Advanced Search & Filtering** - Multiple filter options
- **Image Management** - Handle property images
- **Admin Interface** - Django admin for data management
- **SQLite Database** (easily configurable for PostgreSQL)

### Frontend (React)
- **Modern UI** with responsive design
- **User Authentication** - Login, register, logout
- **Property Listings** - Browse and search properties
- **Property Details** - View detailed property information
- **Booking System** - Make reservations
- **User Profile** - Manage account and bookings
- **Search & Filters** - Advanced search functionality

## 🛠️ Tech Stack

### Backend
- **Django 4.2.7** - Web framework
- **Django REST Framework** - API framework
- **SQLite** - Database (production-ready for PostgreSQL)
- **Django CORS Headers** - Handle cross-origin requests
- **Pillow** - Image processing
- **Django Filter** - Advanced filtering

### Frontend
- **React 19.1.1** - UI library
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **CSS3** - Styling

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Airbnb-clone
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Populate with sample data (optional)
python manage.py populate_sample_data

# Run development server
python manage.py runserver
```

The Django backend will be available at `http://localhost:8000/`

### 3. Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The React frontend will be available at `http://localhost:3000/`

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/users/register/` | User registration |
| POST | `/api/users/login/` | User login |
| POST | `/api/users/logout/` | User logout |
| GET | `/api/users/profile/` | Get user profile |
| PUT | `/api/users/profile/` | Update user profile |
| PUT | `/api/users/change-password/` | Change password |

### Property Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/properties/` | List all properties |
| POST | `/api/properties/` | Create new property |
| GET | `/api/properties/{id}/` | Get property details |
| PUT | `/api/properties/{id}/` | Update property |
| DELETE | `/api/properties/{id}/` | Delete property |
| GET | `/api/properties/featured/` | Get featured properties |
| GET | `/api/properties/search/?q=query` | Search properties |

### Booking Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/bookings/` | List user's bookings |
| POST | `/api/bookings/` | Create new booking |
| GET | `/api/bookings/{id}/` | Get booking details |
| PUT | `/api/bookings/{id}/` | Update booking |
| DELETE | `/api/bookings/{id}/` | Cancel booking |

## 🔍 Search & Filtering

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

## 🗄️ Database Models

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

## 🎨 Frontend Components

### Pages
- **Home** - Landing page with featured properties
- **Search Results** - Filtered property listings
- **Property Detail** - Detailed property view with booking
- **Profile** - User profile and bookings management

### Components
- **Header** - Navigation and search
- **PropertyCard** - Property listing card
- **Auth Forms** - Login and registration forms

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### CORS Settings

The backend is configured to allow requests from `http://localhost:3000` for development.

## 📱 Sample Data

The project includes a management command to populate the database with sample data:

```bash
python manage.py populate_sample_data
```

This creates:
- 4 sample users
- 5 sample properties with different types
- Sample reviews and bookings

## 🚀 Deployment

### Backend Deployment

1. Set `DEBUG = False` in settings.py
2. Use a production database (PostgreSQL recommended)
3. Configure static file serving
4. Set up environment variables
5. Use a production WSGI server (Gunicorn)

### Frontend Deployment

1. Build the production version: `npm run build`
2. Serve the build folder with a web server
3. Configure API base URL for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is for educational purposes.

## 🆘 Troubleshooting

Common issues:
- Check console for error messages
- Verify all dependencies are installed
- Ensure both servers are running
- Check API endpoints are accessible

## 🎯 Key Features

This project demonstrates:

- **Full-stack development** with Django and React
- **RESTful API design** and implementation
- **User authentication** and authorization
- **Database modeling** and relationships
- **Search and filtering** functionality
- **File upload** and image handling
- **State management** in React
- **Responsive design** principles
- **API integration** between frontend and backend

A comprehensive full-stack project demonstrating modern web development practices. 
=======
# Airbnb-clone
>>>>>>> f3dd4ee259cf955b7b8b866dca2946bbec02fe7a
