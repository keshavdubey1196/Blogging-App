from django import forms
from froala_editor.widgets import FroalaEditor

from .models import Blog


class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Blog
        fields = (
            "title",
            "content",
        )
