#!/usr/bin/python3
"""Unit tests for models/base_model.py"""

import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModelInstantiation(unittest.TestCase):
    """Tests instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """Test that BaseModel instantiates without any arguments"""
        self.assertEqual(BaseModel, type(BaseModel()))
    def test_new_instance_stored_in_objects(self):
        """Test that a new instance of BaseModel is stored in the objects dictionary"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_str(self):
        """Test that the ID attribute of BaseModel is a string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_updated_at_is_public_datetime(self):
        """Test that the updated_at attribute of BaseModel is a datetime object"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """Test that two instances of BaseModel have unique IDs"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """Test that two instances of BaseModel have different created_at timestamps"""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        """Test that two instances of BaseModel have different updated_at timestamps"""
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        """Test the string representation of a BaseModel instance"""
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        """Test instantiation of BaseModel with unused arguments"""
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation of BaseModel with keyword arguments"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test BaseModel instantiation with None keyword arguments"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        """Test BaseModel instantiation with both positional and keyword arguments"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

class TestBaseModelSave(unittest.TestCase):
    """Tests save method of the BaseModel class."""

    def test_to_dict_type(self):
        """Test type of the returned dictionary by to_dict method"""
        bm = BaseModel()
        self.assertTrue(isinstance(bm.to_dict(), dict))

    def test_to_dict_contains_correct_keys(self):
        """Test if the dictionary returned by to_dict method contains correct keys"""
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the dictionary returned by to_dict method contains added attributes"""
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in the dictionary returned by to_dict method are strings"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of the to_dict method"""
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test the difference to_dict method and __dict__"""
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        """Test to_dict method with argument"""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

if __name__ == "__main__":
    unittest.main()
