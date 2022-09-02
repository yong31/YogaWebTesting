from django import forms
from django.contrib.auth.models import User
from YogaWebsite.models import Member

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=191,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=191,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=191,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
 

    class Meta:
        model = User
        fields = ["first_name","last_name","username","email"]

GENDER = (
        ('1','Male'),
        ('2','Female'),
    )

AGE = (
        ('0','below 19'),
        ('1','19 to 23'),
        ('2','24 to 40'),
        ('3','above 40'),
    )

ORIENTATION = (
        ('1','Heterosexual'),
        ('2','Bisexual'),
        ('3','Homosexual'),
        ('4','Asexual'),
        ('5','Other'),
    )

class UpdateMemberForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER,required=True)
    age = forms.ChoiceField(choices=AGE,required=True)
    orientation = forms.ChoiceField(choices=ORIENTATION,required=True)

    class Meta:
        model = Member
        fields = ["gender","age","orientation"]

class ContactForm(forms.Form):
    from_name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)