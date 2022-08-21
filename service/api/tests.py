import json
from django.test import TestCase
from rest_framework import status

from django.test import Client as Web_client
from api.models import Client

class TestClient(TestCase):
    
    def setUp(self):
        Client.objects.create(
            phone='898790', phone_code='898', tag='tag', time_zone='timezone')
        
        Client.objects.create(
            phone='361782', phone_code='898', tag='tag2', time_zone='timezone')
        
    
    def test_create_client(self):
        c = Web_client()
        response = c.post('/service/client/', {
            'phone': '456783',
            'phone_code': '987',
            'tag' : 'newtag',
            'time_zone' : 'newTimezone'
        })
        
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_client(self):
        c = Web_client()
        response = c.get('/service/client/')
        response.content
        print(response.json())
        
    def test_update_client(self):
        c = Web_client()
        response = c.put('/service/client/1/', {
            'phone': '456783',
            'phone_code': '987',
            'tag' : 'newtag',
            'time_zone' : 'newTimezone'
        })

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
        