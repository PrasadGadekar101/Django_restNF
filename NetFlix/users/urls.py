
from django.urls import path
from .views import users_home, user_details

# path('articles/<yyyy:year>/', views.year_archive)
urlpatterns = [
    path('', users_home),
    path('<int:pk>/',user_details)
]