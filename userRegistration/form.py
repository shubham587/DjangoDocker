from django import forms
from .models import UserReg

class UserForm(forms.ModelForm):
    class Meta:
        model = UserReg
        fields = ["name", "email", "password"]
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'id' : 'nameId'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'id' : 'emailId'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'id' : 'passwordId', "autocomplete" : "on"}),
        }