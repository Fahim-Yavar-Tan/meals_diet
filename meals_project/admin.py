from django.contrib import admin
from .models import *


# class OnlineUsersAdmin(admin.ModelAdmin):
#     # a list of displayed columns name.
#     list_display = ['__str__']


# admin.site.register(OnlineUsers, OnlineUsersAdmin)
admin.site.register(PersonalInfo)
# admin.site.register(BIOCHEMISTRY)
# admin.site.register(DietMeals)

# Register your models here.
