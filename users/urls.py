from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # USER URLS
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('change-password', views.change_password, name='change_password'),

    # ADHOC USERS URLS
    path('users/', views.user_list, name='user_list'),
    path('users/<int:id>/details/', views.user_details, name='user_details'),
    path('users/<int:id>/edit/', views.user_edit, name='user_edit'),
    path('users/addministryuser/', views.ministryuser_add, name='ministryuser_add'),
    path('users/addgovernor', views.governor_add, name='governor_add'),
    path('users/addpmp', views.pmp_add, name='pmp_add'),
    path('users/add-budget-user/', views.budget_add, name='budget_user_add'),
    path('users/add-due-process/', views.due_process_add, name='due_process_add'),
    path('users/<int:id>/delete/', views.user_delete, name='user_delete'),

    # service worker


]
