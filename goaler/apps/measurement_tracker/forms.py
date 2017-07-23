from django import forms

from .models import Measurement


class MeasurementForm(forms.ModelForm):

    neck = forms.FloatField(required=False)
    chest = forms.FloatField(required=False)
    arm = forms.FloatField(required=False)
    waist = forms.FloatField(required=False)
    hip = forms.FloatField(required=False)
    thigh = forms.FloatField(required=False)

    class Meta:
        model = Measurement
        exclude = ['user', 'date']
