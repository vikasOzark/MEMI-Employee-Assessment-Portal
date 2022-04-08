from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin




@admin.register(QuesModel)
@admin.register(resultModel)
@admin.register(categories)

class questionAdmin(ImportExportModelAdmin):
    listdisplay=  ("username", "percent", "time")