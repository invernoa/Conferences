from django import forms
from .models import Comment
from .models import Conference


class ConfForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ('title', 'place', 'period', 'tracks', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('choice_field', 'text',)
