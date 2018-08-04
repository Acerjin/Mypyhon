from django.shortcuts import render,render_to_response,redirect
from django.http.response import HttpResponse
# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from Myuser.forms import dclxxbform,Userform
from django.forms import formset_factory
from .models import dclxxb,UserAccount
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import *  
from django.contrib.auth.models import User
from Mypython.settings import LOGIN_URL
import json
from django.core import serializers
import datetime
from datetime import timedelta
@login_required
def index(request):
	"""
	首页，获取待处理记录；处理POST记录数据
	"""
	df = formset_factory(dclxxbform)
	dwbmlist = []
	username = request.user.username
	# print (request.user.id,request.user.username)
	userinfo = UserAccount.objects.filter(user_id=request.user.id)		
	if userinfo:
		print (userinfo.first().dept.values_list())
		for x in userinfo.first().dept.values_list():
			dwbmlist.append(x[0])
		dclxxbformset = formset_factory(dclxxbform,extra=1,can_order=True,can_delete=True)
		dclxxbformset = dclxxbformset()	
	if request.method =='POST':
		dcl = dclxxb.objects.filter(dwmc_id__in=dwbmlist).order_by('-fbsj')
		postdata = df(request.POST)
		# print (postdata)
		if postdata.is_valid():
			for p in postdata:
				# print (p.cleaned_data['xm'])
				p.save()
			# return HttpResponse('{"status":"success"}',content_type='application/json')
			
			return render(request, 'index.html',{'f':dclxxbformset,'dcl':dcl})		
		else:
			# print (postdata)
			# print ('badxxx')
			# print (postdata.errors[0]['xhm'])
			return HttpResponse('{"status":"failure","msg":"格式不合法"}',content_type='application/json')
	# form = dwxxform()
	else:
		if userinfo:
			dcl = dclxxb.objects.filter(dwmc_id__in=dwbmlist).order_by('-fbsj')
			return render(request, 'index.html',{'f':dclxxbformset,'dcl':dcl})
			# return render(request, 'index.html',locals())
		else:
			return HttpResponse('weifenpei')
def index_ajax(request):
	dwbmlist=[] 
	dcllist=[]
	userinfo = UserAccount.objects.filter(user_id=request.user.id)
	# print ('dept',dept)		
	if userinfo:
		for x in userinfo.first().dept.values_list():
			dwbmlist.append(x[0])
	df = formset_factory(dclxxbform)
	if request.method=='POST':
		postdata = df(request.POST)
		if postdata.is_valid():
			for p in postdata:
				# print (p.as_table)
				p.save()
			dcl = dclxxb.objects.filter(dwmc_id__in=dwbmlist).order_by('-fbsj')
			data = serializers.serialize("json",dcl,use_natural_foreign_keys=True)
			return HttpResponse(data,content_type='application/json')
		else:
			return HttpResponse(json.dumps({'status':'failure','msg':postdata.errors}),content_type='application/json')
def regist(request):
	if request.method == 'POST':
		userform = Userform(request.POST)
		if userform.is_valid():
			username = userform.cleaned_data['username']
			password = userform.cleaned_data['password']
			email = userform.cleaned_data['email']
			User.objects.create_user(username=username,password=password,email=email,is_staff=True,is_active=True)
			# User.save()
			return HttpResponseRedirect(LOGIN_URL)
		else:
			errorsstr = userform.errors.as_json()
			e = json.loads(errorsstr)
			print (e['username'][0])
			return render_to_response('regist.html',{'userform':userform,'errorstr':json.loads(errorsstr)})

	else:
		userform = Userform()
	return render_to_response('regist.html',{'userform':userform})	
now = datetime.datetime.utcnow()
delta = timedelta(seconds=500)
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# print (username,password)
		user=auth.authenticate(username=username,password=password)
		# user = auth.au(username__exact=username,password__exact=password)
		if user:
			auth.login(request,user)
			obj = redirect('/Myuser/index')
			value=now+delta
			obj.set_cookie("tile","zhanggen",expires=value,path='/',domain=None,secure=False,httponly=False)
			request.session.set_expiry(3600)
			return obj
		else:
			return HttpResponse('error')
	else:
		userform = Userform()
		# print (userform)
	return render(request,'login.html',{'userform':userform})
	# return HttpResponse('ok')
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/Myuser/login')