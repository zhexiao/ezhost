"""
This test is for config file
"""

import unittest, os
import configparser

class ConfTest(unittest.TestCase):
    def _setup_(self):
        self.config = configparser.ConfigParser()
        self.path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.config.read('{0}/data/test_config.ini'.format(self.path))

    def test_config_non_namespace(self):
        self._setup_()

        self.assertNotIn('python', self.config)

    def test_config_namespace(self):
        self._setup_()

        self.assertIn('ezhost', self.config)

    def test_config_value(self):
        self._setup_()
        
        self.assertNotEqual(self.config['ezhost']['user'], 'zx')

    def test_config_non_exist(self):
        self._setup_()

        self.assertRaises (KeyError, lambda: self.config['ezhost']['abc'])

if __name__ == '__main__':
    unittest.main()