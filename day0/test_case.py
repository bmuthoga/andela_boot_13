# Test Cases

import unittest
from app import logic

class TestCalculator(unittest.TestCase):
	
	# Test if it adds correctly.
	def test_magic_sum(self):
		self.assertEqual(logic.magic_sum(5), 15)
	
	# Test if negative number exception handled.
	def test_negative_number(self):
		self.assertEqual(logic.magic_sum(-5))