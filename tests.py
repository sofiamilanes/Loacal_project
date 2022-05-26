from unittest import TestCase
from server import app

class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        """Stuff to do after each test."""

    def test1(self):
        """Some test..."""

    def test2(self):
        """Some other test"""

    def test_some_flask_route(self):
        """Some non-database test..."""

        result = self.client.get("/homepage")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<h1>Test</h1>', result.data)

    def test_login(self):
        """Test login page."""

        result = self.client.post("/login",
                                data={"user_id": "rachel", "password": "123"},
                                follow_redirects=True)
        self.assertIn(b"Welcome Rachel", result.data)