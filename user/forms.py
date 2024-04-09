from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['bio', 'difficulity_level', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()  
        self.helper.form_method = 'post' 
        self.helper.form_enctype = 'multipart/form-data'  # Enctype for file uploads
        self.helper.add_input(Submit('submit', 'Save'))
