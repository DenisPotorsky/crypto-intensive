from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
