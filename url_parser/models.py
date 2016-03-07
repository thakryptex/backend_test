from django.db import models


class UrlAdminModel(models.Model):
    url = models.URLField(blank=False, verbose_name='URL')
    timeshift = models.PositiveIntegerField(default=0, verbose_name='Time shift (in secs)')

    success = models.BooleanField(default=False)
    title = models.CharField(max_length=128, blank=True, default="", null=True)
    h1 = models.CharField(max_length=128, blank=True, default="", null=True)
    charset = models.CharField(max_length=16, blank=True, default="", null=True)

    time = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'URL to parse'
        verbose_name_plural = 'URLs to parse'
