# Django Music Player - Vercel Deployment Guide

## Overview

This Django music player application is configured for deployment on Vercel without using external databases.

## Features

- User authentication (signup/signin)
- Google OAuth integration
- Music streaming and playback
- Playlist management
- Favorites system
- Recent songs tracking
- Search and filter functionality

## Deployment Steps

### 1. Prerequisites

- Vercel account
- Git repository with the project
- Python 3.9

### 2. Project Structure

```
MusicPlayer/
├── musicplayer/          # Django project settings
├── musicapp/            # Main music app
├── authentication/      # User authentication
├── api/                # API endpoints
├── static/             # Static files
├── media/              # Media files (songs, images)
├── templates/          # HTML templates
├── vercel.json         # Vercel configuration
├── requirements.txt    # Python dependencies
└── runtime.txt         # Python version
```

### 3. Configuration Files

#### vercel.json

- Configures Python build
- Routes static and media files
- Sets production environment

#### settings_prod.py

- Production Django settings
- WhiteNoise for static files
- SQLite database (no external DB required)

### 4. Deployment Process

1. **Push to Git Repository**

   ```bash
   git add .
   git commit -m "Configure for Vercel deployment"
   git push origin main
   ```

2. **Deploy on Vercel**

   - Go to [vercel.com](https://vercel.com)
   - Import your Git repository
   - Vercel will automatically detect Django configuration
   - Deploy

3. **Environment Variables** (if needed)
   - Add any environment variables in Vercel dashboard
   - Default configuration uses SQLite database

### 5. Post-Deployment

1. **Create Superuser** (if needed)

   - Access Django admin at `/admin/`
   - Create admin user for content management

2. **Upload Media Files**
   - Media files are included in the repository
   - Songs and images are stored in `/media/` directory

### 6. Features Available

- **Home Page**: Featured songs, recent plays
- **All Songs**: Complete music library with search/filter
- **User Authentication**: Sign up, sign in, Google OAuth
- **Playlists**: Create and manage playlists
- **Favorites**: Save favorite songs
- **Recent**: Track recently played songs
- **Language Filter**: Hindi and English songs

### 7. Technical Details

- **Database**: SQLite (included in deployment)
- **Static Files**: Served via WhiteNoise
- **Media Files**: Served via Django
- **Authentication**: Django AllAuth with Google OAuth
- **Frontend**: Bootstrap 4 with custom CSS

### 8. Troubleshooting

- Check Vercel build logs for any errors
- Ensure all dependencies are in requirements.txt
- Verify static files are collected properly
- Check database migrations are applied

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## License

MIT License - see LICENSE file for details.
