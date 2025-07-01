from . import views
from django.urls import path
from .views import create_new_emp_view, create_list_of_employes, delete_users_except_some

urlpatterns = [
    path('create_new_employees', create_new_emp_view),
    path('create_list_of_employes', create_list_of_employes, name="create_list_of_employes"),
    path('delete_users_except_some/', delete_users_except_some, name='delete_users_except_some'),
]