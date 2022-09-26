



from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("Hospital/dashboard/",views.Dashboard,name="dashboard"),
    path("",views.Signup,name="signup"),
    path("Hospital/login/",views.Login,name="login"),
    path("Hospital/logout/",views.logout,name="logout")

]
