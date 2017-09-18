from django import forms
from django.contrib.auth.models import User
from general.models import UserAccount, Event
from general.modelchoices import *
# from tinymce.models import HTMLField
from general.models import UserAccount, MessageCenterComment, Replies
from general.modelchoices import BANK, GENDER



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


    title               = forms.CharField(help_text="Title", required = True, widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))
    category            = forms.ChoiceField(choices = CATEGORY, error_messages = {'required': 'Please select a category.'},widget=forms.Select(attrs={'class':'form-control','required':'required'}))
    start_date          = forms.DateField(required=True, widget=forms.DateInput(attrs={'class':'form-control id_date','required':'required'}))
    end_date            = forms.DateField(required=True, widget=forms.DateInput(attrs={'class':'form-control id_date','required':'required'}))
    start_time          = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'class':'form-control id_time','required':'required'}))
    end_time            = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'class':'form-control id_time','required':'required'}))
    publish             = forms.BooleanField(required = False)
    event_image         = forms.ImageField(required=False, help_text='Photo', widget=forms.widgets.ClearableFileInput())
    event_msg_body      = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control'}))
    bet_question        = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','required':'required'}))


    class Meta:
        model = Event
        fields = ('title', 'category', 'start_date', 'end_date', 'start_time', 'end_time','publish', 'event_image','event_msg_body','bet_question','event_decision','event_id')

	

class UserProfileForm(forms.ModelForm):
    first_name      = forms.CharField(help_text="First Name", required = True,widget=forms.TextInput(attrs={'placeholder':'First Name', 'required':'required', 'class':'form-control'}))
    last_name       = forms.CharField(help_text="Last Name", required = True,widget=forms.TextInput(attrs={'placeholder':'Last Name', 'required':'required', 'class':'form-control'}))
    username        = forms.CharField(help_text="Username", required = True,widget=forms.TextInput(attrs={'placeholder':'Username', 'required':'required', 'class':'form-control', 'readonly':'readonly'}))
    email           = forms.EmailField(help_text="E-Mail", required = True, widget=forms.EmailInput(attrs={'placeholder':'Email Address', 'required':'required','class':'form-control'}))
    #password        = forms.CharField(help_text="Password", required = True,  widget=forms.PasswordInput(attrs={'placeholder':'Password','required':'required', 'class':'form-control'}))
   
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        
        

class UserAccountForm(forms.ModelForm):
    gender          = forms.ChoiceField(help_text="gender", choices=GENDER, required = True,widget=forms.Select(attrs={'required':'required', 'class':'form-control'}))
    phone_number    = forms.CharField(help_text="Phone Number", required = True,widget=forms.TextInput(attrs={'placeholder':'Phone Number', 'required':'required', 'class':'form-control'}))
    dob             = forms.DateField(help_text="Date of Birth", required = True,widget=forms.DateInput(attrs={'placeholder':'Date of birth', 'required':'required', 'class':'form-control', 'type': 'date'}))
    bank            = forms.ChoiceField(help_text="Bank", choices=BANK, required = True, widget=forms.Select(attrs={'placeholder':'Bank', 'required':'required','class':'form-control'}))
    account_number  = forms.CharField(help_text="Account Number", required = True,widget=forms.TextInput(attrs={'placeholder':'Account Number', 'required':'required', 'class':'form-control'}))
    user_image      = forms.ImageField(help_text="User Image", required = False, widget=forms.ClearableFileInput(attrs={'class':'dropify'}))
    #referred_by     = forms.CharField(help_text="Referred By", required = False,widget=forms.TextInput(attrs={'placeholder':"Referral's Phone Number", 'class':'form-control'}))

    
    class Meta:
        model = UserAccount
        fields = ('bank', 'dob', 'account_number', 'gender', 'phone_number', 'user_image')
        
    def validate_bank_account_no(value):
        len_value = len(value)
        if (len_value < 10 or len_value > 10) and value.isdigit():
            raise ValidationError('Please provide NUBAN 10 digits Bank Account Number. (It currently has %s)' %len_value)



class MessageCenterCommentForm(forms.ModelForm):
    message        = forms.CharField(max_length = 128, help_text = "", widget=forms.Textarea(attrs={'required':'true','class':'form-control'}))
    image_obj      = forms.ImageField(required = False, help_text='Photo', widget=forms.widgets.ClearableFileInput())

    class Meta:
        model = MessageCenterComment
        fields = ('message', 'image_obj',)



class RepliesForm(forms.ModelForm):
    reply          = forms.CharField(max_length = 128, help_text = "", widget=forms.Textarea(attrs={'required':'true','class':'form-control'}))
    name           = forms.CharField(help_text="Name", required = True,widget=forms.TextInput(attrs={'placeholder':'Mame', 'required':'required', 'class':'form-control', 'readonly':'readonly'}))
    email          = forms.EmailField(help_text="E-Mail", required = True, widget=forms.EmailInput(attrs={'placeholder':'E-mail', 'required':'required','class':'form-control'}))
   
    class Meta:
        model = Replies
        fields = ('reply', 'name', 'email')









