
from django.urls import path
from my_blog_app import views


urlpatterns = [
    path('home/', views.home,name='homepage'),
    path('postpage/', views.past_page,name='postpage'),
    path('register/', views.signup,name='register'),
]