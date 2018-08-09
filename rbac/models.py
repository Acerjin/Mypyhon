from django.db import  models
from django.contrib.auth.models import User
class Menu(models.Model):
    title = models.CharField(max_length=32,unique=True)
    parent = models.ForeignKey('Menu',null=True,blank=True)

    def __str__(self):
        # 显示层级菜单
        title_list = [self.title]
        p = self.parent
        while p:
            title_list.insert(0, p.title)
            p = p.parent
        return '-'.join(title_list)

class Permission(models.Model):
    """
    权限
    """
    title = models.CharField(max_length=32, unique=True)
    url = models.CharField(max_length=128, unique=True)
    menu = models.ForeignKey("Menu", null=True, blank=True)

    def __str__(self):
        # 显示带菜单前缀的权限
        return '{menu}---{permission}'.format(menu=self.menu, permission=self.title)

class Role(models.Model):
    """
    角色：绑定权限
    """
    title = models.CharField(max_length=32, unique=True)

    permissions = models.ManyToManyField("Permission")

    # 定义角色和权限的多对多关系

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """
    用户：划分角色
    """
    # username = models.CharField(max_length=32)
    # password = models.CharField(max_length=64)
    # nickname = models.CharField(max_length=32)
    # email = models.EmailField()
    user = models.OneToOneField(User,verbose_name='user',blank=True,null=True)
    roles = models.ManyToManyField("Role")
    # 定义用户和角色的多对多关系

    def __str__(self):
        return self.user.username