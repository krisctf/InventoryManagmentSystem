from django.contrib import admin
from django.urls import path, include  # Include for app-specific URLs

urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # Example: Add your app-specific URLs here
    path('inventory/', include('inventory.urls')),  # Replace 'inventory' with your app name
]
