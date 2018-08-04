from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User 
import xadmin
from xadmin import views
# Register your models here.

from .models import dwxx,dclxxb,UserAccount

class dwxxAdmin(object):
	list_display = ['dwbm','dwmc','dwcwsx']
	# list_display = ('dwbm','dwmc','dwcwsx')
	# fields = [('dwbm','dwmc','dwcwsx'),]

class  dclxxbAdmin(object):
	"""docstring for  dcl"""
	list_display = ('xm','ybh','dwmc','fbz','fbsj')
	# fields = [('xm','ybh'),'dwmc','fbz']
	fieldsets = (
        (None, {
            'fields': [('xm', 'ybh','dwmc')]
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('xhm','yhm','fbz','bz'),
        }),
    )
	date_hierarchy='fbsj'
	list_filter=('dwmc',)
	list_per_page=5
class UserAccountAdmin(object):
	list_display = ('user','phone')
	fields = ['user','dept','phone']

class GlobalSetting(object):
 	"""docstring for GlobalSetting"""
 	site_title='Acerjin'
 	site_footer= 'Acerjin'
 		 
xadmin.site.register(dwxx,dwxxAdmin)
xadmin.site.register(dclxxb,dclxxbAdmin)
xadmin.site.register(UserAccount,UserAccountAdmin)
# xadmin.site.unregister(User)  
# xadmin.site.register(User, testUserAdmin)  