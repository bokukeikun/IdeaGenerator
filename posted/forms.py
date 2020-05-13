from django import forms
from .models import Post

class IdeaGenerateForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('tag',)
        fields = ('category', 'tags', 'title', 'content')


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class': 'special'})




