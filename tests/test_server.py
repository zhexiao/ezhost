"""
This test is for command line args 
"""

import unittest
from ezhost.ServerLists import ServerLists

class ServerListTest(unittest.TestCase):
    def test_server_exist(self):
        self.assertEqual(ServerLists('lamp').value, 'lamp')

    def test_server_non_exist(self):
        self.assertRaises (ValueError, lambda: ServerLists('namp').value)

if __name__ == '__main__':
    unittest.main()