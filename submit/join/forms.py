from django import forms

class SubmitForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id' : 'fname', 'placeholder' : 'Your name' }))
    last = forms.CharField(widget=forms.Textarea(attrs={'id' : 'lname', 'placeholder' : 'Your last name' }))