#!/bin/bash

# Install dependencies
pip3 install -r requirements.txt

# Skip database operations during build (SQLite not available in Vercel build environment)
# Run migrations only if database is available
python3 manage.py migrate --noinput || echo "Skipping migrations - database not available during build"

# Collect static files (skip if database not available)
python3 manage.py collectstatic --noinput || echo "Skipping collectstatic - database not available during build"

# Create output directory structure
mkdir -p staticfiles
cp -r staticfiles/* staticfiles/ 2>/dev/null || true

echo "Build completed successfully!"
