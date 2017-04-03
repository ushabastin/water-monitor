from django import forms

from .models import Nodename

class NodenameForm(forms.ModelForm):

    class Meta:
        model = Nodename
        fields = ('title', 'text',)
