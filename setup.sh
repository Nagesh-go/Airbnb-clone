#!/bin/bash

echo " Setting up Airbnb Clone Full Stack Application"
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo " Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo " Node.js is not installed. Please install Node.js 16+ first."
    exit 1
fi

echo " Prerequisites check passed!"

# Backend Setup
echo ""
echo " Setting up Django Backend..."
echo "================================"

cd backend

# Create virtual environment
echo " Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo " Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo " Installing Python dependencies..."
pip install -r requirements.txt

# Run migrations
echo " Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo ""
echo " Create a superuser account (optional):"
echo "You can skip this by pressing Ctrl+C"
python manage.py createsuperuser

# Populate sample data
echo ""
echo " Populating database with sample data..."
python manage.py populate_sample_data

echo ""
echo " Backend setup complete!"
echo " Django server will run on http://localhost:8000"

# Frontend Setup
echo ""
echo " Setting up React Frontend..."
echo "================================"

cd ../frontend

# Install dependencies
echo " Installing Node.js dependencies..."
npm install

echo ""
echo " Frontend setup complete!"
echo " React app will run on http://localhost:3000"

# Instructions
echo ""
echo " Setup Complete!"
echo "=================="
echo ""
echo "To start the application:"
echo ""
echo "1. Start the Django backend:"
echo "   cd backend"
echo "   source venv/bin/activate  # On Windows: venv\\Scripts\\activate"
echo "   python manage.py runserver"
echo ""
echo "2. In a new terminal, start the React frontend:"
echo "   cd frontend"
echo "   npm start"
echo ""
echo "3. Open your browser and visit:"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:8000"
echo "   Django Admin: http://localhost:8000/admin"
echo ""
echo "Happy coding! 🚀" 