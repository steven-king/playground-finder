from django import forms


class login (forms.Form):
	name=forms.CharField(max_length=50)
