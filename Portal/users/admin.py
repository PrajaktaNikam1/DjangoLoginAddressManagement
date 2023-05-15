from django.contrib import admin
from .models import Address,File,Profile_img
# Register your models here.


class Profile_img_Admin(admin.ModelAdmin):
    list_display = ['id','user','image']

class Address_Admin(admin.ModelAdmin):
    list_display = ['id','user','street','city','state','zip_code','number']

class File_Admin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name','email','file','date_uploaded']


admin.site.register(Profile_img,Profile_img_Admin)
admin.site.register(Address,Address_Admin)
admin.site.register(File,File_Admin)