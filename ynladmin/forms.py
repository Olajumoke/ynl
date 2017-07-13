from ynladmin.models import CostSetting
from django import forms

class CostSettingForm(forms.ModelForm):
    amount   = forms.IntegerField(help_text="Amount", required = True, widget=forms.NumberInput(attrs={'class':'form-control','required':'required', 'placeholder':'Amount(%)','max':'50'}))
       
    class Meta:
        model = CostSetting
        fields = ('amount',)