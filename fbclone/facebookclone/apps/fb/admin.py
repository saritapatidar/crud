from django.contrib import admin

from .models import CustomUser

@admin.register(CustomUser)
class users(admin.ModelAdmin):
    list_display=('username','email','phone_number')

