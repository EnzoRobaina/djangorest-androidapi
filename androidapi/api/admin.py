from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from androidapi.api.models import Usuario

# Register your models here.

class UsuarioCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('__all__')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match!")
        return password2
    
    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['password1'])
        if commit:
            usuario.save()
        return usuario

class UsuarioChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = (
            '__all__'
        )
    
    def clean_password(self):
        return self.initial['password']

class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm

    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal', {
                'fields': (
                    'first_name', 'last_name', 'cpf',
                    'address', 'phone', 'birth_date'
                )
            }
        ),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
    )

    search_fields = ('username', 'email')
    ordering = ('username', )
    filter_horizontal = ()

admin.site.register(Usuario, UsuarioAdmin)