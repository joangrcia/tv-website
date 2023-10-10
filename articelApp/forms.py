from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'w-full mt-2 border-gray-50 rounded placeholder:text-sm placeholder:text-gray-400 dark:bg-zinc-700/50 dark:border-zinc-600', 'placeholder': 'Your message...', 'id':'commentmessage-input', 'rows':'3'}),
        }
        labels = {
            'text': False,  # Menyembunyikan label field 'text'
        }
