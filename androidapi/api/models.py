from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Pessoa(models.Model):
    nascimento = models.DateField(null=True, blank=True)
    status = models.IntegerField(null=False, blank=False, default=0)
    endereco = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=15, blank=True)

    class Meta:
        abstract = True

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Nome de usuário é obrigatório.')
        
        person = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password
        )

        person.set_password(password)
        person.save(using=self._db)
        return person
    
    def create_superuser(self, username, email, password):
        person = self.create_user(
            username,
            email,
            password,
        )

        person.status = 1
        person.is_superuser = True
        person.save(using=self._db)
        return person

class Usuario(Pessoa, AbstractUser):
    objects = UsuarioManager()
