#!/usr/bin/python

import unittest
import feed_predictor as fp

#class BinTestCase(unittest.TestCase):

#class BarnTestCase(unittest.TestCase):

class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
	self.app = fp.Application(master=root)

if __name__ == '__main__':
    unittest.main()
