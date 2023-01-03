from django import forms
from django.contrib.auth import forms as authforms
from blogapp.models import ArticleModel


class LoginForm(authforms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
               
    username = authforms.UsernameField(label='' , widget=forms.TextInput(
        attrs={"autofocus": True,
               'placeholder': "Username",
                }))
    
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={
                                'placeholder': 'Password',
                                   }))

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['article_name', 'article_text']
        widgets = {
            'article_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin: auto',
                'placeholder': 'Article name'
            }),
            'article_text': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin: auto',
                'placeholder': 'Write your text here'
            })
        }
        
        labels = {
            'article_name': '',
            'article_text': ''  
        }
        
        
        
        