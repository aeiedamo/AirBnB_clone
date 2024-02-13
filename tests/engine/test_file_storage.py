import unittest
from unittest.mock import patch
from models.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_initialization(self):
        self.assertEqual(self.storage.__file_path, "file.json")
        self.assertEqual(self.storage.__objects, {})

    @patch("builtins.open", create=True)
    def test_save(self, mock_open):
        mock_file = mock_open.return_value
        self.storage.new(BaseModel())
        self.storage.save()
        mock_file.write.assert_called_once()

    @patch("builtins.open", create=True)
    def test_reload(self, mock_open):
        mock_file = mock_open.return_value
        mock_file.read.return_value = '{"BaseModel.12345": {"id": "12345", "created_at": "2024-02-13T12:00:00", "updated_at": "2024-02-13T12:00:00"}}'
        self.storage.reload()
        self.assertTrue(len(self.storage.__objects) == 1)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertTrue(len(self.storage.__objects) == 1)

    def test_all(self):
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn("BaseModel." + obj.id, objects)


if __name__ == "__main__":
    unittest.main()
