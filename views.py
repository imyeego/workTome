from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from sql import *
import time
import json
import os




#def main(request):
#	t = get_template('main.html')
#	html = t.render(Context({'user' : 'liuzhao'}))
#	return HttpResponse(html)

def login(request):
	#now = datetime.datetime.now()
	#t = get_template('login.html')
	#html = t.render(Context({'time' : now}))
	return render_to_response('login.html',{'count': 1},context_instance=RequestContext(request))

def signup(request):
	return render_to_response('signup.html',{'count': 1},context_instance=RequestContext(request))

def log_in(request):
		count = islogined(request.POST['username'], request.POST['passwd'])
		if count:
			username = toUsername(request.POST['username'],request.POST['passwd'])
			response = HttpResponseRedirect('/index/')
			response.set_cookie('username', username, 7200)
			return response
		else:
			
			t = get_template('login.html')
			c = Context({'count',count})
			return HttpResponse(t.render(c))

			#return render_to_response('login.html',{'count': count},context_instance=RequestContext(request))

#def search(request):
#	if 'sea' in request.POST:
#		message = 'You search for: %s' % request.POST['sea']
#	else:
#		message = 'You submmited an empty form.'
#	return HttpResponse(message)
def index(request):
	username = request.COOKIES.get('username','')
	if username:
		result = get_timeline(username)
		pic = get_user_pic(username)
		topics = gettopics()
		recommends = getrecommends(username)
		followings = getfollowings(username)
		followers = getfollowers(username)
		messenages = getmessenages(username)+1
		cur_time = int(time.time())

		for item in result:
			write_mess_log(item[0],username,cur_time)

		return render_to_response('main.html',{'messenages':messenages,'followers':followers,'followings':followings,'recommends':recommends,'topics':topics,'pic': pic[0][0],'result': result,'username':username},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def send_messenge(request):
	username = request.COOKIES.get('username','')
	file_obj = request.FILES.get('up_image', None)
	
	if not username:
		return HttpResponseRedirect('/login/')
	else:
		cur_time = int(time.time())
		
		content = request.POST['content']
		
		if file_obj:
			fname = file_obj.name
			fp = file(os.getcwd()+'/workTome/templates/images/'+ fname, 'wb')
			s = file_obj.read()
			fp.write(s)
			fp.close()
			send_mess(username, content,fname, cur_time)
			#insert_pic(get_mid(current_time),fname)

		else:
			send_mess_nopic(username, content,cur_time)

		return HttpResponseRedirect('/index/')


def upload(request):
	if request.method == "POST":
		file_obj = request.FILES.get('up_image',None)
		fname = file_obj.name
		fp = file('/templates/images/'+ file_obj.name, 'wb+')
		s = file_obj.read()
		fp.write(s)
		fp.close()

		return json.dumps({"files":[{"name":fname}]})

def join(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']

		count1 = isContainsUsername(username)
		count2 = isContainsUsername(email)
		if not count1 and not count2:
			
			passwd = request.POST['passwd']
			insert_user(username, email,passwd)
			return HttpResponseRedirect('/login/')

		else:
			t = get_template('signup.html')
			c = Context({'count1':count1,'count2':count2})
			return HttpResponse(t.render(c))

def profile(request):
	username = request.COOKIES.get('username','')
	if username:
		
		pic = get_user_pic(username)
		result = get_userinfo(username)
		messages = getMessByUsername(username)
		followings = getfollowings(username)
		followers = getfollowers(username)
		workexprences = getwork_exprencebyusername(username)
		eduexprences = getedu_exprencebyusername(username)

		return render_to_response('profile.html',{'eduexprences':eduexprences,'workexprences':workexprences,'followings':followings,'followers':followers,'pic': pic[0][0],'username':username,'result':result,'messages':messages},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def like(request):
	username = request.COOKIES.get('username','')
	if username:
		mid = request.POST['mid']
		count = mess_add_like(mid)
		
		t = get_template('main.html')
		c = Context({'count',count})
		return HttpResponse(t.render(c))
 

	else:
		return HttpResponseRedirect('/login/')

def follow(request):
	username = request.COOKIES.get('username','')
	if username:
		user_name = request.POST['user_name']
		count = action_follow(username,user_name)

		t = get_template('main.html')
		c = Context({'count',count})
		return HttpResponse(t.render(c))
	else:
		return HttpResponseRedirect('/login/')

def search(request):
	username = request.COOKIES.get('username','')
	if username:
		pic = get_user_pic(username)
		keyword = request.GET['keyword']
		per_count,person = search_person(keyword)
		com_count,company = search_company(keyword)
		top_count,topic = search_topic(keyword)
		mess_count,message = search_mess(keyword)

		t = get_template('search.html')
		c = Context({'keyword':keyword,'pic':pic[0][0],'per_count':per_count,'com_count':com_count,'top_count':top_count,'mess_count':mess_count,'person':person,'company':company,'topic':topic,'message':message})
		return HttpResponse(t.render(c))
	else:
		return HttpResponseRedirect('/login/')

def setting(request):
	username = request.COOKIES.get('username','')
	if username:
		pic = get_user_pic(username)
		t = get_template('settings.html')
		c = Context({'pic':pic[0][0],'username':username})
		return HttpResponse(t.render(c))
	else:
		return HttpResponseRedirect('/login/')
	 
def getNewMess(request):
	username = request.GET['username']
	if username:
		count_newmess = getnewmess(username)
		t = get_template('main.html')
		c = Context({'count_newmess',count_newmess})
		return HttpResponse(t.render(c))
	else:
		return HttpResponseRedirect('/login/')

def current_time(request):
	username = request.COOKIES.get('username','')
	if username:

		t = get_template('current_datetime.html')
		html = t.render(Context({'current_date' : time.time(),'username':username}))
		return HttpResponse(html)
	else:
		 return HttpResponseRedirect('/login/')
		















