from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization-list/', OrganizationList.as_view(), name='organization-list'),
    path('organization-list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization-list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization-list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
]
