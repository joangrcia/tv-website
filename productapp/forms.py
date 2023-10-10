from django import forms

class PaymentForm(forms.Form):
    account_number = forms.CharField(max_length=100)
    proof_of_payment = forms.FileField()
    mt_name = forms.CharField(max_length=100)
