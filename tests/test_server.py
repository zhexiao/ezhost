"""
    This test is for command line args
"""

import unittest
from ezhost.ServerLists import ServerLists


class ServerListTest(unittest.TestCase):

    def test_server_exist(self):
        """
            Check server is exist in ServerLists
        """
        self.assertEqual(ServerLists('lamp').value, 'lamp')

    def test_server_non_exist(self):
        """
            Check if server is not exist, should raise a valueError
        """
        self.assertRaises(ValueError, lambda: ServerLists('namp').value)


if __name__ == '__main__':
    unittest.main()
