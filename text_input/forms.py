from django import forms
from .models import *

class MaterialInput(forms.Form):
    text = forms.CharField(
        label="Enter the article that you want to study.",
        widget=forms.Textarea,
        error_messages={"required": "Please enter the article."},
    )

    def __init__(self, *args, **kwargs):
        super(MaterialInput, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['rows'] = 19
        self.fields['text'].widget.attrs['columns'] = 15
