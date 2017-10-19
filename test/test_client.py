
import sys
import unittest
from unittest.mock import Mock

sys.path.append(".")

from client import Client


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.mock_service = Mock()

    def test_service_gets_called(self):
        Client(self.mock_service).run() 
        #print(self.mock_service.send)
        #print(self.mock_service.mock_calls[0])
        print(self.mock_service.send.mock_calls)
        print(self.mock_service.mock_calls)
        self.mock_service.send.assert_called_once_with("hello")
        #self.mock_service.send.assert_called

if __name__ == '__main__':
    unittest.main()        
