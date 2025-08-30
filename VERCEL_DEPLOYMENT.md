# Vercel Deployment Guide for Django Music Player

This guide will help you deploy your Django Music Player application to Vercel using the dashboard (no CLI required).

## Prerequisites

1. **Git Repository**: Your code should be in a Git repository (GitHub, GitLab, Bitbucket)
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
3. **Database**: You'll need a PostgreSQL database (Vercel provides one automatically)

## Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure your repository contains all the necessary files:

- `requirements.txt` (updated with production dependencies)
- `vercel.json` (Vercel configuration)
- `build_files.sh` (build script)
- All Django project files

### 2. Connect to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your Git repository
4. Vercel will automatically detect it's a Python/Django project

### 3. Configure Environment Variables

In your Vercel project dashboard:

1. Go to **Settings** → **Environment Variables**
2. Add the following variables:

```
SECRET_KEY=your-very-secure-secret-key-here
DEBUG=False
```

**Important**: Generate a new secret key for production:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 4. Database Configuration

Vercel will automatically:

- Provide a PostgreSQL database
- Set the `DATABASE_URL` environment variable
- Handle database connections

### 5. Deploy

1. Click **Deploy** in the Vercel dashboard
2. Vercel will:
   - Install dependencies from `requirements.txt`
   - Run the build script (`build_files.sh`)
   - Collect static files
   - Run database migrations
   - Deploy your application

### 6. Post-Deployment Setup

After successful deployment:

1. **Create Superuser** (if needed):

   - Go to your deployed URL + `/admin/`
   - Create a superuser account

2. **Add Music Files**:
   - Since Vercel is serverless, you can't upload files directly
   - Consider using cloud storage (AWS S3, Cloudinary) for media files
   - Or pre-populate your database with music data

## Important Notes

### Media Files Limitation

**Current Issue**: Your app stores music files locally in the `media/` folder, but Vercel's serverless environment doesn't support persistent file storage.

**Solutions**:

1. **Use Cloud Storage** (Recommended):

   - AWS S3
   - Cloudinary
   - Google Cloud Storage
   - Update your Django models to use cloud storage

2. **Pre-populate Database**:
   - Add music files to your database before deployment
   - Use external URLs for music files

### Static Files

Static files are handled by WhiteNoise middleware and will be served correctly.

### Database

- Uses PostgreSQL on Vercel
- Automatically managed by Vercel
- No additional setup required

## Troubleshooting

### Common Issues

1. **Build Failures**:

   - Check Vercel build logs
   - Ensure all dependencies are in `requirements.txt`
   - Verify Python version compatibility

2. **Static Files Not Loading**:

   - Check that `STATIC_ROOT` is properly configured
   - Ensure WhiteNoise middleware is added

3. **Database Errors**:

   - Verify `DATABASE_URL` is set correctly
   - Check that migrations are running

4. **Media Files Not Working**:
   - This is expected - implement cloud storage solution
   - Or use external URLs for music files

### Debugging

1. **Check Logs**: Go to your Vercel dashboard → Functions → View Function Logs
2. **Environment Variables**: Verify all required variables are set
3. **Build Output**: Check the build output for any errors

## Next Steps

1. **Implement Cloud Storage**: For production, implement AWS S3 or similar for media files
2. **Add Custom Domain**: Configure a custom domain in Vercel settings
3. **Set up Monitoring**: Add error tracking and monitoring
4. **Optimize Performance**: Consider CDN for static files

## Support

If you encounter issues:

1. Check Vercel documentation: [vercel.com/docs](https://vercel.com/docs)
2. Review Django deployment checklist: [docs.djangoproject.com/en/stable/howto/deployment/checklist/](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
3. Check Vercel community forums
