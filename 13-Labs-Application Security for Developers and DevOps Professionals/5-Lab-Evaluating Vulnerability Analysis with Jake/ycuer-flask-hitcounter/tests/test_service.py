"""
Test Cases for Hitcounter Service
"""
import json
from unittest import TestCase
from hitcounter import app


class TestHitcounterService(TestCase):
    """Test case for HitCounter Service"""

    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        """In should return the home page"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_get_hitcount(self):
        """It should Get the current hit count"""
        resp = self.client.get("/hits")
        self.assertEqual(resp.status_code, 200)
        body = json.loads(resp.data)
        count = body["counter"]
        self.assertEqual(count, 0)

    def test_increment_hitcount(self):
        """In should Increment the hit count"""
        # increment the counter
        resp = self.client.put("/hits")
        self.assertEqual(resp.status_code, 200)
        body = json.loads(resp.data)
        count = body["counter"]
        self.assertEqual(count, 1)
