# 🎵 Django Music Player - Vercel Ready

A fully functional Django music streaming application configured for Vercel deployment.

## 🚀 Quick Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/MusicPlayer)

## ✨ Features

- 🎧 **Music Streaming**: Play songs with a beautiful interface
- 👤 **User Authentication**: Sign up, sign in, and Google OAuth
- 📝 **Playlist Management**: Create and manage your playlists
- ❤️ **Favorites**: Save your favorite songs
- 🔍 **Search & Filter**: Find songs by name, artist, or language
- 📱 **Responsive Design**: Works on desktop and mobile
- 🎨 **Modern UI**: Bootstrap 4 with custom styling

## 🛠️ Tech Stack

- **Backend**: Django 3.2
- **Database**: SQLite (no external DB required)
- **Frontend**: Bootstrap 4, HTML5, CSS3, JavaScript
- **Authentication**: Django AllAuth
- **Static Files**: WhiteNoise
- **Deployment**: Vercel

## 📁 Project Structure

```
MusicPlayer/
├── musicplayer/          # Django project settings
├── musicapp/            # Main music app
├── authentication/      # User authentication
├── api/                # API endpoints
├── static/             # Static files (CSS, JS, images)
├── media/              # Media files (songs, album art)
├── templates/          # HTML templates
├── vercel.json         # Vercel configuration
├── requirements.txt    # Python dependencies
└── runtime.txt         # Python version
```

## 🎯 Key Features

### Music Player

- Stream music directly in the browser
- Playlist creation and management
- Favorite songs system
- Recent songs tracking
- Search and filter functionality

### User Management

- User registration and login
- Google OAuth integration
- User-specific playlists and favorites
- Profile management

### Content Management

- Admin panel for song management
- Upload and manage music files
- Album art and metadata
- Language categorization (Hindi/English)

## 🔧 Configuration

The application is pre-configured for Vercel deployment:

- **vercel.json**: Vercel deployment configuration
- **settings_prod.py**: Production Django settings
- **requirements.txt**: All necessary Python packages
- **runtime.txt**: Python 3.9 specification

## 📦 Included Content

The application comes with:

- 30+ sample songs (Hindi and English)
- Album artwork for all songs
- Pre-configured database with sample data
- Complete user interface

## 🌐 Deployment

1. **Fork/Clone** this repository
2. **Connect** to Vercel
3. **Deploy** - Vercel will automatically detect Django configuration
4. **Access** your music player at the provided URL

## 🎵 Sample Songs Included

### Hindi Songs

- Baarish - Half Girlfriend
- Gulaabo - Mirzya
- Soch Na Sake - Airlift
- And many more...

### English Songs

- Attention - Charlie Puth
- Girls Like You - Maroon 5
- Let Me Love You - DJ Snake
- And many more...

## 🔐 Admin Access

After deployment:

1. Visit `/admin/` on your deployed site
2. Use the default admin credentials or create a new superuser
3. Manage songs, users, and content

## 📱 Mobile Friendly

The application is fully responsive and works great on:

- Desktop computers
- Tablets
- Mobile phones

## 🎨 Customization

Easily customize:

- Colors and styling in `static/musicapp/css/musicplayer.css`
- Templates in `templates/musicapp/`
- Add new features in `musicapp/views.py`

## 📄 License

MIT License - feel free to use and modify!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Ready to deploy your own music player? Click the "Deploy with Vercel" button above!** 🚀
