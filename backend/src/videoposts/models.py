from django.db import models
from django.conf import settings

from postcollections.models import Collection

class SuperVideoPost(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    collection = models.ManyToManyField(Collection)

    title = models.CharField( max_length=50)

    description = models.TextField()

    goals  = models.TextField()

    how_to = models.TextField()

    youtube_link = models.URLField(max_length=200)

    image_link =  models.URLField(max_length=200)

    start = models.PositiveSmallIntegerField()

    end = models.PositiveSmallIntegerField()

    file = models.FileField(upload_to='uploads/',default='file/None/No-doc.pdf')




    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Super Video Post'
        verbose_name_plural = 'Super Video Posts'

    @property
    def owner(self):
        return self.user
