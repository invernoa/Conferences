from django.urls import path

from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import url

urlpatterns = [

    path('', views.listing, name = 'listing'),
    path('conf/<int:pk>/', views.conf_detail, name='conf_detail'),
    path('conf/new/', views.conf_new, name='conf_new'),
    path('conf/<int:pk>/edit/', views.conf_edit, name='conf_edit'),
    path('conf/<int:pk>/add_comment', views.add_comment, name='add_comment'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),



]