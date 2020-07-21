from django.contrib import admin

from User.models import User


class UserAdmin(admin.ModelAdmin):
    def sex(self):
        return '女' if self.sex else '男'
    list_display = ['username', 'password', 'age', sex]


admin.site.register(User, UserAdmin)