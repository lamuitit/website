from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=200)

class CCCDForm(forms.Form):
    cccd=forms.CharField(max_length=12)
"""
class CreateBioLower14(forms.Form):
    name = forms.CharField(max_length=200)
    birth = forms.DateTimeField()
    gender = forms.CharField(max_length=200, label='gender')
    phonenumber = forms.CharField(max_length=12, label='phone number')
    location = forms.CharField(max_length=300, label='location')
    cccd = forms.CharField(max_length=200)

class CreateBioUpper14(forms.Form):
    name = forms.CharField(max_length=200, label='name')
    birth = forms.DateTimeField()
    gender = forms.CharField(max_length=200, label='gender')
    phonenumber = forms.CharField(max_length=12, label='phone number')
    location = forms.CharField(max_length=300, label='location')
    cccd = forms.CharField(max_length=200)
"""