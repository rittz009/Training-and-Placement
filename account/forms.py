from django import forms

from .models import *

############### Form for collaborating views and templates ###############

# LoginForm() "To collaborate get and post request" #

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Username',
    'id':'username',
    }))
    email = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Email',
    'id':'email',
    }))
    password = forms.CharField(max_length=30,
    widget = forms.PasswordInput())

#J obApplicationForm() "To collaborate get and post request" #

class JobApplicationForm(forms.Form):
    resume = forms.FileField(
        label='resume',
    )
    company = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Company',
    'id':'company',
    }))
    position = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Position',
    'id':'position',
    }))
    reason_to_join = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Reason to join',
    'id':'ytojoin',
    }))

# JobApplicationReviewForm() "To collaborate get and post request" #

class JobApplicationReviewForm(forms.Form):
    name = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Student Name',
    'id':'name',
    }))
    course = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Course',
    'id':'course',
    }))
    sem = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Semester',
    'id':'sem',
    }))
    department = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Department',
    'id':'department',
    }))
    email = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'E-mail',
    'id':'email',
    }))
    mobno = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Phone Number',
    'id':'mobno',
    }))
    resume = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Resume',
    'id':'resume',
    }))
    company = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Company',
    'id':'company',
    }))
    position = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Position',
    'id':'position',
    }))
    reason_to_join = forms.CharField(max_length=30,
    widget = forms.TextInput(attrs={
    'class':'form-horizontal',
    'placeholder':'Reason to join',
    'id':'reason_to_join',
    }))
