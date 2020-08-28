from django import forms
from bug_tracker_app import models




class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Write the username. . .'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={
            'class':'form-control',
            'placeholder':'Enter the password. . .'
        }
  
    ))



class AddTicketForm(forms.Form):
    title = forms.CharField(max_length=30,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Write the title of ticket. . .'
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
           attrs={
            'class':'form-control',
            'placeholder':'add description. . .'
        }
    ))