# Vercel Deployment Guide for Django Music Player

This guide will help you deploy your Django Music Player application to Vercel using the dashboard (no CLI required).

## Prerequisites

1. **Git Repository**: Your code should be in a Git repository (GitHub, GitLab, Bitbucket)
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
3. **Database**: You'll need a PostgreSQL database (Vercel provides one automatically, or you can use external)

## Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure your repository contains all the necessary files:

- `requirements.txt` (updated with production dependencies)
- `vercel.json` (Vercel configuration)
- `build_files.sh` (build script)
- All Django project files

### 2. Database Setup (Choose One Option)

#### Option A: Use Vercel's Built-in PostgreSQL (Recommended for beginners)
- Vercel will automatically provide a PostgreSQL database
- No additional setup required
- The `DATABASE_URL` will be automatically set by Vercel

#### Option B: Use External PostgreSQL Database
Run the setup script to configure an external database:

```bash
python3 setup_external_db.py
```

**Popular Free PostgreSQL Providers:**
- **Supabase**: https://supabase.com (Free tier: 500MB)
- **Railway**: https://railway.app (Free tier: $5 credit)
- **Neon**: https://neon.tech (Free tier: 3GB)
- **PlanetScale**: https://planetscale.com (Free tier: 1GB, but uses MySQL)

### 3. Connect to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your Git repository
4. Vercel will automatically detect it's a Python/Django project

### 4. Configure Environment Variables

In your Vercel project dashboard:

1. Go to **Settings** → **Environment Variables**
2. Add the following variables:

**For Vercel's built-in PostgreSQL:**
```
SECRET_KEY=s02tj6=n59q10!yqr4@c=l9s6s&o@0g(lxxdf1osbv1%h_b5rc
DEBUG=False
```

**For External PostgreSQL:**
```
SECRET_KEY=s02tj6=n59q10!yqr4@c=l9s6s&o@0g(lxxdf1osbv1%h_b5rc
DEBUG=False
DATABASE_URL=postgresql://username:password@host:port/database
```

**Optional: For Cloud Storage (AWS S3):**
```
USE_S3=True
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
AWS_S3_REGION_NAME=us-east-1
```

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

2. **Migrate Data** (if using external database):
   ```bash
   # Set your DATABASE_URL environment variable
   export DATABASE_URL="your-postgresql-url"
   
   # Run the migration script
   python3 migrate_data.py
   ```

3. **Add Music Files**:
   - Since Vercel is serverless, you can't upload files directly
   - Consider using cloud storage (AWS S3, Cloudinary) for media files
   - Or pre-populate your database with music data

## External Database Setup Guide

### Supabase Setup
1. Go to [supabase.com](https://supabase.com)
2. Create a new project
3. Go to Settings → Database
4. Copy the connection string
5. Replace `[password]` with your database password

### Railway Setup
1. Go to [railway.app](https://railway.app)
2. Create a new project
3. Add PostgreSQL service
4. Go to Variables → Connect → PostgreSQL
5. Copy the DATABASE_URL

### Neon Setup
1. Go to [neon.tech](https://neon.tech)
2. Create a new project
3. Go to Connection Details
4. Copy the connection string

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

- Uses PostgreSQL on Vercel or external PostgreSQL
- Automatically managed by Vercel (if using built-in)
- Connection pooling and health checks configured

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
   - Test database connection locally

4. **Media Files Not Working**:
   - This is expected - implement cloud storage solution
   - Or use external URLs for music files

### Debugging

1. **Check Logs**: Go to your Vercel dashboard → Functions → View Function Logs
2. **Environment Variables**: Verify all required variables are set
3. **Build Output**: Check the build output for any errors
4. **Database Connection**: Test your database URL locally

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
