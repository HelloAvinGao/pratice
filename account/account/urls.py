"""account URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from demo import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tableData', views.tableDataViewSet)

urlpatterns = [
    path('things/', views.things),
    path('things/addData/', views.addData),
    path('things/addData/sendData/', views.sendData),
    # path('things/viewData/', views.viewData),
    path('things/searchData/', views.searchData),
    path('things/editData/', views.editData),
    path('things/editData/updateData/',views.updateData),
    path('documents/', views.documents),
    path('documents/upload/',views.upload),
    path('documents/download/',views.downloadFile),
    path('documents/delete/', views.deleteFile),
    path('check/', views.checks),
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('API/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
