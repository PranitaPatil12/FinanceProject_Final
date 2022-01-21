from django import forms
from .models import SanctionedLoan


class RSanctionedLoanModelForm(forms.ModelForm):
    class Meta:
        fields = ['customer','required_loan']
        model = SanctionedLoan
        labels = {
            "required_loan": "Required Loan",
        }


class SanctionedLoanModelForm(forms.ModelForm):
    class Meta:
        fields = ['customer','required_loan', 'approved_loan', 'tenure', 'interest']
        model = SanctionedLoan
        labels = {
            "required_loan": "Required Loan",
            "approved_loan": "Approved Loan",
            "tenure": "Tenure(in months)",
            "interest": "Interest Rate(annual)",
            "emi": "EMI",
            "is_approved": "Approval",
        }

    def clean_approved_loan(self):
        approved_loan = self.cleaned_data['approved_loan']
        if approved_loan <= 50000:
            raise forms.ValidationError('Approved Loan should be Greater than 50000')
        elif approved_loan > 1500000:
            raise forms.ValidationError('Approved Loan should not be Greater than 15 Lacs')
        else:
            return approved_loan

    def clean_tenure(self):
        tenure = self.cleaned_data['tenure']
        if tenure <= 12:
            raise forms.ValidationError('Tenure should be Greater than 12 months')
        elif tenure > 60:
            raise forms.ValidationError('Tenure should not be Greater than 60 months')
        else:
            return tenure

    def clean_interest(self):
        interest = self.cleaned_data['interest']
        if interest <= 10.49:
            raise forms.ValidationError('interest should be Greater than 10.49%')
        elif interest > 24:
            raise forms.ValidationError('Interest should not be Greater than 24%')
        else:
            return interest
