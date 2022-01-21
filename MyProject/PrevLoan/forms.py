from django import forms
from .models import PrevLoan


class PrevLoanForm(forms.ModelForm):
    class Meta:
        model = PrevLoan
        fields = "__all__"
        labels = {'bank_name': 'Bank Name', 'branch_name': 'Branch Name', 'account_no': 'Account Number',
                  'ifsc_code': 'IFSC Code', 'micr_code': 'MICR Code', 'loan_amount': 'Loan Amount',
                  'loan_type': 'Loan Type', 'loan_tenure': 'Loan Tenure', 'amount_paid': 'Amount Paid'
                  }
        widgets = {
            'bank_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Bank Name'
                }
            ),
            'branch_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Branch Name'
                }
            ),
            'account_no': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Account Number'
                }),
            'ifsc_code': forms.TextInput(
                attrs={
                    'placeholder': 'Enter IFSC Code'
                }),
            'micr_code': forms.TextInput(
                attrs={
                    'placeholder': 'Enter MICR Code'
                }),
            'loan_amount': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Loan Amount'
                }),

            'amount_paid': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Amount Paid'
                }),

            'loan_tenure': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Loan Tenure'
                }),
            'customer': forms.TextInput(attrs={'readonly': 'readonly'})
        }

    def clean_ifsc_code(self):
        ifsc_code = self.cleaned_data['ifsc_code']
        if len(ifsc_code) < 11:
            raise forms.ValidationError('IFSC CODE must be of 11')
        else:
            return ifsc_code

    def clean_micr_code(self):
        micr_code = self.cleaned_data['micr_code']
        if len(micr_code) < 9:
            raise forms.ValidationError('MICR CODE must be of 9')
        else:
            return micr_code

    #    def clean_account_no(self):
    #        account_no = self.cleaned_data['account_no']
    #        if account_no != 10:
    #            raise forms.ValidationError('Account number must be of 10 digits')
    #        else:
    #           return account_no

    def clean_loan_amount(self):
        loan_amount = self.cleaned_data['loan_amount']
        if loan_amount > 1000000:
            raise forms.ValidationError('loan amount should be in between 50000-1000000')
        else:
            return loan_amount
