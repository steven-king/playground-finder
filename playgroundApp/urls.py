from django.conf.urls import patterns, url

from playgroundApp import views

urlpatterns=patterns('',
	url(r'^$', views.playgroundList, name='playgroundapp_home'),
	url(r'^playgroundapp/playground_info$', views.playgroundDetail, name='playground_info'),
	url(r'^playgroundapp/playground_suggest$', views.suggestPlayground, name='userSuggest'),
	url(r'^playgroundapp/user_profile$', views.userProfile, name='userProfile'),
	url(r'^playgroundapp/user_suggest$', views.userSuggest, name='userSuggest'),
	url(r'^playgroundapp/user_signup$', views.userSignUp, name='userSignUp'),
	url(r'^playgroundapp/user_login$', views.userLogin, name='userLogin'),
        url(r'^playgroundapp/map$', views.map, name='map'),
)