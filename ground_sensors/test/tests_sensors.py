from rest_framework.test import APITestCase
from ground_sensors.models import GroundSensor
from django.urls import reverse
from rest_framework import status


class SensorsTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('GroundSensor-list')
        self.device = GroundSensor.objects.create(
            device='11223344',
            soil_humidity=40,
            air_humidity=55,
            temperature=25.00,
            battery_life=98
        )

    def test_requisicao_get(self):
        """Test to verify GET request"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post(self):
        """Test to verify POST request"""
        data = {
            'device': '22223355',
            'soil_humidity': 45,
            'air_humidity': 57,
            'temperature': 20.00,
            'battery_life': 98
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put(self):
        """Test to verify PUT request"""
        data = {
            'device': '11223344',
            'soil_humidity': 46,
            'air_humidity': 52,
            'temperature': 25.00,
            'battery_life': 92
        }
        response = self.client.put('/GroundSensor/11223344/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        """Test to verify DELETE request"""
        response = self.client.delete('/GroundSensor/11223344/')
        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT)
