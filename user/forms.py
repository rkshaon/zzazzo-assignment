from django import forms

from user.models import User


class NewUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter user first name',
    }), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter user first name',
    }), required=True)
    img = forms.FileField(widget=forms.ClearableFileInput(attrs={
    }), required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={
    }), required=False)

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'img', 'address'}