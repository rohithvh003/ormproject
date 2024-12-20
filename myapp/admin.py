from django.contrib import admin
from myapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    i =['Sid','Sname','Smarks','Sage','Sgender','Splace']
admin.site.register(Student, StudentAdmin)
