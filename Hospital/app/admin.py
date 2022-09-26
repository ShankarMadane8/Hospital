from msilib.schema import AdminExecuteSequence
from django.contrib import admin
from .models import Patient,Doctor
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
   list_display=('user','first_name','last_name',"profile_picture","username",'email','password','confirm_password','address1','city','state','pincode')
    
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
   list_display=('first_name','last_name',"profile_picture","username",'email','password','confirm_password','address1','city','state','pincode')
    
    




