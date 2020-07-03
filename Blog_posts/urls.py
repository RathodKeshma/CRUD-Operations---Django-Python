from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('crud/', views.BlogUserView.as_view(), name ="BlogUserView"),
    path('list/', views.BlogUserView.listUser, name='listUser'),
    path('delete/<int:id>', views.BlogUserView.deleteUser, name='deleteUser'),
    path('post/', views.BlogUserView.createUser, name='createUser'),
    path('post/<int:id>', views.BlogUserView.createUser, name='update_User'),


]