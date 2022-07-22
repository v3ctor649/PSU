from django import forms

class RegisterForm(forms.Form):
    surname = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Фамилия"}))
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Имя"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Адрес электронной почты"}))