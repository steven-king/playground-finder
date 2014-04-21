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
<<<<<<< HEAD
        url(r'^playgroundapp/newreview$', views.userReview, name='userReview'),
=======

        
        #urls for the user review page
        url(r'^$newreview/$', views.userReview, name='playground_new_review'),
        url(r'new_review.html', views.userReview, name='post_form_review'),
>>>>>>> cbb2b177efb1e14818e42762aa19148b8763b94b
        url(r'^playgroundapp/map$', views.map, name='map'),

)
