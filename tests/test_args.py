"""
This test is for command line args 
"""

import unittest
import argparse

class ArgsTest(unittest.TestCase):
    def test_args_namespace(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-t', 
            '--test', 
            help='test arg', 
        )
        args = parser.parse_args()
        assert (args.test is None)

    def test_args_value(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--bar')
        parser.add_argument('--foo')
        args = parser.parse_args(['--bar', 'YYY', '--foo', 'ZZZ'])     
        assert (args.bar=='YYY') and (args.foo=='ZZZ')

if __name__ == '__main__':
    unittest.main()