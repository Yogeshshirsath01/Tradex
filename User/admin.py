from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")

class PostAdmin(admin.ModelAdmin):
    list_display = ("users", "text", "created_at", "updated_at")


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
