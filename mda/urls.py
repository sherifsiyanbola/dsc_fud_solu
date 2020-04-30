from django.urls import path
from . import views

app_name = 'mda'

urlpatterns = [
    path('ministrylist', views.MinistryList.as_view(), name = 'ministry_list'),
    path('ministrycreate', views.MinistryCreate.as_view(), name = 'ministry_create'),
    path('ministrydetail/<int:pk>/', views.MinistryDetail.as_view(), name = 'ministry_detail'),
    path('ministrydelete/<int:pk>/', views.MinistryDelete.as_view(), name = 'ministry_delete'),
    path('ministryupdate/<int:pk>/', views.MinistryUpdate.as_view(), name = 'ministry_update')
]