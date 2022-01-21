from .models import Guarantor
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class GuarantorModelForm(forms.ModelForm):
    class Meta:
        model = Guarantor
        fields = "__all__"
        labels = {
            'guarantor_name': 'Guarantor Name',
            'relation_with_cust': 'Relation with Customer',
            'profession': 'Profession',
            'contact_no': 'Mobile number ',
            'aadhar_no': 'Aadhar number',
            'pan_no': 'PAN number',
            'house_no': 'House number',
            'landmark': 'Landmark',
            'area': 'Area',
            'city': 'City',
            'pincode': 'Pincode',
            'country': 'Country',
        }
        widgets = {
            'contact_no': forms.TextInput(attrs={'placeholder': '10 digit mobile'}),
            'pan_no': forms.TextInput(attrs={'placeholder': '10 digit PAN number'}),
            'aadhar_no': forms.TextInput(attrs={'placeholder': '12 digit aadhar number'}),
            'customer': forms.TextInput(attrs={'readonly': 'readonly'})
        }

    def clean_pan_no(self):
        pan_no = self.cleaned_data['pan_no']
        print(type(pan_no))
        if len(pan_no) != 10 and not pan_no.isupper():
            raise forms.ValidationError("Invalid PAN Number!!")
        else:
            return pan_no

    def clean_pincode(self):
        pincode = self.cleaned_data['pincode']

        if len(str(pincode)) != 6:
            raise forms.ValidationError("Pincode invalid!!")
        else:
            return pincode

