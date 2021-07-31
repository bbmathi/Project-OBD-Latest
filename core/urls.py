# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this
from webapp import views

urlpatterns = [
            # Django admin route
    path("", include("authentication.urls")),
    path('admin/', admin.site.urls),  # Auth routes - login / register
    path('app',include('app.urls')),
    path("api/getlatlan_tag1", views.MyApi_Tag1.as_view()),
    path("api/getlatlan_tag2", views.MyApi_Tag2.as_view()),
    path("api/getlatlan_tag3", views.MyApi_Tag3.as_view()),
    path("api/RPM_tag1", views.MyApi_Rpm_Tag1.as_view())
     ]

