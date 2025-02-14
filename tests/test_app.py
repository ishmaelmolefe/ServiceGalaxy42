# test_service.py
import unittest
from unittest.mock import patch, MagicMock
from service import search_car_availability

class TestCarSearchPagination(unittest.TestCase):
    @patch("service.get_cars")
    def test_search_car_found_on_second_page(self, mock_get_cars):
        """
        Test that the car is found when it exists on the second page of results.
        """
        # Mock token
        token = "valid_token_123"

        # Configure mock_get_cars to return:
        # - Page 1: 10 cars (none matching Toyota Corolla)
        # - Page 2: 1 car (Toyota Corolla)
        mock_get_cars.side_effect = [
            # Page 1 response
            {
                "cars": [
                    {"make": "Honda", "model": "Civic", "available": True}
                    for _ in range(10)  # 10 Hondas (page 1)
                ]
            },
            # Page 2 response
            {
                "cars": [
                    {"make": "Toyota", "model": "Corolla", "available": True}
                ]
            },
        ]

        # Execute search
        result = search_car_availability(token, "Toyota", "Corolla")

        # Assertions
        self.assertTrue(result, "Car should be found and available")
        self.assertEqual(mock_get_cars.call_count, 2, "Should fetch 2 pages")
        mock_get_cars.assert_any_call(token, page=1, limit=10)
        mock_get_cars.assert_any_call(token, page=2, limit=10)

    @patch("service.get_cars")
    def test_search_car_not_found(self, mock_get_cars):
        """
        Test that the car is NOT found when it doesn't exist in any page.
        """
        token = "valid_token_123"
        
        # Mock empty responses for all pages
        mock_get_cars.return_value = {"cars": []}

        result = search_car_availability(token, "Tesla", "Model S")
        self.assertFalse(result, "Car should not be found")