from django.conf.urls import patterns, url

from playgroundApp import views

urlpatterns=patterns('',
	url(r'^$', views.Playground_List, name='playgroundApp_home'),
	url(r'^playgroundApp/playground_info$', views.Playground, name='playground_info'),
	url(r'^playgroundApp/playgroundSuggest$', views.suggestPlayground, name='userSuggest'),
	url(r'^playgroundApp/userProfile$', views.userProfile, name='userProfile'),
	url(r'^playgroundApp/userSuggest$', views.userSuggest, name='userSuggest'),
	url(r'^playgroundApp/userSignup$', views.userSignUp, name='userSignUp'),
	url(r'^playgroundApp/userLogin$', views.userLogin, name='userLogin'),
)
