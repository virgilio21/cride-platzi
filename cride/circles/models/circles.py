"""Circle model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CrideModel


class Circle(CrideModel):
    """Circle model.
    A circle is a private group where rides are offered and taken
    by its members. To join a circle a user must receive an unique
    invitation code from an existing circle member.
    """

    name = models.CharField('circle name', max_length = 140)
    slug_name = models.SlugField(unique = True, max_length = 140)
    about = models.TextField('circle description', max_length = 255)
    picture = models.ImageField(upload_to='circles/pictures', blank = True, null = True)

    #Stats
    rides_offered = models.PositiveIntegerField(default = 0)
    rides_taken = models.PositiveIntegerField(default = 0)

    is_verified = models.BooleanField(
        'verificacion de un circulo',
        default = True,
        help_text = 'verificar un circulo es la forma de saber si es una comunidad oficial'
    )
    is_public = models.BooleanField(
        'como saber si un circulo es privado o publico',
        default = True,
        help_text = 'Public circles are listed in the main page so everyone know about their existence.'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members.'
    )
    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited, this will be the limit on the number of members.'
    )

    def __str__(self):
        """Return circle name."""
        return self.name
    
    #Cambiamos la forma en que se ordenara cuando hagamos circles.objects.all
    #el simbolo - sirve para indicar que se hara de forma descendente.
    #Tenemos que heredar de la clase meta de nuestro modelo abstracto
    class Meta(CrideModel.Meta):
        """Meta class."""

        ordering = ['-rides_taken', '-rides_offered']

