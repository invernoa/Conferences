from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from  django.db.models import CASCADE

# Create your models here.
class Conference(models.Model):
    title = models.CharField(max_length=255)
    tracks = models.TextField()
    place = models.CharField(max_length=200)
    period = models.DateField()
    description = models.TextField()
    place_description = models.TextField()
    terms = models.TextField()
    published_date = models.DateTimeField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=CASCADE)
    conf = models.ForeignKey(Conference, verbose_name="Conference", on_delete=CASCADE)
    text = models.TextField("Comment text", max_length=500)
    created = models.DateTimeField("Added", auto_now_add=True)
    moder = models.BooleanField("Moderation", default=True)
    CHOICES = (('1', 'Question about applying'), ('2', 'Want to publish'), ('3', 'Other'))
    choice_field = models.CharField(choices=CHOICES, default='none', max_length=25)

    def __str__(self):
        return self.text
