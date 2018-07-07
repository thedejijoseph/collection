# used to go about unittesting
# in close collaboration with greenwall.py

import unittest
from greenwall import implode, get_region, get_region_pop
from greenwall import GatePass

class GreenwallTestCase(unittest.TestCase):
	"""Tests for greenwall.py"""
	
	def test_implode(self):
		"""Is steel stronger than concrete?"""
		will_implode = implode("concrete", "steel")
		self.assertEqual(will_implode, True)
	
	def test_implode_withsheet(self):
		"""Is coated 'steel' stronger than concrete?"""
		will_implode = implode("concrete", "steel", "gold")
		self.assertEqual(will_implode, False)
	
	def test_region(self):
		region = get_region("lagos", "nigeria")
		self.assertEqual(region, "Lagos, Nigeria.")
	
	def test_region_pop(self):
		region_pop = get_region_pop("lagos, nigeria", "5m")
		self.assertEqual(region_pop, "Lagos, Nigeria - 5m.")

class GatePassTestCase(unittest.TestCase):
	"""Test cases for greenwall.GatePass."""
	
	def setUp(self):
		"""Create a gatepass and a set of gates to be used in all test cases."""
		gatepass_id = 33
		self.gatepass = GatePass(gatepass_id)
		
		self.gates = [2, 4, 6]
		
	def test_store_single_usage(self):
		"""Test that a single gate is accessed properly."""
		# gatepass(33) is used at Gate 4
		self.gatepass.use_pass(self.gates[0])
		
		self.assertIn(self.gates[0], self.gatepass.pass_usage)
	
	def test_use_gatepass_three_times(self):
		"""Test that a gatepass can be used 3 times."""
		for gate in self.gates:
			self.gatepass.use_pass(gate)
		
		for gate in self.gates:
			self.assertIn(gate, self.gatepass.pass_usage)

unittest.main()
