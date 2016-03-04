from django.db import models


class UrlAdminModel(models.Model):
    url = models.URLField()
    timeshift = models.DurationField()

    def __str__(self):
        return self.url