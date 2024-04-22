from django.contrib import admin
from django.urls import path, re_path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, OrgMemberList , OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView,  StudentList , StudentCreateView, StudentUpdateView, StudentDeleteView,  CollegeList , CollegeCreateView, CollegeUpdateView, CollegeDeleteView, ProgramList , ProgramCreateView, ProgramUpdateView, ProgramDeleteView
from studentorg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),

    path('organization-list/', OrganizationList.as_view(), name='organization-list'),
    path('organization-list/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization-list/<pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization-list/<pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),
    path('orgmember-list/', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmember-list/add/', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember-list/<pk>/', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember-list/<pk>/delete/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),
    path('student-list/', StudentList.as_view(), name='student-list'),
    path('student-list/add/', StudentCreateView.as_view(), name='student-add'),
    path('student-list/<pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student-list/<pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('college-list/', CollegeList.as_view(), name='college-list'),
    path('college-list/add/', CollegeCreateView.as_view(), name='college-add'),
    path('college-list/<pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('college-list/<pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),
    path('program-list/', ProgramList.as_view(), name='program-list'),
    path('program-list/add/', ProgramCreateView.as_view(), name='program-add'),
    path('program-list/<pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('program-list/<pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),
]
