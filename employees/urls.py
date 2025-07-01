from . import views
from django.urls import path

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('<str:id>/', views.employee_detail, name='employee'),
]