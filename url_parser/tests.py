from django.test import TestCase
from .models import UrlAdminModel as Model


class DBTestCase(TestCase):
    def test_model(self):
        test = Model.objects.create(url="url.ru")
        urls = Model.objects.values()
        list_result = [entry for entry in urls]
        d = list_result[0]
        self.assertTrue('id' in d)
