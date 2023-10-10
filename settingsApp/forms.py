from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    # phone_number = forms.IntegerField()  # Tambahkan field phone_number
    user_bio = forms.CharField(max_length=100)  # Hapus initial value
    profile_image = forms.ImageField(label='Profile Picture', initial='default.jpg')
    delete_profile_image = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'ml-2'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'user_bio', 'profile_image')
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'border border-gray-100 text-gray-900 text-sm rounded focus:ring-violet-100 focus:border-violet-500 block w-full p-2.5 dark:bg-zinc-700/50 dark:border-zinc-600 dark:placeholder:text-zinc-100/60 dark:text-zinc-100'})
        self.fields['first_name'].widget.attrs.update({'class': 'border border-gray-100 text-gray-900 text-sm rounded focus:ring-violet-100 focus:border-violet-500 block w-full p-2.5 dark:bg-zinc-700/50 dark:border-zinc-600 dark:placeholder:text-zinc-100/60 dark:text-zinc-100'})
        self.fields['last_name'].widget.attrs.update({'class': 'border border-gray-100 text-gray-900 text-sm rounded focus:ring-violet-100 focus:border-violet-500 block w-full p-2.5 dark:bg-zinc-700/50 dark:border-zinc-600 dark:placeholder:text-zinc-100/60 dark:text-zinc-100'})
        self.fields['email'].widget.attrs.update({'class': 'border border-gray-100 text-gray-900 text-sm rounded focus:ring-violet-100 focus:border-violet-500 block w-full p-2.5 dark:bg-zinc-700/50 dark:border-zinc-600 dark:placeholder:text-zinc-100/60 dark:text-zinc-100'})
        self.fields['user_bio'].widget.attrs.update({'class': 'border border-gray-100 text-gray-900 text-sm rounded focus:ring-violet-100 focus:border-violet-500 block w-full p-2.5 dark:bg-zinc-700/50 dark:border-zinc-600 dark:placeholder:text-zinc-100/60 dark:text-zinc-100'})
        self.fields['profile_image'].widget.attrs.update({'class': 'fallback'})