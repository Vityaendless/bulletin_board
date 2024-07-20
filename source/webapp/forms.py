from django import forms

from .models import Ad


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('photo', 'title', 'description', 'category', 'price')
        error_messages = {
            'title': {
                'required': 'Please enter field'
            }
        }
