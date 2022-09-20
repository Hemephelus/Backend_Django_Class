
from django.urls import path
from my_blog_app import views


urlpatterns = [
    path('home/', views.home,name='homepage'),
    path('postpage/<int:pk>', views.post_page,name='postpage'),
    path('register/', views.signup,name='register'),
    path('last-post/<int:pk>', views.last_post,name='lastpostpage'),
]