from django import forms

class BikeDetailForm(forms.Form):
    company = forms.CharField()
    name = forms.CharField()
    price = forms.CharField()
    range = forms.CharField()
    speed = forms.CharField()
    weight = forms.CharField()
    height = forms.CharField()
    power = forms.CharField()
    colors = forms.CharField()
    image = forms.CharField()
    warranty = forms.CharField()
    time = forms.CharField()
    max_power = forms.CharField()
    touches = forms.CharField()
    # Add more fields as needed
