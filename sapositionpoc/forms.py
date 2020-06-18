from django import forms
from .models import Sa

#lass SaForm(forms.ModelForm):

    #class Meta:
        #model = Sa
        #fields = ('sa_number', 'sa_position',)
class SaForm(forms.ModelForm):
    class Meta:
        model = Sa
        fields = [
            'sa_number',
            'sa_position'
        ]

class RawSaForm(forms.Form):
    sa_number = forms.CharField()
    sa_position = forms.CharField()
