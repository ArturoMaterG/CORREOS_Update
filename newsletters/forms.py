from django import forms
from .models import Newsletter, NewslettersUser

class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model= NewslettersUser
        fields=['email']
    
class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model=Newsletter

        fields=['name','subject','body','email','status']
    