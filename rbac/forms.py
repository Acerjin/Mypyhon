from django.forms import ModelForm
from .models import UserInfo
from .models import Role,Permission,Menu



class UserInfoModelForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
        labels = {
            'username': '用户名',
            'password': '密码',
            'nickname': '昵称',
            'email': '邮箱',
            'roles': '角色',
        }
class RoleModelForm(ModelForm):
    class Meta:
        model = Role
        fields = '__all__'
        labels = {
            'title': 'mc',
            'permissions': 'qx',
        }
class PermissionModelForm(ModelForm):
    class Meta:
        model = Permission
        fields = '__all__'
        labels = {
            'title': 'mc',
            'url': 'dz',
            'menu':'cd',
        }
class MenuModelForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        labels = {
            'title': 'mc',
            'parent':'fcd'
        }