import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes_default_values(self):
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
