import requests
import unittest
import random
import unittest
from unittest.mock import patch
from main import get_posts


class TestAPIFeatures(unittest.TestCase):

    @patch('requests.get')
    def test_get_posts(self, mock_get):
        # Mocked response from API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"userId": 1, "id": 1, "title": "Title 1", "body": "Body 1"},
            {"userId": 2, "id": 2, "title": "Title 2", "body": "Body 2"},
            {"userId": 3, "id": 3, "title": "Title 3", "body": "Body 3"},
            {"userId": 4, "id": 4, "title": "Title 4", "body": "Body 4"},
            {"userId": 4, "id": 5, "title": "Title 5", "body": "Body 5"},
            {"userId": 6, "id": 6, "title": "Title 6", "body": "Body 6"},
            {"userId": 7, "id": 7, "title": "Title 7", "body": "Body 7"},
            {"userId": 8, "id": 8, "title": "Title 8", "body": "Body 8"},
            {"userId": 9, "id": 9, "title": "Title 9", "body": "Body 9"},
            {"userId": 10, "id": 10, "title": "Title 10", "body": "Body 10"}
        ]

        # Calling the get_posts function
        result = get_posts()

        # Assertion to ensure correct url is called
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/posts")

        # Check if the returned result matches the mock response
        expected_result = [
            {"userId": 1, "id": 1, "title": "Title 1", "body": "Body 1"},
            {"userId": 2, "id": 2, "title": "Title 2", "body": "Body 2"},
            {"userId": 3, "id": 3, "title": "Title 3", "body": "Body 3"},
            {"userId": 4, "id": 4, "title": "Title 4", "body": "Body 4"},
            {"userId": 4, "id": 5, "title": "Title 5", "body": "Body 5"},
            {"userId": 6, "id": 6, "title": "Title 6", "body": "Body 6"},
            {"userId": 7, "id": 7, "title": "Title 7", "body": "Body 7"},
            {"userId": 8, "id": 8, "title": "Title 8", "body": "Body 8"},
            {"userId": 9, "id": 9, "title": "Title 9", "body": "Body 9"},
            {"userId": 10, "id": 10, "title": "Title 10", "body": "Body 10"}
        ]
        # expected_result = mock_response
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
