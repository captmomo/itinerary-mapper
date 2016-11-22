import unittest

from server import app
from model import db, example_data, connect_to_db


class ItineraryTests(unittest.TestCase):
    """Tests for my site"""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("Create an Account", result.data)
        self.assertNotIn("Logout", result.data)


class ItineraryDatabaseTests(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Set up the database before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///testitinerarydb")

        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()


if __name__ == "__main__":
    unittest.main()
