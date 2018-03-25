import unittest
from stores import get_lat_long, get_nearest

class PetStoreTest(unittest.TestCase):
	def test_latitude(self):
		"Check the latitude of one of the results"
		self.assertEqual(get_lat_long("AL1 2RJ")[0], 51.7417478638519)

	def test_nearest(self):
		"Test the nearest postcode feature with outcode AL1"
		self.assertEqual(get_nearest("AL1")[0]["postcode"], "AL1 2RJ")
