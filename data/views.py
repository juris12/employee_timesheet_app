from django.shortcuts import render, redirect
from employees.models import Employees, Attendance
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

import csv
import io
import random
from datetime import datetime, timedelta

@login_required
def create_new_emp_view(request):
    mesage = request.GET.get('mesage')
    mesage_obj = {
        "mesage": mesage,
        "is_error": 0
    }
    return render(request, 'data/create_new_emp.html',{"mesage_obj":mesage_obj})


@login_required
def create_list_of_employes(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return HttpResponse('No file uploaded!')

        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8-sig') 
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)
        reader.fieldnames = [name.strip() for name in reader.fieldnames]
        max_rows = 300
        created_users = 0

        for i, row in enumerate(reader):
            print(i, row)
            if i >= max_rows:
                break

            first_name = row.get('First Name', '').strip()
            last_name = row.get('Last Name', '').strip()

            if not first_name or not last_name:
                continue

            username = f"{first_name.capitalize()} {last_name.capitalize()}"
            print(username)
            if Employees.objects.filter(username=username).exists():
                continue
            employee = Employees.objects.create(username=username)

            end_date = datetime.today().date()
            start_date = (end_date - timedelta(days=30*6))

            current_date = start_date
            while current_date <= end_date:
                days_in_month = random.randint(0, 20)
                month_start = current_date.replace(day=1)
                next_month = (month_start + timedelta(days=32)).replace(day=1)
                days_in_this_month = (next_month - month_start).days

                attendance_days = random.sample(range(1, days_in_this_month+1), k=min(days_in_month, days_in_this_month))
                for day in attendance_days:
                    date_of_attendance = month_start.replace(day=day)
                    for _ in range(3):
                        hours_worked = round(random.uniform(0, 15), 2)
                        if hours_worked == 0:
                            continue
                        Attendance.objects.create(
                            employee=employee,
                            date=date_of_attendance.strftime('%Y-%m-%d'),
                            hours_worked=hours_worked
                        )
                current_date = next_month

            created_users += 1

        mesage = f'Successfully created {created_users} employees and their attendance records.'
        return redirect(f'/data/create_new_employees?mesage={mesage}')

    else:
        return HttpResponse('Invalid request method!')
    
@login_required
@require_POST
def delete_users_except_some(request):
    keep_ids = [1, 2, 3, 4]
    users_to_delete = Employees.objects.exclude(id__in=keep_ids)
    Attendance.objects.filter(employee__in=users_to_delete).delete()
    users_to_delete.delete()
    mesage = f"Deleted all users except IDs {keep_ids} and their attendances."
    return redirect(f'/data/create_new_employees?mesage={mesage}')
