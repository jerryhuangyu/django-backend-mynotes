from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name="notes"),
    path('notes/<str:pk>/', views.getNote, name="note"),
]