from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'project'

urlpatterns = [
    path('', views.landpage, name='landpage'),
    path('projectlist/', views.project_list, name='project_list'),
    path('years', views.YearList.as_view(), name='year_list'),
    path('year-detail/<int:pk>', views.YearDetail.as_view(), name='year_detail'),
    path('add-year', views.YearCreate.as_view(), name='year_create'),
    path('update-year/<int:pk>', views.YearUpdate.as_view(), name='year_update'),
    path('delete-year/<int:pk>', views.YearDelete.as_view(), name='year_delete'),
    #path('create-project', views.ProjectCreate.as_view(), name = 'project_create'),
    path('create-project', views.project_create, name='project_create'),
    path('project-detail/<int:pk>/',
         views.ProjectDetail.as_view(), name='project_detail'),
    path('project/<int:pk>/comment/', views.add_comment, name='comment_create'),
    path('project-delete/<int:pk>/',
         views.ProjectDelete.as_view(), name='project_delete'),
    path('pmp-project-update/<int:pk>/',
         views.PmpProjectUpdate.as_view(), name='pmp_project_update'),
    path('ministry-project-update/<int:pk>/',
         views.MinistryProjectUpdate.as_view(), name='ministry_project_update'),
    #path('pmp-projects', views.PmpProjects.as_view(), name='pmp_projects'),
    path('pmp-projects', views.pmp_project_list, name='pmp_projects'),
    #path('ministry-projects', views.MinistryProjects.as_view(), name='ministry_projects'),
    path('ministry-projects', views.ministry_project_list, name='ministry_projects'),
    #path('governor-projects', views.GovernorList.as_view(),name='governor_projects'),
    path('governor-projects', views.governor_project_list, name="governor_projects"),
    path('comment-detail/<int:pk>/',
         views.CommentDetail.as_view(), name='comment_detail'),
    path('comment/<int:pk>/delete', views.comment_delete, name='comment_delete'),
    path('comment-update/<int:pk>/',
         views.CommentUpdate.as_view(), name='comment_update'),
    path('pmp-reports', views.PmpReports.as_view(), name='pmp_reports'),
    path('ministry-reports', views.MinistryReports.as_view(),
         name='ministry_reports'),
    path('governor-reports', views.GovernorReports.as_view(),
         name='governor_reports'),
    path('add-report', views.ReportCreate.as_view(), name='create_report'),
    path('report/<int:pk>/', views.ReportDetail.as_view(), name='report_detail'),
    path('report-delete/<int:pk>/',
         views.ReportDelete.as_view(), name='report_delete'),
    path('report-update/<int:pk>/',
         views.ReportUpdate.as_view(), name='report_update'),
    path('dashboard/', views.dashboard, name='dashboard')
]
