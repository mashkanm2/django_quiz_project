


from django.test import TestCase,Client
from django.urls import reverse
from unittest import mock

class Testquizapp(TestCase):
    def setUp(self):
        self.client = Client()
        return super().setUp()

    
