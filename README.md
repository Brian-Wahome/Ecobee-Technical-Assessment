# Ecobee-Technical-Assessment
CLI app to add new features and functionallity to the  JSON Placeholder (https://jsonplaceholder.typicode.com/) API

Features of the app are as listed below:
* List Random Posts: Fetches and displays a list of 10 random posts from the remote API.
* View Post: Allows the user to select a post by its ID and displays its details.
* View and Post Comments: Displays comments on a selected post and lets the user post their own comment.
* Search for post by title: Allows the user to search through all posts using keywords in title.

# Getting Started
**Prerequisites**
* Python3.8+
* pip

**Installation**
* Clone the repository using the following command 'git clone https://github.com/Brian-Wahome/Ecobee-Technical-Assessment.git'
* Install the required packages using 'pip install -r requirements.txt'

# Running the app
Run the CLI app by running the command 'python main.py' on the terminal

# Running the tests
To run all tests at once run the command 'python tests.py'

**Running test_get_posts**

To run the test for the get_posts function run the command 'python -m unittest tests.TestAPIFeatures.test_get_posts'

**Running test_select_post**

To run the test for the select_post function run the command 'python -m unittest tests.TestAPIFeatures.test_select_post'

**Running test_view_post_comments**

To run the test for the view_post_comments function run the command 'python -m unittest tests.TestAPIFeatures.test_view_post_comments'

**Running test_post_comment**

To run the test for the post_comment function run the command 'python -m unittest tests.TestAPIFeatures.test_post_comment'

**Running test_search_posts_by_title**

To run the test for the search_posts_by_title function run the command 'python -m unittest tests.TestAPIFeatures.test_search_posts_by_title'

**Running the test_search_posts_by_title_api_error**

To run the test_search_posts_by_title_api_error test run the command 'python -m unittest tests.TestAPIFeatures.test_search_posts_by_title'


