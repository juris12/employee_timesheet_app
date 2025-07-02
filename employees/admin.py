from django.contrib import admin
from .models import Employees, Attendance
from django import forms

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    search_fields = ('username',)


class AttendanceForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
    )

    class Meta:
        model = Attendance
        fields = '__all__'

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    form = AttendanceForm
    list_display = ('id', 'employee', 'date', 'hours_worked')
    search_fields = ('employee__username', 'date')
    list_filter = ('date', 'employee')