from django.contrib.auth.urls import path
from .views import *


urlpatterns = [

    path('user/', UserProfileViewSets.as_view({"get": "list", "post": "create"}), name='userprofile_list'),
    path('user/<int:pk>/', UserProfileViewSets.as_view({"get": "retrieve", 'put': 'update', 'delete': "destroy"}), name='userprofile_detail'),

    path('course/', CourseViewSets.as_view({"get": "list", "post": "create"}), name='course_list'),
    path('course/<int:pk>/', CourseViewSets.as_view({"get": "retrieve", 'put': 'update', 'delete': "destroy"}),name='course_detail'),
    path('module/', ModuleViewSets.as_view({"get": "list", "post": "create"}), name='module_list'),
    path('module/<int:pk>/', ModuleViewSets.as_view({"get": "retrieve", 'put': 'update', 'delete': "destroy"}), name='module_detail'),
    path('enrollment/', EnrollmentViewSets.as_view({"get": "list", "post": "create"}), name='enrollment_list'),
    path('enrollment/<int:pk>/', EnrollmentViewSets.as_view({"get": "retrieve", 'put': 'update', 'delete': "destroy"}), name='enrollment_detail'),
    path('assignment/', AssignmentViewSets.as_view({"get": "list", "post": "create"}), name='assignment_list'),
    path('assignment/<int:pk>/', AssignmentViewSets.as_view({"get": "retrieve", 'put': 'update', 'delete': "destroy"}), name='assignment_detail'),
    path('submission/', SubmissionViewSets.as_view({"get": "list", "post": "create"}), name='submission_list'),
    path('user/<int:pk>/', SubmissionViewSets.as_view({"get": "retrieve", 'put': 'update', 'delete': "destroy"}), name='submission_detail'),
    path('grade/', GradeViewSets.as_view({"get": "list", "post": "create"}), name='grade_list'),
    path('grade/<int:pk>/', GradeViewSets.as_view({"get": "retrieve", 'put': 'update', 'delete': "destroy"}), name='grade_detail'),
    path('certificate/', CertificateViewSets.as_view({"get": "list", "post": "create"}), name='certificate_list'),
    path('certificate/<int:pk>/', CertificateViewSets.as_view({"get": "retrieve", 'put': 'update', 'delete': "destroy"}), name='certificate_detail'),
]