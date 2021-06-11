from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title of your post'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a unique identificator for your post'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list ,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter yout post body'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title of your post'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a unique identificator for your post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter yout post body'}),
        }