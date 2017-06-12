from django import forms
from django.contrib.auth.models import User
from general.models import UserAccount, Event
from general.modelchoices import *
from tinymce.models import HTMLField



attrs3 = {'required': 'true'}


class DateInput(forms.DateInput):
    input_type = 'date'



class UserForm(forms.ModelForm):
	username        = forms.CharField(max_length = 128, help_text = "", widget=forms.TextInput(attrs={'required':'true', 'Placeholder':'Username'}))
	email           = forms.EmailField(max_length = 128, help_text = "", widget=forms.EmailInput(attrs={'required':'true', 'Placeholder':'E-mail'}))
	password 		= forms.CharField(widget=forms.PasswordInput())


	class Meta:
	    model = User
	    fields = ('username', 'email', 'password')


class EventForm(forms.ModelForm):

	title          = forms.CharField(help_text="Title", required = True, widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
	category 	   = forms.ChoiceField(choices = CATEGORY, error_messages = {'required': 'Please select a category.'},widget=forms.Select(attrs={'class':'form-control','required':'required'}))
	start_time     = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','required':'required'}))
	end_time       = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control','required':'required'}))
	publish        = forms.BooleanField(required = False)
	event_image    = forms.ImageField(help_text='Photo', widget=forms.widgets.ClearableFileInput({'required':'required'}))
	admin_text     = HTMLField()


	class Meta:
	    model = Event
	    fields = ('title', 'category', 'start_time', 'end_time', 'publish', 'event_image', 'admin_text',)


