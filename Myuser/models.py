from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.urls import reverse
# Create your models here.
class dwxx(models.Model):
    """
    单位信息

    """
    id = models.AutoField(primary_key=True)
    dwbm = models.IntegerField(verbose_name='单位编码')
    dwmc = models.CharField(max_length=50,verbose_name='单位名称')
    dwcwsx = models.CharField(max_length=10,verbose_name='单位财务属性')
    class Meta:
        verbose_name = '单位信息'
        verbose_name_plural = '单位信息'
    def __str__(self):
        return self.dwmc
    def natural_key(self):
        return(self.dwmc)
class dwxxManager(models.Manager):
    def get_by_natural_key(self, dwmc):
        return self.get(dwmc=dwmc)
class dclxxb(models.Model):
    id = models.AutoField(primary_key=True)
    # bh = models.IntegerField(verbose_name='编号')
    xm = models.CharField(max_length=10,verbose_name='姓名')
    ybh = models.IntegerField(verbose_name='医保号')
    dwmc = models.ForeignKey(dwxx,verbose_name='单位名称',default='')
    yhm = models.CharField(max_length=11,verbose_name='原电话号码',blank=True, null=True)
    xhm = models.CharField(max_length=11,verbose_name='新号码',default='')
    fbz = models.CharField(max_length=10,verbose_name='发布者')
    fbsj = models.DateTimeField(verbose_name='发布时间',auto_now_add=True)
    bz = models.CharField(max_length=10,verbose_name='备注',blank=True,null=True)
    class Meta:
        verbose_name='待处理信息表'
        verbose_name_plural='待处理信息表'
        permissions = (
            ('cl','处理'),
        )
    def __str__(self):
        return self.xm
    def natural_key(self):
        return (self.xm) + self.dwxx.natural_key()
    natural_key.dependencies = ['Myuser.dwxx']
    def get_absolute_url(self):
    	return reverse('dclxxb:detail',kwargs={'id':self.id})

class cljl(models.Model):
    id = models.AutoField(primary_key=True)
    # bh = models.ForeignKey(dclxxb,verbose_name='编号')
    xm = models.CharField(max_length=10,verbose_name='姓名')
    ybh = models.IntegerField(verbose_name='医保号')
    dwbm = models.ForeignKey(dwxx,verbose_name='单位编码')
    bglx = models.CharField(max_length=10,verbose_name='变更类型',blank=True, null=True)
    clz = models.CharField(max_length=10,verbose_name='处理者')
    clsj = models.DateTimeField(verbose_name='处理时间',auto_now_add=True)
    class Meta:
        verbose_name='处理记录表'
        verbose_name_plural='处理记录表'
    def __str__(self):
        return (self.clz,self.xm,self.ybh)
class UserAccount(models.Model):
    dept = models.ManyToManyField(dwxx,verbose_name="部门",default='')
    phone = models.CharField(max_length=11, null=True, blank=True, unique=True, verbose_name="手机号码")
    user = models.OneToOneField(User,verbose_name='用户名')
    class Meta:  
        verbose_name = u'用户信息'  
        verbose_name_plural = u'用户信息'  
    def __str__(self):
        return (self.user.username)



class Permission(models.Model):
    """
     quanxianguanli
    """
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=255)
