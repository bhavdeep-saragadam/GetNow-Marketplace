from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from products.views import user_profile  # Import the new view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    # Include default authentication URLs with a different prefix
    path('accounts/', include('django.contrib.auth.urls')),
    path('user/profile/', user_profile, name='user_profile'),  # Add this line
]
