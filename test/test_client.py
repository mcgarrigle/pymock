
import unittest

from mock import patch
from service import Service

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.mock_cursor = MagicMock()
        self.test_hb = HeartBeater(self.mock_cursor, self.mock_metrics)

    def test_service_gets_called:
        Client().run() 
        
