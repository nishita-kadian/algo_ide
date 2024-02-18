from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('profile/<str:pk>/', views.profile, name="profile"),

    path('create_profile', views.createUser, name="create_profile"),
    path('update_profile/<str:pk>/', views.updateUser, name="update_profile"),
    # path('delete_profile/<str:pk>', views.deleteUser, name="delete_profile"),
    # path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    # path('', views.save_snippets, name='save_snippets'),
]
