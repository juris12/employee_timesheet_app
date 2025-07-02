from . import views
from django.urls import path

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('detail/<str:id>/', views.employee_detail, name='employee'),
    path('detail/<str:id>/date/<str:date>', views.employee_attendance_at_a_date),
    path('suggestions/', views.employee_names),
]