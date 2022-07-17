"""AFISHA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from movie_app import views
from . import swagger
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/directors/", views.DirectorModelViewSet.as_view({'get':'list','post':'create'})),
    path("api/v1/directors/<int:pk>/", views.DirectorModelViewSet.as_view({'get':'retrieve',
                                                                            'put':'update',
                                                                            'delete':'destroy'})),
    path("api/v1/movie/", views.MovieModelViewSet.as_view({'get':'list','post':'create'})),
    path("api/v1/movie/<int:pk>/", views.MovieModelViewSet.as_view({'get':'retrieve',
                                                                    'put':'update',
                                                                    'delete':'destroy'})),
    path("api/v1/movie/reviwe/", views.ReviewModelViewSet.as_view({'get':'list','post':'create'})),
    path("api/v1/movie/reviwe/<int:pk>/", views.ReviewModelViewSet.as_view({'get':'retrieve',
                                                                            'put':'update',
                                                                            'delete':'destroy'})),
    path('api/v1/login/', views.LoginAPIView.as_view()),
    path('api/v1/register/', views.RegisterAPIView.as_view()),
    path('api/v1/ganrs/', views.GanreAPIView.as_view()),
    path('api/v1/ganrs/<int:pk>/', views.GanreItemUpdateDeleteAPIView.as_view()),
    path('api/v1/tags/', views.TagModelViewSet.as_view({'get':'list','post':'create'})),
    path('api/v1/tags/<int:pk>', views.TagModelViewSet.as_view({'get':'retrieve',
                                                             'put':'update',
                                                             'delete':'destroy'})),



]
urlpatterns += swagger.urlpatterns
