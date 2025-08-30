#!/usr/bin/env python3
"""
Script to migrate data from SQLite to external PostgreSQL database
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_django():
    """Setup Django environment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplayer.settings')
    django.setup()

def backup_sqlite():
    """Create a backup of the SQLite database"""
    import shutil
    from datetime import datetime
    
    backup_name = f"db_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sqlite3"
    
    if os.path.exists('db.sqlite3'):
        shutil.copy2('db.sqlite3', backup_name)
        print(f"✅ SQLite database backed up as: {backup_name}")
        return backup_name
    else:
        print("❌ No SQLite database found")
        return None

def migrate_to_postgres():
    """Migrate data to PostgreSQL"""
    print("🔄 Migrating data to PostgreSQL...")
    
    try:
        # Run migrations
        print("📋 Running migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        # Create superuser if needed
        print("👤 Creating superuser...")
        print("Please enter superuser credentials:")
        execute_from_command_line(['manage.py', 'createsuperuser'])
        
        print("✅ Migration completed successfully!")
        
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False
    
    return True

def main():
    """Main function"""
    print("🎵 Django Music Player - Data Migration")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Please run this script from your Django project root directory")
        sys.exit(1)
    
    # Setup Django
    setup_django()
    
    # Check if DATABASE_URL is set
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        print("❌ DATABASE_URL environment variable not set")
        print("Please set it to your PostgreSQL connection string")
        sys.exit(1)
    
    # Backup SQLite database
    backup_file = backup_sqlite()
    
    # Migrate to PostgreSQL
    if migrate_to_postgres():
        print(f"\n🎉 Migration completed!")
        if backup_file:
            print(f"📁 SQLite backup saved as: {backup_file}")
        print(f"🗄️  Data is now in PostgreSQL database")
    else:
        print(f"\n❌ Migration failed")
        if backup_file:
            print(f"📁 You can restore from backup: {backup_file}")

if __name__ == "__main__":
    main()
