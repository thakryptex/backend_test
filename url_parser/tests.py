from django.test import TestCase
from .models import UrlAdminModel as Model
from datetime import datetime
from django.utils import timezone


class DBTestCase(TestCase):
    def test_model(self):
        dtime = datetime.now()
        ttime = timezone.now()
        test = Model.objects.create(url="url.ru", time=dtime)
        Model.objects.filter(url="url.ru").update(time=ttime)
        h1 = int(dtime.hour)
        h2 = int(ttime.hour)
        self.assertTrue(h1 == h2)
