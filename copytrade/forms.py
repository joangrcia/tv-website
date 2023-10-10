# forms.py
from django import forms
from .models import Metatraders

class MetatraderForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Menambahkan widget PasswordInput
    class Meta:
        model = Metatraders
        fields = ['login', 'password', 'ip_address', 'port']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'border border-gray-100 text-gray-900 text-sm rounded focus:ring-violet-100 focus:border-violet-500 block w-full p-2.5 dark:bg-zinc-700/50 dark:border-zinc-600 dark:placeholder:text-zinc-100/60 dark:text-zinc-100'})
        self.fields['password'].widget.attrs.update({'class': 'border border-gray-100 text-gray-900 text-sm rounded focus:ring-violet-100 focus:border-violet-500 block w-full p-2.5 dark:bg-zinc-700/50 dark:border-zinc-600 dark:placeholder:text-zinc-100/60 dark:text-zinc-100', 'type':'password'})
        self.fields['ip_address'].widget.attrs.update({'class': 'border border-gray-100 text-gray-900 text-sm rounded focus:ring-violet-100 focus:border-violet-500 block w-full p-2.5 dark:bg-zinc-700/50 dark:border-zinc-600 dark:placeholder:text-zinc-100/60 dark:text-zinc-100'})
        self.fields['port'].widget.attrs.update({'class': 'border border-gray-100 text-gray-900 text-sm rounded focus:ring-violet-100 focus:border-violet-500 block w-full p-2.5 dark:bg-zinc-700/50 dark:border-zinc-600 dark:placeholder:text-zinc-100/60 dark:text-zinc-100'})