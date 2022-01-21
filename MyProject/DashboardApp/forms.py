from django import forms
from .models import *


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'full_name' : forms.TextInput(attrs={'placeholder':'Enter Full Name'}),
            'guardian_name' : forms.TextInput(attrs={'placeholder':'Enter Guardian Name'}),
            'mobile' : forms.TextInput(attrs={'placeholder':'Enter Mobile Number'}),
            'email' : forms.TextInput(attrs={'placeholder':'Enter Email Id'}),
            'pan_no' : forms.TextInput(attrs={'placeholder':'Enter Pancard Number'}),
            'aadhar_card' : forms.TextInput(attrs={'placeholder':'Enter Aadhar Card Number'}),
            'dob' : forms.TextInput(attrs={'placeholder':'Enter Date Of Birth'}),
        }

    def clean_pan_no(self):
        pan_no = self.cleaned_data['pan_no']
        if len(pan_no)!=10:
            raise forms.ValidationError("length should be Ten")
        else:
            return pan_no

    def clean_aadhar_card(self):
        aadhar_card = self.cleaned_data['aadhar_card']
        if len(str(aadhar_card))!= 12:
            raise forms.ValidationError('Length should be Twelve digit')
        else:
            return aadhar_card


