from django import forms
from django.contrib.auth.models import User
from .models import Address,File,Profile_img
import re

class Profile_imgF(forms.ModelForm):
    class Meta:
        model= Profile_img
        fields = "__all__"
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control form-control-md','multiple': True}),
        }

# class

class Update_usernameF(forms.ModelForm):
    class Meta:
        model=User
        # help_texts = {
        #     'username': None,
        #     # 'password': 'Password should be alphanumeric, and One Special character (Minimum Length of password is 8)'
        # }
        fields=['username']

    def clean_username(self):
        ipname = self.cleaned_data['username']
        if (len(ipname) >= 6):
            return ipname
        else:
            raise forms.ValidationError('User name Must be greater than 6 letters')


class Address_Form(forms.ModelForm):
    class Meta:
        model= Address
        fields = "__all__"
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Name Here'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eg. T-866-67, Faiz Road'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your City Here'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your State Here'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Postal code Here'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile Number Here'})
        }

    def clean_zip_code(self):
        zip = self.cleaned_data['zip_code']
        if (len(zip) == 6):
            return zip
        else:
            raise forms.ValidationError('Wrong Input! Please Enter valid Zip Code')

    def clean_number(self):
        mbno = self.cleaned_data['number']
        if re.match("^[6-9]{1}[0-9]{9}$", mbno):
            return mbno
        else:
            raise forms.ValidationError('Please Enter Valid Mobile No.')


class File_Form(forms.ModelForm):
    class Meta:
        model= File
        fields = "__all__"
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email ID Here'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control form-control-md','multiple': True})
        }


class Signup(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-Enter Your Password '}))

    # username = forms.CharField(help_text=False)
    class Meta:
        model = User
        help_texts = {
            'username': None,
            # 'password': 'Password should be alphanumeric, and One Special character (Minimum Length of password is 8)'
        }
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name Here'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name Here'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email ID Here'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username Here'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password Here'}),
            # 'Confirm_Password':forms.PasswordInput(attrs={'class':'form-control'}),
        }

    def clean_username(self):
        ipname = self.cleaned_data['username']
        if (len(ipname) >= 6):
            return ipname
        else:
            raise forms.ValidationError('User name Must be greater than 6 letters')

    def clean_email(self):
        email = self.cleaned_data['email']
        if re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):
            return email
        else:
            raise forms.ValidationError('Please Enter valid email Address')

    def clean_password(self):
        password = self.cleaned_data['password']
        if re.fullmatch('^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$', password):
            return password
        else:
            raise forms.ValidationError('''Password Must contains:
                                             Minimum One Uppercase, One lowercase
                                             any number, and One Special character
                                             (Minimum Length of password is 8)
                                             ''')

    def clean(self):
        cleaned_data = super(Signup, self).clean()
        Password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("Confirm_Password")

        if Password != confirm_password:
            raise forms.ValidationError('Password and Confirm Password does not match')




