""" 
Como ejecutar esta prueba
python -m unittest tests.test_api_client.ApiClientTests
python -m unittest tests.test_api_client.ApiClientTests.test_get_location_returns_side_effect
"""

import unittest, requests
import unittest.mock

from unittest.mock import patch
# from api_client import get_location
from src.api_client import get_location

class ApiClientTests(unittest.TestCase):
    
    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        ipGoogle = "8.8.8.8"        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'ipVersion': 4,
            'ipAddress': '8.8.8.8',
            'latitude': 37.386051,
            'longitude': -122.083847,
            # 'countryName': 'United States of America',
            # 'regionName': 'California',
            # 'cityName': 'Mountain View',
            'countryName': 'USA',
            'regionName': 'Florida',
            'cityName': 'MIAMI',
            'countryCode': 'US',
            'timeZone': '-08:00',
            'zipCode': '94035',
            'isProxy': False,
            'continent': 'Americas',
            'continentCode': 'AM',
            'currency': {'code': 'USD',
            'name': 'US Dollar'},
            'language': 'English',
            'timeZones': [
                'America/Adak',
                'America/Anchorage',
                'America/Boise',
                'America/Chicago',
                'America/Denver',
                'America/Detroit',
                'America/Indiana/Indianapolis',
                'America/Indiana/Knox',
                'America/Indiana/Marengo',
                'America/Indiana/Petersburg',
                'America/Indiana/Tell_City',
                'America/Indiana/Vevay',
                'America/Indiana/Vincennes',
                'America/Indiana/Winamac',
                'America/Juneau',
                'America/Kentucky/Louisville',
                'America/Kentucky/Monticello',
                'America/Los_Angeles',
                'America/Menominee',
                'America/Metlakatla',
                'America/New_York',
                'America/Nome',
                'America/North_Dakota/Beulah',
                'America/North_Dakota/Center',
                'America/North_Dakota/New_Salem',
                'America/Phoenix',
                'America/Sitka',
                'America/Yakutat',
                'Pacific/Honolulu'
                ],
            'tlds': ['.us']
        }
        response = get_location(ipGoogle)
        # self.assertCountEqual( response.get('country'), 'United States of America')
        self.assertCountEqual( response.get('country'), 'USA')
        self.assertCountEqual( response.get('region'), 'Florida')
        self.assertCountEqual( response.get('city'), 'MIAMI')
        mock_get.assert_called_once_with(f"http://freeipapi.com/api/json/8.8.8.8") # prueba la url
        
        
    @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        ipGoogle = "8.8.8.8"
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda:{
                    'countryName': 'USA',
                    'regionName': 'Florida',
                    'cityName': 'MIAMI',
                }
            )
        ] 
        
        with self.assertRaises(requests.exceptions.RequestException):
            get_location(ipGoogle)
        response = get_location(ipGoogle)
        # self.assertCountEqual( response.get('country'), 'United States of America')
        self.assertCountEqual( response.get('country'), 'USA')
        self.assertCountEqual( response.get('region'), 'Florida')
        self.assertCountEqual( response.get('city'), 'MIAMI')
        # mock_get.assert_called_once_with(f"http://freeipapi.com/api/json/8.8.8.8") # prueba la url
    