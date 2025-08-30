#!/usr/bin/env python3
"""
Script to help set up external PostgreSQL database for Django Music Player
"""

import os
import sys
import dj_database_url
from urllib.parse import urlparse

def test_database_connection(database_url):
    """Test if the database connection works"""
    try:
        import psycopg2
        from psycopg2 import sql
        
        # Parse the database URL
        parsed = urlparse(database_url)
        
        # Connect to the database
        conn = psycopg2.connect(
            host=parsed.hostname,
            port=parsed.port or 5432,
            database=parsed.path[1:],  # Remove leading slash
            user=parsed.username,
            password=parsed.password
        )
        
        # Test the connection
        cur = conn.cursor()
        cur.execute('SELECT version();')
        version = cur.fetchone()
        
        print(f"✅ Database connection successful!")
        print(f"   PostgreSQL version: {version[0]}")
        
        cur.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def setup_database():
    """Interactive setup for external database"""
    print("🔧 External PostgreSQL Database Setup")
    print("=" * 50)
    
    print("\nChoose your database provider:")
    print("1. Supabase (Free tier available)")
    print("2. Railway (Free tier available)")
    print("3. Neon (Free tier available)")
    print("4. PlanetScale (Free tier available)")
    print("5. Custom PostgreSQL URL")
    print("6. Use Vercel's built-in PostgreSQL")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    if choice == "1":
        print("\n📋 Supabase Setup:")
        print("1. Go to https://supabase.com")
        print("2. Create a new project")
        print("3. Go to Settings → Database")
        print("4. Copy the connection string")
        print("5. Replace [password] with your database password")
        
        url = input("\nEnter your Supabase connection string: ").strip()
        
    elif choice == "2":
        print("\n📋 Railway Setup:")
        print("1. Go to https://railway.app")
        print("2. Create a new project")
        print("3. Add PostgreSQL service")
        print("4. Go to Variables → Connect → PostgreSQL")
        print("5. Copy the DATABASE_URL")
        
        url = input("\nEnter your Railway DATABASE_URL: ").strip()
        
    elif choice == "3":
        print("\n📋 Neon Setup:")
        print("1. Go to https://neon.tech")
        print("2. Create a new project")
        print("3. Go to Connection Details")
        print("4. Copy the connection string")
        
        url = input("\nEnter your Neon connection string: ").strip()
        
    elif choice == "4":
        print("\n📋 PlanetScale Setup:")
        print("1. Go to https://planetscale.com")
        print("2. Create a new database")
        print("3. Go to Connect → Connect with Prisma")
        print("4. Copy the connection string")
        print("Note: PlanetScale uses MySQL, not PostgreSQL")
        
        url = input("\nEnter your PlanetScale connection string: ").strip()
        
    elif choice == "5":
        url = input("\nEnter your custom PostgreSQL URL: ").strip()
        
    elif choice == "6":
        print("\n✅ Using Vercel's built-in PostgreSQL")
        print("Vercel will automatically provide the DATABASE_URL")
        return "vercel"
        
    else:
        print("❌ Invalid choice")
        return None
    
    # Test the connection
    if url and url != "vercel":
        print(f"\n🔍 Testing database connection...")
        if test_database_connection(url):
            print(f"\n✅ Database URL is valid!")
            print(f"URL: {url}")
            return url
        else:
            print(f"\n❌ Please check your database URL and try again")
            return None
    
    return url

def main():
    """Main function"""
    print("🎵 Django Music Player - External Database Setup")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Please run this script from your Django project root directory")
        sys.exit(1)
    
    # Setup database
    database_url = setup_database()
    
    if database_url and database_url != "vercel":
        print(f"\n📝 Environment Variables to set in Vercel:")
        print(f"DATABASE_URL={database_url}")
        print(f"SECRET_KEY=s02tj6=n59q10!yqr4@c=l9s6s&o@0g(lxxdf1osbv1%h_b5rc")
        print(f"DEBUG=False")
        
        # Save to file
        with open('database_url.txt', 'w') as f:
            f.write(f"DATABASE_URL={database_url}\n")
        
        print(f"\n💾 Database URL saved to 'database_url.txt'")
        
    elif database_url == "vercel":
        print(f"\n📝 Environment Variables to set in Vercel:")
        print(f"SECRET_KEY=s02tj6=n59q10!yqr4@c=l9s6s&o@0g(lxxdf1osbv1%h_b5rc")
        print(f"DEBUG=False")
        print(f"\n✅ Vercel will automatically provide DATABASE_URL")
    
    print(f"\n🚀 Next steps:")
    print(f"1. Set the environment variables in your Vercel dashboard")
    print(f"2. Deploy your application")
    print(f"3. Run migrations: python manage.py migrate")

if __name__ == "__main__":
    main()
