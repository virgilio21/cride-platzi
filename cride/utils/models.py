#Django
from django.db import models

class CrideModel(models.Model):

    created_at = models.DateTimeField(
        auto_now_add = True,
        help_text = 'Se guarda la fecha en la que se creo el modelo o objeto'
    )
    updated_at = models.DateTimeField(
        auto_now = True,
        help_text = 'Se guarda la fecha en que fue llamado el modelo por ultima vez'
    )
    #La clase meta no permite algunas cosas entre ellas la mas importante
    #Nos va a permiter declarar la clase CrideModel como abstracta y de esta forma servir
    #Como clase base para los demas modelos.
    class Meta:
        abstract = True
        #El ultimo objeto en ser creado.
        get_latest_by = 'created_at'
        #La forma en que se ordenan los registros
        ordering = ['-created_at', '-updated_at']