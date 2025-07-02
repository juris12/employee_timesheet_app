from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Employees, Attendance
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Min, Max, Sum, Func, F
from django.http import JsonResponse
from django.db.models import Case, When, IntegerField
import statistics
import json


@login_required
def employee_detail(request, id=None):
    if id:
        employee = get_object_or_404(Employees, pk=id)
        sort = request.GET.get('sort') == 'DESC'
        attendance = Attendance.objects.filter(employee=employee)
        attendance_summary = (
            attendance.values('date')
            .annotate(
                total_hours=Func(
                    Sum('hours_worked'),
                    function='ROUND',
                    template='%(function)s(%(expressions)s, 2)'
                )
            )
            .order_by(f'{"" if sort else "-"}date')
        )
        hours_list = list(attendance.values_list('hours_worked', flat=True))
        average = round(statistics.mean(hours_list), 2) if hours_list else 0
        median = round(statistics.median(hours_list), 2) if hours_list else 0
        min_val = round(min(hours_list), 2) if hours_list else 0
        max_val = round(max(hours_list), 2) if hours_list else 0

        dates_for_chart = [entry['date'] for entry in attendance_summary]
        hours_for_chart = [entry['total_hours'] for entry in attendance_summary]
        return render(request, 'employees/employee_detail.html', {
            'employee': employee,
            'attendance': attendance_summary,
            'average': average,
            'median': median,
            'min': min_val,
            'max': max_val,
            'dates_for_chart': json.dumps(dates_for_chart),
            'hours_for_chart': json.dumps(hours_for_chart),
            'num_rows': attendance_summary.count()
        })
@login_required
def employee_attendance_at_a_date(request, id=None, date=None):
    if id:
        employee = get_object_or_404(Employees, pk=id)
        attendance = Attendance.objects.filter(employee=employee, date=date)
        total = attendance.aggregate(total_hours=Sum('hours_worked'))['total_hours'] or 0
        return render(request, 'employees/attendance_at_a_date.html', {
            'employee': employee,
            'date': date,
            'attendance': attendance,
            'total': total,
            'num_rows': attendance.count()
        })

@login_required
def employee_list(request):
    query = request.GET.get('q')
    limit = int(request.GET.get('limit') or 60)

    if query:
        employees = Employees.objects.filter(username__icontains=query)[:limit]
    else:
        employees = Employees.objects.all()[:limit]

    return render(request, 'employees/employee_list.html', {
        'employees': employees,
        'num_rows': employees.count()
    })

@login_required
def employee_names(request):
    search_text = request.GET.get('search_text', '')
    suggestions = Employees.objects.annotate(
        starts_with=Case(
            When(username__istartswith=search_text, then=1),
            default=0,
            output_field=IntegerField(),
        )
    ).filter(username__icontains=search_text).order_by('-starts_with', 'username').values('username')[:10]
    suggestion_list = [entry['username'] for entry in suggestions]
    return JsonResponse(suggestion_list, safe=False)