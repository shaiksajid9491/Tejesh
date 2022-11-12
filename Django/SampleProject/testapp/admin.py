from django.contrib import admin
from .models import Employee
# Register your models here.ye
class AdminEmployee(admin.ModelAdmin):
    list_display = ["name","salary","age","address","email"]
admin.site.register(Employee,AdminEmployee)