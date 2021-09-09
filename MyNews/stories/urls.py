from django.urls import path
from stories import views


app_name = 'stories'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>/', views.blog, name='category'),
    path('story/<int:pk>/', views.single, name='single'),
    path('contact/', views.contact, name='contact'),
]
