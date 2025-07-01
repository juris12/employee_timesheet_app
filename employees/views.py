from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Employees, Attendance
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum

@login_required
def employee_detail(request, id=None):
    if id:
        employee = get_object_or_404(Employees, pk=id)
        attendance_summary = (
            Attendance.objects
            .filter(employee=employee)
            .values('date')
            .annotate(total_hours=Sum('hours_worked'))
            .order_by('date')
        )
        return render(request, 'employees/employee_detail.html', {
            'employee': employee,
            'attendance': attendance_summary,
            'num_rows': attendance_summary.count()
        })


@login_required
def employee_list(request):
    query = request.GET.get('q')
    if query:
        employees = Employees.objects.filter(username__icontains=query)
    else:
        employees = Employees.objects.all()

    return render(request, 'employees/employee_list.html', {
        'employees': employees,
        'num_rows': employees.count()
    })