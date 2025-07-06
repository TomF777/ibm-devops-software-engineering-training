# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDifferentItemsController(BaseTestCase):
    """DifferentItemsController integration test stubs"""

    def test_items_get(self):
        """Test case for items_get

        Returns a list of items
        """
        response = self.client.open(
            '/items',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
