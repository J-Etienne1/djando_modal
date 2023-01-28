
from django.contrib import admin
from django.urls import path, include

# Import the 'home' and 'away' module
import home.urls
import away.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('away/', include('away.urls')),
]

