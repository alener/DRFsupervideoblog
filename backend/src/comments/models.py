from django.db import models

from django.conf import settings


from videoposts.models import SuperVideoPost

class Comment(models.Model):

    super_video_post = models.ForeignKey(SuperVideoPost, on_delete=models.CASCADE, related_name='comments')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )



    body = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    @property
    def owner(self):
        return self.user

