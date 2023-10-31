import unittest
from digital_root import digital_root

class TestDigitalRoot(unittest.TestCase):

  def test_two_digits(self):
    self.assertEqual(digital_root(16), 7)

  def test_three_digits(self):
    self.assertEqual(digital_root(942), 6)

  def test_large_number(self):
    self.assertEqual(digital_root(132189), 6)

  def test_another_large_number(self):
    self.assertEqual(digital_root(493193), 2)

if __name__ == '__main__':
  unittest.main()