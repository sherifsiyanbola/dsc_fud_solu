from django.db import models
from django.urls import reverse

class Lga(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lga_detail", kwargs={"pk": self.pk})

    def lgaProjectCount(self):
        return self.projects.all().count()
