from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Study, Comment, UserProfile

# Register your models here.

class UserProfileInline(admin.StackedInline):
  model = UserProfile
  can_delete = False

class UserAdmin(BaseUserAdmin):
  inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Study)
admin.site.register(Comment)