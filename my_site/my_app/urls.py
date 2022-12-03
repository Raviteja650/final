from django.urls import path,URLPattern
from . import views

urlpatterns=[
    path('',views.sample),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name="signup"),
    path('getres/',views.getres),
    path('app/',views.appres),
    path('check/',views.checkuser,name="check"),

    ]