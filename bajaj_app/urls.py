from django.urls import path
from . import views

urlpatterns = [
    path('bfhl/', views.handle_data, name='handle_data'),
]
