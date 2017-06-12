from django import forms
from django.contrib.auth.models import User
from general.models import UserAccount
from general.modelchoices import BANK, GENDER
from django.contrib.admin.widgets import AdminDateWidget 





class UserForm(forms.ModelForm):
    first_name      = forms.CharField(help_text="First Name", required = True,widget=forms.TextInput(attrs={'placeholder':'First Name', 'required':'required', 'class':'form-control'}))
    last_name       = forms.CharField(help_text="Last Name", required = True,widget=forms.TextInput(attrs={'placeholder':'Last Name', 'required':'required', 'class':'form-control'}))
    username        = forms.CharField(help_text="Username", required = True,widget=forms.TextInput(attrs={'placeholder':'Username', 'required':'required', 'class':'form-control'}))
    email           = forms.EmailField(help_text="E-Mail", required = True, widget=forms.EmailInput(attrs={'placeholder':'Email Address', 'required':'required','class':'form-control'}))
    password        = forms.CharField(help_text="Password", required = True,  widget=forms.PasswordInput(attrs={'placeholder':'Password','required':'required', 'class':'form-control'}))
   
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
 


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
    phone_number    = forms.IntegerField(help_text="Phone Number", required = True,widget=forms.NumberInput(attrs={'placeholder':'Phone Number', 'required':'required', 'class':'form-control'}))
    dob             = forms.DateField(help_text="Date of Birth", required = True,widget=forms.DateInput(attrs={'placeholder':'Date of birth', 'required':'required', 'class':'form-control', 'type': 'date'}))
    bank            = forms.ChoiceField(help_text="Bank", choices=BANK, required = True, widget=forms.Select(attrs={'placeholder':'Bank', 'required':'required','class':'form-control'}))
    account_number  = forms.IntegerField(help_text="Account Number", required = True,widget=forms.NumberInput(attrs={'placeholder':'Account Number', 'required':'required', 'class':'form-control'}))
    user_image      = forms.ImageField(help_text="User Image", required = True,widget=forms.ClearableFileInput(attrs={'required':'required', 'class':'dropify'}))
    class Meta:
        model = UserAccount
        fields = ('bank', 'dob', 'account_number', 'gender', 'phone_number', 'user_image')
        
    def validate_bank_account_no(value):
        len_value = len(value)
        if (len_value < 10 or len_value > 10) and value.isdigit():
            raise ValidationError('Please provide NUBAN 10 digits Bank Account Number. (It currently has %s)' %len_value)