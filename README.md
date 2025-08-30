# Django Music Player

A Django-based music player application with user authentication, playlists, favorites, and social login features.

## Features

- User authentication with email/password and Google OAuth
- Music player with playlist management
- Favorites and recent songs tracking
- Support for Hindi and English songs
- Responsive design

## Local Development

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`

## Deployment on Vercel

### Prerequisites

- Git repository with your code
- Vercel account

### Steps

1. **Push your code to Git repository** (GitHub, GitLab, etc.)

2. **Connect to Vercel Dashboard**:

   - Go to [vercel.com](https://vercel.com)
   - Sign in and click "New Project"
   - Import your Git repository

3. **Configure Environment Variables** in Vercel Dashboard:

   - Go to your project settings
   - Navigate to "Environment Variables"
   - Add the following variables:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=False
     DATABASE_URL=postgresql://username:password@host:port/database
     ```

4. **Database Setup**:

   - Vercel will automatically provide a PostgreSQL database
   - The `DATABASE_URL` will be automatically set by Vercel

5. **Deploy**:
   - Vercel will automatically detect it's a Django project
   - The deployment will use the `vercel.json` configuration
   - Static files will be collected automatically

### Important Notes

- **Media Files**: For production, you should use cloud storage (AWS S3, Cloudinary, etc.) for media files instead of local storage
- **Static Files**: Static files are served by WhiteNoise middleware
- **Database**: Uses PostgreSQL on Vercel, SQLite locally
- **Environment Variables**: Make sure to set all required environment variables in Vercel dashboard

### Troubleshooting

- If you encounter issues with static files, check that `STATIC_ROOT` is properly configured
- For database issues, ensure `DATABASE_URL` is correctly set
- Check Vercel deployment logs for any Python/Django errors

## Project Structure

```
MusicPlayer/
├── authentication/     # User authentication app
├── musicapp/          # Main music player app
├── musicplayer/       # Django project settings
├── static/           # Static files (CSS, JS, images)
├── media/            # User uploaded media files
├── templates/        # HTML templates
├── requirements.txt  # Python dependencies
├── vercel.json      # Vercel deployment configuration
└── build_files.sh   # Build script for Vercel
```
