from django.contrib import admin
from myApp.models import *


class Custom_User_Display(admin.ModelAdmin):
    list_display=['username','user_type','email']
admin.site.register(Custom_User,Custom_User_Display)
