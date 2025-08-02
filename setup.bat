@echo off
echo 🚀 Setting up Airbnb Clone Full Stack Application
echo ==================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed. Please install Node.js 16+ first.
    pause
    exit /b 1
)

echo ✅ Prerequisites check passed!

REM Backend Setup
echo.
echo 🔧 Setting up Django Backend...
echo ================================

cd backend

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing Python dependencies...
pip install -r requirements.txt

REM Run migrations
echo 🗄️ Running database migrations...
python manage.py makemigrations
python manage.py migrate

REM Create superuser
echo.
echo 👤 Create a superuser account (optional):
echo You can skip this by pressing Ctrl+C
python manage.py createsuperuser

REM Populate sample data
echo.
echo 📊 Populating database with sample data...
python manage.py populate_sample_data

echo.
echo ✅ Backend setup complete!
echo 🌐 Django server will run on http://localhost:8000

REM Frontend Setup
echo.
echo 🎨 Setting up React Frontend...
echo ================================

cd ..\frontend

REM Install dependencies
echo 📥 Installing Node.js dependencies...
npm install

echo.
echo ✅ Frontend setup complete!
echo 🌐 React app will run on http://localhost:3000

REM Instructions
echo.
echo 🎉 Setup Complete!
echo ==================
echo.
echo To start the application:
echo.
echo 1. Start the Django backend:
echo    cd backend
echo    venv\Scripts\activate
echo    python manage.py runserver
echo.
echo 2. In a new terminal, start the React frontend:
echo    cd frontend
echo    npm start
echo.
echo 3. Open your browser and visit:
echo    Frontend: http://localhost:3000
echo    Backend API: http://localhost:8000
echo    Django Admin: http://localhost:8000/admin
echo.
echo Happy coding! 🚀
pause 