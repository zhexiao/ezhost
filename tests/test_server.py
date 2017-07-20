"""
    This test is for command line args
"""

import unittest
import argparse
import configparser
from ezhost.BigDataArchi import BigDataArchi


class ServerTest(unittest.TestCase):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--server',
        help='服务器代替名',
    )

    def test_bigdata(self):
        """
        Test ssh generate
        :return:
        """
        args = self.parser.parse_args([
            '-'
        ])
        BigDataArchi(args).install()

if __name__ == '__main__':
    unittest.main()
