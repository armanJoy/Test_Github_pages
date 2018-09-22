from django.conf.urls import url
from django.urls import path
from cricket import views

urlpatterns = [
    path('', views.cricket, name='cricket'),
]

urlpatterns +=[
    path('Abc/', views.abc),
    path('base/', views.base),
    path('sample/', views.sample),
    path('creatematch/', views.MatchRegistrationView.as_view(), name='macth_registration'),
]