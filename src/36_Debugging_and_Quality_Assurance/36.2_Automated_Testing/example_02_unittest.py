#!/usr/bin/env python

import unittest
import fac

class MyTest(unittest.TestCase):
    def testCalculation(self):
        self.assertEqual(fac.fac(5), 120)
        self.assertEqual(fac.fac(10), 3628800)
        self.assertEqual(fac.fac(20), 2432902008176640000)

    def testExceptions(self):
        self.assertRaises(ValueError, fac.fac, -1)

if __name__ == "__main__":
    unittest.main()


