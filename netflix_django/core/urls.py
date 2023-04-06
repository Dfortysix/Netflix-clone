from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'core'

urlpatterns = [
    path("",views.index,name="index"),
    path("home/",views.index,name="home"),
    path("profiles/",views.ProfileList,name="profiles"),
    path("newprofiles/",views.new_profile,name="new"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout")



    
]