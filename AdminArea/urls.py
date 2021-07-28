from django.urls import path
from . import views
AdminArea = "AdminArea"
urlpatterns = [
    path('', views.index,name='index'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('AdminDashboard/',views.AdminDashboard,name='AdminDashboard'),

    path('Users/',views.Users,name='Users'),
    path('InstituteDetailes/',views.InstituteDetailes,name='InstituteDetailes'),

    path('AddAdminUser/',views.AddAdminUser,name='AddAdminUser'),
    path('EnrollStudentInquiry/',views.EnrollStudentInquiry,name='EnrollStudentInquiry'),
    path('InquiryLists/',views.InquiryLists,name='InquiryLists'),

    path('AdminProfile/',views.AdminProfile,name='AdminProfile'),
    path('AdminChangePassword/',views.AdminChangePassword,name='AdminChangePassword'),
    path('AdminLockScreen/',views.AdminLockScreen,name='AdminLockScreen'),


     path('admin_logout/',views.admin_logout,name='admin_logout'),
    ]