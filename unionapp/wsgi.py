import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unionapp.settings')
application = get_wsgi_application()

# 🔥 Run migration and create superuser
try:
    django.setup()
    from django.core.management import call_command
    from django.contrib.auth import get_user_model

    # Run migrations
    call_command('migrate', interactive=False)

    # Create superuser if not exists
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin'
        )
        print("✅ Superuser 'admin' created.")
    else:
        print("ℹ️ Superuser 'admin' already exists.")

except Exception as e:
    print("❌ Error during startup:", str(e))
