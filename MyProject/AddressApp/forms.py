from django import forms
from .models import PermanentAddress,CurrentAddress

class PermanentAddressForm(forms.ModelForm):
    class Meta :
        model = PermanentAddress
        fields = '__all__'

        # labels
        labels = {
            'flat_no': 'Flat No',
            'street_name': 'Street Name',
            'city': 'City',
            'pincode': 'Pincode',
            'area': 'Area',
            'landmark': 'Landmark',
            'district': 'District',
            'state': 'State',
            'country': 'Country'
        }

        # placeholder
        widgets = {'flat_no': forms.TextInput(attrs={'placeholder': 'Enter your flat number'}),
                   'street_name': forms.TextInput(attrs={'placeholder': 'Enter street name'}),
                   'city': forms.TextInput(attrs={'placeholder': 'Enter city name'}),
                   'pincode': forms.NumberInput(attrs={'placeholder': 'Enter your pincode'}),
                   'area': forms.TextInput(attrs={'placeholder': 'Enter your area'}),
                   'landmark': forms.TextInput(attrs={'placeholder': 'Enter your landmark'}),
                   'district': forms.TextInput(attrs={'placeholder': 'Enter your district'}),
                   'state': forms.TextInput(attrs={'placeholder': 'Enter your state'}),
                   'country': forms.TextInput(attrs={'placeholder': 'Enter your country'}),
                   'customer':forms.TextInput(attrs={'readonly':'readonly'})
                   }



class CurrentAddressForm(forms.ModelForm):
    class Meta:
        model = CurrentAddress
        fields = '__all__'

        # labels
        labels = {
            'flat_no_1': 'Flat No',
            'street_name_1': 'Street Name',
            'city_1': 'City',
            'pincode_1':'Pincode',
            'area_1': 'Area',
            'landmark_1':'Landmark',
            'district_1':'District',
            'state_1':'State',
            'country_1':'Country'
        }

        # placeholder
        widgets = {'flat_no_1': forms.TextInput(attrs={'placeholder': 'Enter your flat number'}),
                   'street_name_1': forms.TextInput(attrs={'placeholder': 'Enter street name'}),
                   'city_1': forms.TextInput(attrs={'placeholder': 'Enter city name'}),
                   'pincode_1': forms.NumberInput(attrs={'placeholder': 'Enter your pincode'}),
                   'area_1': forms.TextInput(attrs={'placeholder': 'Enter your area'}),
                   'landmark_1': forms.TextInput(attrs={'placeholder': 'Enter your landmark'}),
                   'district_1': forms.TextInput(attrs={'placeholder': 'Enter your district'}),
                   'state_1':forms.TextInput(attrs={'placeholder': 'Enter your state'}),
                   'country_1':forms.TextInput(attrs={'placeholder': 'Enter your country'}),
                   }