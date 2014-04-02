# Create your views here.
from django.http import HttpResponse

def home(request):
        return HttpResponse('HelloWorld')

# Below is copied from Xing with comments taken out
# Create your views here.

from django.shortcuts import render, render_to_response


def playgroundDetail (request):
	return render (request, "playgroundApp/playground_info.html")

def playgroundList(request):
	return render (request, "playgroundApp/home.html")

def suggestPlayground(request):
	return render (request, "playgroundApp/playground_suggest.html")

def userProfile (request):
	return render (request, "playgroundApp/user_profile.html")

def userLogin (request):
	return render (request, "playgroundApp/user_login.html")

def userSignUp(request):
	return  render (request, "playgroundApp/user_signup.html")

def userSuggest(request):
	return  render (request, "playgroundApp/user_suggest.html")
