#!/bin/bash
# Production deployment script for TueLinh Real Estate

echo "🚀 DEPLOYING TUELINH REAL ESTATE TO PRODUCTION..."
echo "================================================="

# Set production environment
export DJANGO_SETTINGS_MODULE="tuelinh_real_estate.settings"
export DEBUG=False

# Install dependencies
echo "📦 Installing production dependencies..."
pip install -r requirements.txt --no-dev

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Run database migrations
echo "🗄️  Running database migrations..."
python manage.py migrate --noinput

# Create cache table (if using database cache)
echo "💾 Creating cache tables..."
python manage.py createcachetable || true

# Compress static files
echo "🗜️  Compressing static files..."
python manage.py compress --force || true

# Check deployment
echo "🔍 Running deployment checks..."
python manage.py check --deploy

gunicorn tuelinh_real_estate.wsgi:application

echo ""
echo "✅ DEPLOYMENT COMPLETED!"
echo "================================================="
echo ""
echo "🚀 To start the production server:"
echo "   gunicorn tuelinh_real_estate.wsgi:application --bind 0.0.0.0:8000"
echo ""
echo "🔧 Or with more workers:"
echo "   gunicorn tuelinh_real_estate.wsgi:application --bind 0.0.0.0:8000 --workers 3"
