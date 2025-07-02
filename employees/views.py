from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Employees, Attendance
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Func, F
from django.http import JsonResponse
from django.db.models import Case, When, IntegerField


@login_required
def employee_detail(request, id=None):
    if id:
        employee = get_object_or_404(Employees, pk=id)
        attendance_summary = (
            Attendance.objects
            .filter(employee=employee)
            .values('date')
            .annotate(
                total_hours=Func(
                    Sum('hours_worked'),
                    function='ROUND',
                    template='%(function)s(%(expressions)s, 2)'
                )
            )
            .order_by('date')
        )
        return render(request, 'employees/employee_detail.html', {
            'employee': employee,
            'attendance': attendance_summary,
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