from django.contrib import admin

from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']

    class Meta:
        model = MyUser


admin.site.register(MyUser, MyUserAdmin)
