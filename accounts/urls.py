from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('adm/users/', views.UserListView.as_view(), name='adm_list_user'),
    path('adm/users/create', views.UserCreateView.as_view(), name='adm_create_user'),
    path('adm/users/edit/<int:pk>', views.UserListView.as_view(), name='adm_edit_user'),
    path('adm/users/delete/<int:pk>', views.UserListView.as_view(), name='adm_delete_user'),


]
