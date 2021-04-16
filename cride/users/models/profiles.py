"""Profile users"""
#Django
from django.db import models 

#Utilities
from cride.utils.models import CrideModel

    
class Profile(CrideModel):

    #Si un user se elimina se elimina tambien el profile
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    picture = models.ImageField(
        'imagen de perfil',
        upload_to = 'users/pictures/',
        blank = True,
        null = True
    )
    biography = models.TextField(max_length = 500, blank = True)
    
    #Stats
    rides_taken = models.PositiveIntegerField(default = 0)
    rides_offered = models.PositiveIntegerField(default = 0)
    reputation = models.FloatField(
        default = 5.0,
        help_text = 'Reputacion de usuarios basado en los rides que han ofrecido'
    )

    def __str__(self):
        return str(self.user)