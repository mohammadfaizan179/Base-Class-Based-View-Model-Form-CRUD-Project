from django.contrib import admin
from enroll.models import Student_Model

# Register your models here.
@admin.register(Student_Model)
class Student_Model_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']