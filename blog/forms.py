from django import forms
from .models import Post, Izoh
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForma(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['sarlavha', 'matn']
        widgets = {
            'sarlavha': forms.TextInput(attrs={
                'class': 'forma-input',
                'placeholder': 'Post sarlavhasini kiriting...'
            }),
            'matn': forms.Textarea(attrs={
                'class': 'forma-textarea',
                'placeholder': 'Post matnini yozing...',
                'rows': 10
            }),
            'muallif': forms.TextInput(attrs={
                'class': 'forma-input',
                'placeholder': 'Muallif ismi...'
            }),
        }
        labels = {
            'sarlavha': '📝 Sarlavha',
            'matn': '✍️ Post Matni',
            'muallif': '👤 Muallif',
        }



class RoyxatdanOtishForma(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Foydalanuvchi nomi',
            'email': 'Email',
        }


class IzohForm(forms.ModelForm):
    class Meta:
        model = Izoh
        fields = ['matn']
        widgets = {
            'matn': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': "Izoh qoldiring..."
            })
        }