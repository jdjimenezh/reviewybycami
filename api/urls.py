from django.urls import path
from api.views import HomeView

app_name = 'api'

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
]