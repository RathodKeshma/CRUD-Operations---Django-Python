from django import forms
from .models import BlogUser

class BlogUserForm(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = '__all__'