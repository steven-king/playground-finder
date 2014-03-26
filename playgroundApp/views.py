# Create your views here.
from django.http import render, get_object_or_404, redirect, render_to_response
from playgroundApp.models import Playground
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from playgroundApp.forms import addPlaygroundForm
def home(request):
        return HttpResponse('HelloWorld')

def Playground (request, pk):
	Playerground=get_object_or_404 (Playground, id=pk)
	return render (request, 'playgroundApp/playground_info.html', {"Playground": Playground})

def Playground_List(request):
	#playground_list=Playground.object.all()
	#paginator=Paginator(playground_list, 10)
	#page=request.GET.get('page')

	#try:
		#playgrounds=paginator.page(page)
	#except PageNotAnInteger:
		#playgrounds=paginator.page(1)
	#except Emptypage:
		#playgrounds=paginator.page(paginator.num_pages)
	#return render (request, 'playgroundApp/playground_list.html' {playgrounds: playgrounds})


def suggestPlayground(request):
	#if request.method == 'GET':
		#form=addPlaygroundForm()
	#else:
		#form=addPlaygroundForm(request.POST)
		#submitDate = datetime.utcnow
		#if form.is_valid():
			#Name=form.cleaned_data['Name']
			#Street=form.cleaned_data['Street']
			#Zipcode=form.cleaned_data['Zipcode']
			#Handicap=form.cleaned_data['Handicap']
			#isCertifield=form.cleaned_data['isCertifield']
			#Image=form.cleaned_data['Image']
			#GeoCoordinateLat=form.cleaned_data['GeoCoordinateLat']
			#GeoCoordinateLon=form.cleaned_data['GeoCoordinateLon']
			#Playground=Playground.objects.create(Name=Name, Street=Street, Zipcode=Zipcode, Handicap=Handicap, isCertifield=isCertifield, Image=Image, GeoCoordinateLat=GeoCoordinateLat, GeoCoordinateLon=GeoCoordinateLon, Date=submitDate)
			#return HttepResponseRedirect (reverse('Playground_list'))

	#return render (request, 'playgroundApp/new_playground.html', { 'form': form, })
	return render (request, 'It lets user suggests a playground')
def useProfile (request):
	
	#User=get_object_or_404 (Playground)
        #return render (request, 'playgroundApp/user_info.html', {"User": User})
	return (request, 'It shows user information')
def userLogin (request):
	return (request, 'It is the user login view')

def userSignUp(request):
	return  render (request, 'It is the user sign up view')


