from django.urls import path
from . import views

app_name = 'lga'

urlpatterns = [
    path('lgalist', views.LgaList.as_view(), name = 'lga_list'),
    path('lgacreate', views.LgaCreate.as_view(), name = 'lga_create'),
    path('lgadetail/<int:pk>/', views.LgaDetail.as_view(), name = 'lga_detail'),
    path('lgadelete/<int:pk>/', views.LgaDelete.as_view(), name = 'lga_delete'),
    path('lgaupdate/<int:pk>/', views.LgaUpdate.as_view(), name = 'lga_update')
]