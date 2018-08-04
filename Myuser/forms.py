from django.forms import ModelForm
import re
# Create your views here.
from django import forms
from Myuser.models import dclxxb,dwxx

class dclxxbform(ModelForm):
	"""docstring for dwxxform"""
	class Meta:
		model = dclxxb
		fields = ['xm','ybh','dwmc','yhm','xhm','bz','fbz']
		# fields = '__all__'
	def clean_xhm(self):
		xhm = self.cleaned_data['xhm']
		print(xhm)
		xhm_regex = r'^1[34578]\d{9}$'
		p = re.compile(xhm_regex)
		if xhm:
			if p.match(xhm):
				return xhm
			else:
				raise forms.ValidationError('手机号非法',code='invalid xhm')
		else:
			raise forms.ValidationError('手机号为空',code='none xhm')

class Userform(forms.Form):
	error_css_class = 'error'

	username = forms.CharField(label='用户名',max_length=50)
	password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class':'sfda'}))
	email = forms.EmailField(label='邮箱')
	
	def clean_username(self):
		username = self.cleaned_data['username']
		un_len = len(username)
		print (un_len)
		if un_len<10:
			raise forms.ValidationError('username is too short!')
		else:
			return username
	def clean_password(self):
		password = self.cleaned_data['password']
		pw_len = len(password)
		print (pw_len)
		if pw_len<10:
			raise forms.ValidationError('password is too short!')
		else:
			return password
