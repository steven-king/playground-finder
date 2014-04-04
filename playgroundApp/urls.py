from django.conf.urls import patterns, url

from playgroundApp import views

urlpatterns=patterns('',
<<<<<<< HEAD
	url(r'^$', views.playgroundList, name='playgroundapp_home'),
	url(r'^playgroundapp/playground_info$', views.playgroundDetail, name='playground_info'),
	url(r'^playgroundapp/playground_suggest$', views.suggestPlayground, name='userSuggest'),
	url(r'^playgroundapp/user_profile$', views.userProfile, name='userProfile'),
	url(r'^playgroundapp/user_suggest$', views.userSuggest, name='userSuggest'),
	url(r'^playgroundapp/user_signup$', views.userSignUp, name='userSignUp'),
	url(r'^playgroundapp/user_login$', views.userLogin, name='userLogin'),
)
=======
	url(r'^$', views.Playground_List, name='playgroundApp_home'),
	url(r'^playgroundApp/playground_info$', views.Playground, name='playground_info'),
	url(r'^playgroundApp/playgroundSuggest$', views.suggestPlayground, name='userSuggest'),
	url(r'^playgroundApp/userProfile$', views.userProfile, name='userProfile'),
	url(r'^playgroundApp/userSuggest$', views.userSuggest, name='userSuggest'),
	url(r'^playgroundApp/userSignup$', views.userSignUp, name='userSignUp'),
	url(r'^playgroundApp/userLogin$', views.userLogin, name='userLogin'),
)
>>>>>>> 2a58c0eadb1d262ee2f01f576d392a1b12f13187
