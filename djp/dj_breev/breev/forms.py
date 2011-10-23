import re
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form) :
  username = forms.EmailField(label=u'Gebruikersnaam (email)', max_length=75)
#  email = forms.EmailField(label=u'Email')
  password1 = forms.CharField(
     label=u'Wachtwoord',
     widget=forms.PasswordInput()
     )  
  password2 = forms.CharField(
     label=u'Wachtwoord (opnieuw)',
     widget=forms.PasswordInput()
     )
     
  def clean_password2(self) :
    if 'password1' in self.cleaned_data :
      password1 = self.cleaned_data['password1']      
      password2 = self.cleaned_data['password2']
      if password1 == password2 :
        return password2
    raise forms.ValidationError('Wachtwoorden zijn niet gelijk')

  def clean_username(self) :
    username = self.cleaned_data['username']
# TODO check op email validiteit
#    if not re.search(r'^\w+$', username) :
#      raise forms.ValidationError('''Gebruikersnaam kan alleem
#                                     alfanumerieke karakters bevatten.''')
    try :
      User.objects.get(username=username)
    except User.DoesNotExist :
      return username
    raise forms.ValidationError('Gebruikersnaam is al in gebruik.')     
    
  def clean_email(self) :
    email = self.cleaned_data['email']
    try :
      User.objects.get(email=email)
    except User.DoesNotExist :
      return email
    raise forms.ValidationError('Email is al in gebruik.')     

class GebruikerCategorieSaveForm(forms.Form) :
  categorie = forms.CharField(
    label = u'Categorie',
    widget=forms.TextInput(attrs={'readonly':'readonly'})
  ) 
  volgorde = forms.IntegerField(
    label = u'Volgorde',
    required = False,
  )
  aantal_artikelen = forms.IntegerField(
    label = u'Aantal Artikelen',
    required = False,
  )
  
class SearchForm(forms.Form) :
  query = forms.CharField(
  label=u'Vul een zoekterm om op te zoeken',
  widget=forms.TextInput(attrs={'size':32})
    )
