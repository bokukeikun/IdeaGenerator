from django import forms
from .models import Post, Comment

class IdeaGenerateForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('category', 'tags', 'title', 'content')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class': 'special'})
            self.fields["tags"].required = True
            self.fields["category"].required = True

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': '公開コメントを入力',
    }))
    class Meta:
        model = Comment
        fields = [ 'content' ]


# class TagElementsCreateForm(forms.ModelForm):
#     class Meta:
#         model = Original
#         fields = ['tags', 'elements']