# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attendance(models.Model):
    employee = models.ForeignKey('Employees', models.DO_NOTHING)
    date = models.TextField()
    hours_worked = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Attendance'
    def __str__(self):
            return f"{self.employee.username} - {self.date} ({self.hours_worked} hrs"



class Employees(models.Model):
    username = models.TextField()

    class Meta:
        managed = False
        db_table = 'Employees'
    def __str__(self):
        return self.username
    