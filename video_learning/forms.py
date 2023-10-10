# video_learning/forms.py

from django import forms
from .models import PaymentTransaction

class PaymentTransactionForm(forms.ModelForm):
    class Meta:
        model = PaymentTransaction
        fields = ['proof_of_payment']
