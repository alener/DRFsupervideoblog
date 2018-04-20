from django.db import models
from django.conf import settings


##comments = 

class Collection(models.Model):

    creator = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    title = models.CharField( max_length = 50)

    goals  = models.TextField()

    description  = models.TextField()


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Video Collection'
        verbose_name_plural = 'Videos Collections'

    @property
    def owner(self):
        return self.creator