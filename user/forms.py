from django import forms
from .models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'bio', 'difficulity_level', 'profile_picture']