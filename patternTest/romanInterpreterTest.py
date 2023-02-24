'''
Created on 22 févr. 2023

@author: pascal
'''
import unittest
from pattern.romanInterpreter import RomanInterpreter

class RomanInterpreterTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_compute(self):
        interpreter = RomanInterpreter()
        interpreter.compute("VII")
        self.assertEqual(interpreter.get_result(), 7)
        interpreter.compute("XIV")
        self.assertEqual(interpreter.get_result(), 14)
        interpreter.compute("CXXXIX")
        self.assertEqual(interpreter.get_result(), 139)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()