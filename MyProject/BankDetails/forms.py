from django import forms
from .models import *

class BankDetailsModelForm(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = '__all__'

        labels={
            'account_holder_name':'Account Holder Name',
            'account_no':'Account Number',
            'bank_name':'Bank Name',
            'branch_name':'Branch Name',
            'account_type':'Account Type',
            'ifsc_code':'IFSC Code',
            'micr_code':'MICR Code'
        }

        widgets = {
            'account_holder_name': forms.TextInput(attrs={'placeholder': 'Enter Account Holder Name'}),
            'account_no': forms.TextInput(attrs={'placeholder': 'Enter Account Number'}),
            'bank_name': forms.TextInput(attrs={'placeholder': 'Enter Bank Name'}),
            'branch_name': forms.TextInput(attrs={'placeholder': 'Enter branch_name'}),

            'ifsc_code': forms.TextInput(attrs={'placeholder': 'Enter 11-digit IFSC Code'}),
            'micr_code': forms.TextInput(attrs={'placeholder': 'Enter 9-digit MICR Code'}),
            'customer': forms.TextInput(attrs={'readonly':'readonly'})

        }

    def clean_ifsc_code(self):
        ifsc_code = self.cleaned_data['ifsc_code']
        if not len(ifsc_code) == 11 or not ifsc_code.isalnum():
            raise forms.ValidationError("IFSC code must be Valid")
        else:
            return ifsc_code

    def clean_micr_code(self):
        micr_code = self.cleaned_data['micr_code']

        if not len(micr_code) == 9:
            raise forms.ValidationError("MICR code must be Valid")
        else:
            return micr_code

    def clean_account_no(self):
        account_no = self.cleaned_data['account_no']
        print(type(account_no))
        if not len(str(account_no)) == 10:
            raise forms.ValidationError("Account No must be Valid")
        else:
            return account_no




