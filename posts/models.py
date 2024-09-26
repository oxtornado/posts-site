from django.db import models
from django.urls import reverse 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("posts_detail", kwargs={"pk": self.pk})