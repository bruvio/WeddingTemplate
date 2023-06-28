from django import forms
from django.utils.safestring import mark_safe
from .models import RSVP,Comments, Hotels, Excurisons
from django.forms import ModelForm

class RSVP_FORM(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['name','phone','attend']
        
class Comments_Forms(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','question','Answer']

class Hotels_Forms(forms.ModelForm):
    class Meta:
        model = Hotels
        fields = ['H_name','H_Desc','H_Price', 'H_link']

class Excursions_Forms(forms.ModelForm):
    class Meta:
        model = Excurisons
        fields = ['E_name','E_Desc','E_Price', 'E_link']



