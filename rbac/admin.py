from django.contrib import admin
from .models import UserInfo,Role,Permission,Menu
# Register your models here.


class UserinfoAdmin(admin.ModelAdmin):
    list_display = ('user',)
    fields = ('user','roles')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title','parent')
    fields = ('title','parent')
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fields = ('title','permissions')
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('title','url','menu')
    fields = ('title','url','menu')
admin.site.register(UserInfo,UserinfoAdmin)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Permission,PermissionAdmin)