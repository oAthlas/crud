from . import views
from django.urls import path

urlpatterns = [
    path('', views.create_user, name='create_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
]