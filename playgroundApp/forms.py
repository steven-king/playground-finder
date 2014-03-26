from django import forms
from plagyroundAPP import models as m

class addPlaygroundByUser(forms.Form):
	
            Name: forms.TextField(max_length=256)
            Street: forms.TextField(max_length=256)
            Zipcode: forms.IntegerField(max_length=10)
            Handicap: forms.BooleanField();
            Hours: forms.TextField(max_length=20)
            isCertified: forms.BooleanField();
            Image:forms.TextField();
            GeoCoordinateLat: forms.IntegerField();
            GeoCordinateLon: forms.IntergerField();

class addPlaygroundForm(forms.ModelForm):
	class Meta:
		model = m.Playground
