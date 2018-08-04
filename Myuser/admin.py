from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User 
# import xadmin
# Register your models here.

from .models import dwxx,dclxxb,UserAccount

class dwxxAdmin(admin.ModelAdmin):
	list_display = ('dwbm','dwmc','dwcwsx')
	fields = [('dwbm','dwmc','dwcwsx'),]

class  dclxxbAdmin(admin.ModelAdmin):
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
class UserAccountAdmin(admin.ModelAdmin):
	list_display = ('user','phone')
	fields = ['user','dept','phone']
	actions = ['changephone']
	def changephone(self,request,queryset):
		for q in queryset:
			q.phone = q.user.id
			q.save()
		print (q)
	changephone.short_description = "phone_changed!"
class userProfileForm(forms.ModelForm):
	dwxx = dwxx.objects.all().values_list('id','dwmc')
	gldw =[]
	# for x in dwxx:
	# 	gldw.append()
	# print (dwxx,'111')
	# gldw1 =['111',]
	dept = forms.MultipleChoiceField(label='管理单位',choices=dwxx,widget=forms.CheckboxSelectMultiple())
	class Meta:
		models=UserAccount
		fields=['phone','user']
class profileInline(admin.StackedInline):  
    model = UserAccount  
    form = userProfileForm 
class testUserAdmin(UserAdmin):  
    inlines = [profileInline,]  
admin.site.register(dwxx,dwxxAdmin)
admin.site.register(dclxxb,dclxxbAdmin)
admin.site.register(UserAccount,UserAccountAdmin)
# admin.site.unregister(User)  
# admin.site.register(User, testUserAdmin)  