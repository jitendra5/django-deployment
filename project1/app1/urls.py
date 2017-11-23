from django.conf.urls import url
from app1 import views

app_name="app1"

urlpatterns=[
    url(r'^$', views.indexview, name='indexview'),
    url(r'^form/', views.formview, name='formview'),
    url(r'^contact/', views.contactview, name='contactview'),
    url(r'^login/', views.user_login, name='user_login'),
    url(r'^logout/', views.user_logout, name='user_logout'),
]
