__all__ = []

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import RegexValidator
from django.utils.html import strip_tags


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                'class': 'input-register form-control',
                'placeholder': 'Your email address',
            },
        ),
    )
    username = forms.CharField(
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'input-register form-control',
                'placeholder': 'Your nickname',
            },
        ),
    )
    first_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'input-register form-control',
                'placeholder': 'Your first name',
            },
        ),
    )
    last_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'input-register form-control',
                'placeholder': 'Your last name',
            },
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-register form-control',
                'placeholder': 'Your password',
            },
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-register form-control',
                'placeholder': 'Confirm your password',
            },
        ),
    )
    marketing_consent1 = forms.BooleanField(
        required=False,
        label='Receive spam',
        widget=forms.CheckboxInput(
            attrs={'class': 'input-register'},
        ),
    )
    marketing_consent2 = forms.BooleanField(
        required=False,
        label='Sell soul here',
        widget=forms.CheckboxInput(
            attrs={'class': 'input-register'},
        ),
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'marketing_consent1',
            'marketing_consent2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is alredy in use.')

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.marketing_consent1 = self.cleaned_data['marketing_consent1']
        user.marketing_consent2 = self.cleaned_data['marketing_consent2']

        if commit:
            user.save()

        return user


class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'input-register form-control',
                'placeholder': 'Your Email',
            },
        ),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'autofocus': True,
                'class': 'input-register form-control',
                'placeholder': 'Your Password',
            },
        ),
    )

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError('Invalid email or password.')

            if not user.is_active:
                raise forms.ValidationError('This account is inactive.')

            self.user_cache = authenticate(
                self.request, email=email, password=password,
            )
            if self.user_cache is None:
                raise forms.ValidationError('Invalid email or password.')

            return self.cleaned_data


class CustomUserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        required=False,
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                'class': 'input-register form-control',
                'placeholder': 'Your email address',
            },
        ),
    )
    phone = forms.CharField(
        required=False,
        validators=[
            RegexValidator(
                r'^\+?1?\d{9,15}$',
                'Enther a valid phone number.',
            ),
        ],
        widget=forms.NumberInput(
            attrs={
                'autofocus': True,
                'class': 'input-register form-control',
                'placeholder': 'Your phone number',
            },
        ),
    )
    first_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'input-register form-control',
                'placeholder': 'Your first name',
            },
        ),
    )
    last_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'input-register form-control',
                'placeholder': 'Your last name',
            },
        ),
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'phone',
            'marketing_consent1',
            'marketing_consent2',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'input-register form-control',
                    'placeholder': 'Your email address',
                },
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'input-register form-control',
                    'placeholder': 'Your first name',
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'input-register form-control',
                    'placeholder': 'Your last name',
                },
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'input-register form-control',
                    'placeholder': 'Your username',
                },
            ),
            'marketing_consent1': forms.CheckboxInput(
                attrs={'class': 'input-register'},
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and (
            User.objects
            .filter(email=email)
            .exclude(id=self.instance.id)
            .exists()
        ):
            raise forms.ValidationError('This email is alredy in use.')

        return email

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get('email'):
            cleaned_data['email'] = self.instance.email

        for field in [
            'first_name',
            'last_name',
            'username',
            'phone',
            'marketing_consent1',
            'marketing_consent2',
        ]:
            if cleaned_data.get(field):
                cleaned_data[field] = strip_tags(cleaned_data[field])

        return cleaned_data
