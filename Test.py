#!/usr/bin/python3
#testcase for adding two numbers
import unittest

from Prog1 import summation
class TestSum(unittest.TestCase):
  def test_list_int(self):
    """
      Testcase to add two numbers
    """
    data=[20,30]
    result=summation(data)
    self.assertEqual(result,55)

if __name__=='__main__':
  unittest.main()
  
