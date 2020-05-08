from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form_title_input'}),
        'text': forms.TextInput(attrs={'class': 'form_text_input'}),
        'image': forms.FileInput(attrs={'class': 'form_image_input'}),
        }
        help_texts = {
            'title': 'Введите название статьи',
        }