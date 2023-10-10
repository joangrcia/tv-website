from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    user_bio = forms.CharField(max_length=100)  # Tambahkan field user_bio
    profile_image = forms.ImageField(label='Profile Picture', required=False)
    delete_profile_image = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'ml-2'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'user_bio', 'profile_image', 'delete_profile_image')
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'w-full rounded border border-stroke bg-gray py-3 px-4.5 font-medium text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary'})
        self.fields['first_name'].widget.attrs.update({'class': 'w-full rounded border border-stroke bg-gray py-3 pl-11.5 pr-4.5 font-medium text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary'})
        self.fields['last_name'].widget.attrs.update({'class': 'w-full rounded border border-stroke bg-gray py-3 px-4.5 font-medium text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary'})
        self.fields['email'].widget.attrs.update({'class': 'w-full rounded border border-stroke bg-gray py-3 pl-11.5 pr-4.5 font-medium text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary'})
        self.fields['user_bio'].widget.attrs.update({'class': 'w-full rounded border border-stroke bg-gray py-3 pl-11.5 pr-4.5 font-medium text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary'})
        self.fields['profile_image'].widget.attrs.update({'class': 'fallback'})