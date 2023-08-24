import requests
import unittest
import random
import unittest
from unittest.mock import patch
from main import get_posts, select_post, view_post_comments, post_comment, search_posts_by_title


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
        expected_result_2 = [
            {"userId": 1, "id": 1, "title": "Title 1", "body": "Body 1"},
            {"userId": 2, "id": 2, "title": "Title 2", "body": "Body 2"},
            {"userId": 3, "id": 3, "title": "Title 3", "body": "Body 3"}
        ]
        # expected_result = mock_response
        self.assertEqual(result, expected_result)
        #check if output is not similar
        self.assertNotEqual(result, expected_result_2, "Items with different output expected but items have similar output")

    @patch("requests.get")
    def test_select_post(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"userId": 11, "id": 11, "title": "Title 10", "body": "Body 10"}

        # Calling the select_post function
        test_id = 11
        result = select_post(id)
        self.assertNotEqual(result, "Post Id does not exist")
        self.assertEqual(result["id"], test_id)

    @patch("requests.get")
    def test_view_post_comments(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"postId": 1, "id": 1, "Text": "Text 1", },
                                                   {"postId": 1, "id": 2, "Text": "Text 2", },
                                                   {"postId": 3, "id": 3, "Text": "Text 3", }]

        result = view_post_comments(1)

        # Check to ensure comments are present
        self.assertNotEqual(result, "No Comments")
        # Checks to ensure comments are for the post id selected
        self.assertEqual(result[0]['postId'], 1)
        self.assertEqual(result[1]['postId'], 1)
        self.assertEqual(result[2]['postId'], 3)

    @patch("requests.post")
    def test_post_comment(self, mock_post):
        mock_post.return_value.status_code = 201

        result = post_comment(10, "Brian Wahome", "brian@gmail.com", "Nice post")
        self.assertTrue(result)

    @patch("requests.get")
    def test_search_posts_by_title(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"userId": 1, "id": 1, "title": "Test", "body": "Body 1"},
            {"userId": 3, "id": 2, "title": "Search", "body": "Body 2"},
            {"userId": 1, "id": 3, "title": "sEarch ", "body": "Body 3"}
        ]

        matching_posts = search_posts_by_title("Search")
        # Check if any post has been matched
        self.assertIsNotNone(matching_posts)
        # Check if number of posts matched is similar to what is expected
        self.assertEqual(len(matching_posts), 2)
        # Check if titles are similar
        self.assertEqual(matching_posts[0]["title"], "Search")


if __name__ == '__main__':
    unittest.main()
