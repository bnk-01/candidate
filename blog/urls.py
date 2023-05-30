from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [


    path('', views.home),
    path('index/', login_required(views.PostList.as_view()), name='home'),
    path('about/', views.about),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]