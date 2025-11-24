import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get("/")
        self.assertIn(b"Simple Movie Site", response.data)
        self.assertIn(b"Inception", response.data)

if __name__ == "__main__":
    unittest.main()
