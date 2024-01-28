from django.contrib import admin
from .models import Student

# Register your models here.
class adminmodel(admin.ModelAdmin):
    list_display=('id','name','email','password','mobile','address')
    
admin.site.register(Student,adminmodel)    
    