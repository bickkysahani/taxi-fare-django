from django import forms
from datetime import datetime

from .models import Journey

class JourneyForm(forms.ModelForm):
    time = forms.TimeField(label='Hour',required=True,
                              widget=forms.TimeInput(format='%H:%M',attrs={'class':'form-control'}),
                              initial=datetime.now().strftime('%H:%M'))
    distance = forms.FloatField(label='Distance (km)',
                                 required=True,
                                 min_value=0,
                                 initial=0,widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Journey
        fields = ['distance','time']

    # def __init__(self):
    #     super().__init__(self)
    #     self.fields['distance'].widget.attrs.update({'class':'form-control'})
    #     self.fields['time'].widget.attrs.update({'class':'form-control'})