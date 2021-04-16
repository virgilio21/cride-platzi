"""Users model"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField
from django.core.validators import RegexValidator

#Utilies
from cride.utils.models import CrideModel

class User(CrideModel, AbstractUser):

    email = models.EmailField(
        'email address',
        unique = True,
        error_messages = {
            'unique' : 'Ya existe un usuario con ese email.'
        }
    )

    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message = 'Ocurrio un erorr con la validacion del telefono, introducio un mal formato.'
    )
    #blank true para hacer que el dato sea opcional.
    phone_number = models.EmailField(validators = [phone_regex], max_length = 17, blank = True)
    #Indicamos el campo que servira como username y como campo de autenticacion
    USERNAME_FIELD = 'email'
    #Campos requeridos, por default el campo que definimos como username no necesitamos espicificarlo.
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default = True,
        help_text = (
            'Por default todo los usuarios son clientes'
        )
    )
    is_verified = models.BooleanField(
        'verified email address',
        default = False, 
        help_text = 'Campo para saber si el email fue verifado'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username