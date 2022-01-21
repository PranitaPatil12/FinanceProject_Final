from django import forms
from .models import Documents

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = '__all__'

        lables = {
            'pan_card': 'Pan Card',
            'aadhar_card': 'Aaadhar Card',
            'bank_statment': 'Bank Statement',
            'photo': 'Photo',
            'signature': 'Signature',
            'salary_slip': 'Salary Slip',
            'from16': 'Form16',
            'blance_sheet': 'Balance Sheet',
            'itr': 'Itr',
            'business_proof': 'Business Proof',

        }

        widgets = {
            'customer':forms.TextInput(attrs={'readonly':'readonly'})
        }
