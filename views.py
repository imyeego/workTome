from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from sql import *
import time




#def main(request):
#	t = get_template('main.html')
#	html = t.render(Context({'user' : 'liuzhao'}))
#	return HttpResponse(html)

def login(request):
	#now = datetime.datetime.now()
	#t = get_template('login.html')
	#html = t.render(Context({'time' : now}))
	return render_to_response('login.html',{'count': 1},context_instance=RequestContext(request))

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

		return render_to_response('main.html',{'username': username,'result': result},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def send_messenge(request):
	username = request.COOKIES.get('username','')
	

	if not username:
		return HttpResponseRedirect('/login/')
	else:
		current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
		current_time = time.strftime('%H:%M:%S',time.localtime(time.time()))
		content = request.POST['content']
		send_mess(username, current_date, current_time, content)
		return HttpResponseRedirect('/index/')

def test(request):
	t = ((1,2,3,4,5),(4,8,5,7,12),(2,6,9,8,7,4,))
	return render_to_response('test.html',{'t': t},context_instance=RequestContext(request))















