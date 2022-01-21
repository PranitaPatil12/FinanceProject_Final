from django import forms
from .models import LoanDetails, Enquiry

class DateInput(forms.DateInput):
    input_type = 'date'


class LoanDetailsForm(forms.ModelForm):
    class Meta:
        model = LoanDetails
        exclude = ['cibil_score','is_eligible']

        labels = {
            'dob':'Date Of Birth',
            'required_loan':'Required Loan Amount'
        }

        widgets = {
            'full_name':forms.TextInput(attrs={'placeholder':'Enetr your full name'}),
            'mobile':forms.TextInput(attrs={'placeholder':'e.g +918529637451'}),
            'email':forms.TextInput(attrs={'placeholder':'Enetr your email'}),
            'pan_number':forms.TextInput(attrs={'placeholder':'Enter your Pan Number'}),
            'required_loan':forms.TextInput(attrs={'placeholder':'Enter Required loan amount'}),
            'dob':DateInput(attrs={'placeholder':'Enter Birth Date'})
        }


    def clean_full_name(self):
        fullname = self.cleaned_data['full_name']
        return fullname.title()


    def clean_pan_number(self):
        pan = self.cleaned_data['pan_number']
        if len(pan) == 10 and pan.isupper():
            return pan
        raise forms.ValidationError("Invalid Pan Number")


    def clean_required_loan(self):
        required_amount = self.cleaned_data['required_loan']
        if required_amount < 50000 or required_amount > 1500000:
            raise forms.ValidationError("In valid amount(must be between 50K to 15 Lac)")
        return required_amount


class EnquiryModelForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'


        widgets = {'class': 'form-control',
                   'mobile': forms.TextInput(attrs={'placeholder': 'for ex: +919856481575'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Enter email ex: abc@gmail.com'}),
                   'city': forms.TextInput(attrs={'placeholder': 'Enter city name'})
                   }

    def clean_full_name(self):
        return self.cleaned_data['full_name'].capitalize()