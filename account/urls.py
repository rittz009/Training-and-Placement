from django.urls import path

from . import views

############### urls path are mentioned here ###############

urlpatterns = [
    path('',views.login, name = 'login'),   # path for login page
    path('studdashboard/<int:pk>',views.StudDashboardView, name = 'studdashboard'),  # path for Student Dashboard page
    path('TPOdashboard/<int:pk>',views.TPODashboardView, name = 'TPOdashboard'),   # path for Training Placement Dashboard page
    path('<int:pk>/jobapplication/', views.JobApplicationView, name = 'jobapplication'),   # path for Job Application page
    path('jobapplication_review/<int:pk>/', views.ReviewJobApplicationView, name = 'jobapplication_review'),   # path for reviewing Job Application page
]
