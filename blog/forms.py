from django import forms
from material import Layout, Row

from . import models

class PostForm(forms.ModelForm):
    layout = Layout(
        Row('title'),
        Row('text')
    )

    class Meta:
        model = models.Post
        fields = ('title', 'text')