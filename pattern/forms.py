from .models import Pattern
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Pattern, Comment

class PatternForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = ['pattern_name', 'description', 'featured_image', 'difficulity_level', 'needle_size', 'yarn', 'gauge']
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()  
        self.helper.form_method = 'post' 
        self.helper.add_input(Submit('submit', 'Save'))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)