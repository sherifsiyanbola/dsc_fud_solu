from django.db import models
from django.urls import reverse

class Ministry(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ministry_detail", kwargs={"pk": self.pk})
    
    def ministryProjectCount(self):
        return self.projects.all().count()
    