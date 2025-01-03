from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model): # models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=4000)
    creation_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title