from django.contrib import admin
from enroll.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['stuid','stuname','stufathername','num']
admin.site.register(Student,StudentAdmin)