
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm


from .models import *
SEXE=(('Famme','famme'),('Homme','homme'),)
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=forms.EmailInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
class EnseignantForm(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control'

        }
    ))
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'

        }
    ))

    numero_telephone=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    sexe=forms.ChoiceField(choices=SEXE,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ))
    adr=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    code_postal=forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control'

        }
    ))



class SupprimerEnseignantForm(forms.Form):

    enseignant1=forms.ModelChoiceField(Enseignant.objects,widget=forms.Select(
        attrs={
            'class':'form-control',
            'name':'en1',
            'id':'en1',
        }
    ))


class ModifierEnseignantForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)
    sexe = forms.ChoiceField(choices=SEXE,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ),required=False)

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)


    numero_telephone=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)
    adr=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)
    code_postale=forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)


class groupeForm(forms.Form):

    designation=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))

    nb_enfant_max=forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control'

        }
    ))
    niveau=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))



class supprimerGroupeForm(forms.Form):
    groupe=forms.ModelChoiceField(Groupe.objects,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ))

class ModifierGroupeForm(forms.Form):
    groupe1 = forms.ModelChoiceField(Groupe.objects, widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ))

    designation1=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)

    nb_enfant_max1=forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)
    niveau1=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)


class ModuleForm(forms.ModelForm):
    designation=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    class Meta:
        model=Module
        fields={'designation',}

class SupprimerModuleForm(forms.Form):
    module=forms.ModelChoiceField(Module.objects,widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))


class AffectationForm(forms.ModelForm):
    groupe=forms.ModelChoiceField(Groupe.objects,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ))
    module=forms.ModelChoiceField(Module.objects,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ))
    enseignant=forms.ModelChoiceField(Enseignant.objects,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ))
    class Meta:
        model=Enseignament
        fields={'module','enseignant','groupe',}


class EnfantFrom(forms.Form):
    parent=forms.ModelChoiceField(Parent.objects,widget=forms.Select(
        attrs={
            'class': 'form-control',


        }
    ),required=False)
    nom=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    prenom=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    sexe =forms.ChoiceField(choices=SEXE,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ))

    groupe=forms.ModelChoiceField(Groupe.objects,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ))
    date_N=forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'type':'date',

        }
    ))
class ModifierEnfantFrom(forms.Form):
    parent=forms.ModelChoiceField(Parent.objects,widget=forms.Select(
        attrs={
            'class': 'form-control',


        }
    ),required=False)
    nom=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)
    prenom=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ),required=False)
    sexe =forms.ChoiceField(choices=SEXE,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ),required=False)

    groupe=forms.ModelChoiceField(Groupe.objects,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ),required=False)
    date_N=forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'type':'date',

        }
    ),required=False)


class ParentForm(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    email=forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control'

        }
    ))
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'

        }
    ))

    numero_telephone=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    sexe=forms.ChoiceField(choices=SEXE,widget=forms.Select(
        attrs={
            'class': 'form-control'

        }
    ))
    adr=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    adr_tr=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))



class ArticleForm(forms.Form):
    titre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'

        }
    ))
    discription =forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control'

        }
    ))
    pic =forms.ImageField()


class PasswordChangeCustomForm(PasswordChangeForm):
        error_css_class = 'has-error'
        error_messages = {'password_incorrect':
                  "Το παλιό συνθηματικό δεν είναι σωστό. Προσπαθείστε   ξανά."}
        old_password = forms.CharField(required=True, label='Συνθηματικό',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'Το συνθηματικό δε μπορεί να είναι κενό'})

        new_password1 = forms.CharField(required=True, label='Συνθηματικό',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'Το συνθηματικό δε μπορεί να είναι κενό'})
        new_password2 = forms.CharField(required=True, label='Συνθηματικό (Επαναλάβατε)',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'Το συνθηματικό δε μπορεί να είναι κενό'})


