import unittest
from app import app  # import your Flask app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Test that the home page returns HTTP 200
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        # Test that the home page contains some expected text
        response = self.app.get("/")
        self.assertIn(b"Simple Movie Site", response.data)
        self.assertIn(b"Top Movies", response.data)
        self.assertIn(b"The Shawshank Redemption", response.data)
        self.assertIn(b"Inception", response.data)
        self.assertIn(b"Interstellar", response.data)
        self.assertIn(b"The Dark Knight", response.data)
        self.assertIn(b"Avengers: Endgame", response.data)

if __name__ == "__main__":
    unittest.main()
