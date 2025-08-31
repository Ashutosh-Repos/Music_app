#!/bin/bash

# Install dependencies
pip3 install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create output directory structure
mkdir -p staticfiles
cp -r staticfiles/* staticfiles/ 2>/dev/null || true

echo "Build completed successfully!"
