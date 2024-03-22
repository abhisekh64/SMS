from django.contrib import admin
from .models import Employee


# Register your models here.
@admin.register(Employee)
class ShowEmployee(admin.ModelAdmin):
    list_display = ["name","email","department","position","salary"]
