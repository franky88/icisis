from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from .models import SideNav
# Create your views here.
def mainLogin(request):
	# if request.user.is_authenticated():
	# 	if request.user.groups.filter(name="administrators").exists() or request.user.groups.filter(name="admins").exists():
	# 		links_to_display = SideNav.objects.all()
	# 		context = {
	# 			"links_to_display": links_to_display,
	# 		}
	# 	else:
	# 		links_to_display = SideNav.objects.all()
	# 		for link in links_to_display:
	# 			if request.user.groups.filter(name=link.read_only):
	# 				links_to_display = links_to_display.filter(read_only=link.read_only)
	# 		context = {
	# 			'links_to_display': links_to_display,
	# 		}
	# else:
	# 	links_to_display = SideNav.objects.filter(read_only="department_adviser")
	# 	context = {
	# 		'links_to_display': links_to_display,
	# 	}

	# 	next = request.GET.get('next', '/')
	# 	if request.method == "POST":
	# 		username = request.POST['username']
	# 		password = request.POST['password']
	# 		user=authenticate(username=username, password=password)

	# 		if user is not None:
	# 			if user.is_active:
	# 				login(request, user)
	# 				return HttpResponseRedirect(next)
	# 			else:
	# 				HttpResponse("Inactive user")
	# 		else:
	# 			return HttpResponseRedirect(settings.LOGIN_URL)
	# return render(request, "main/main_login.html", {"redirect_to": next})

	next = request.GET.get('next', '/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user=authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				HttpResponse("Inactive user")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "main/main_login.html", {"redirect_to": next})

def mainLogout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)