from django.contrib import admin
from django.urls import path,include
from . import views
from .views import authView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("signup/", views.authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("",views.home, name="home")
]
