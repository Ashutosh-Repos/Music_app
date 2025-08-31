#!/bin/bash

echo "🎵 Django Music Player - Vercel Deployment Script"
echo "=================================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please initialize git first:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    echo "   git remote add origin <your-repo-url>"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please create it first:"
    echo "   python3 -m venv venv"
    echo "   source venv/bin/activate"
    echo "   pip install -r requirements.txt"
    exit 1
fi

echo "✅ Checking project configuration..."

# Activate virtual environment
source venv/bin/activate

# Run Django checks
echo "🔍 Running Django deployment checks..."
python manage.py check --deploy

# Collect static files with production settings
echo "📦 Collecting static files..."
DJANGO_SETTINGS_MODULE=musicplayer.settings_prod python manage.py collectstatic --noinput

# Test production settings
echo "🧪 Testing production settings..."
DJANGO_SETTINGS_MODULE=musicplayer.settings_prod python manage.py check --deploy

echo ""
echo "✅ Project is ready for deployment!"
echo ""
echo "🚀 Next steps:"
echo "1. Push to Git repository:"
echo "   git add ."
echo "   git commit -m 'Configure for Vercel deployment'"
echo "   git push origin main"
echo ""
echo "2. Deploy on Vercel:"
echo "   - Go to https://vercel.com"
echo "   - Import your Git repository"
echo "   - Vercel will auto-detect Django configuration"
echo "   - Deploy automatically"
echo ""
echo "3. Access your music player at the provided URL"
echo ""
echo "📚 For detailed instructions, see DEPLOYMENT_GUIDE.md"
echo ""
echo "�� Happy listening!"
