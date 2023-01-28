from django.urls import path
from .views import AwayPageView

urlpatterns = [
    path('', AwayPageView.as_view(), name='home'),
]
