import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from tcpy_parser.tcpy_parser import TCPyParser
from tcpy_parser.tcpy_file import TCPyFile
from tcpy_parser.tcpy_attribute import TCPyAttribute
from tcpy_exceptions.tcpy_exceptions import InvalidTypeError, InvalidFormatError

class TestTCPyParser(unittest.TestCase):
    def setUp(self):
        self.files_to_remove = []

    def tearDown(self):
        for filename in self.files_to_remove:
            if os.path.exists(filename):
                os.remove(filename)

    def create_test_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
        self.files_to_remove.append(filename)

    def test_parse(self):
        filename = "test_data.tcpy"
        content = "id:int:1\nname_len:int:4\nsession_name:str:name_len\n"
        self.create_test_file(filename, content)

        parser = TCPyParser(filename)
        endpoint = parser.parse()

        expected_attributes = [
            TCPyAttribute("id", "int", 1),
            TCPyAttribute("name_len", "int", 4),
            TCPyAttribute("session_name", "str", "name_len")
        ]

        expected_endpoint = TCPyFile(filename, expected_attributes)

        self.assertEqual(endpoint.filepath, expected_endpoint.filepath)
        self.assertEqual(endpoint.attributes, expected_endpoint.attributes)

    def test_invalid_type(self):
        filename = "invalid_type.tcpy"
        content = "id:invalid:1\n"
        self.create_test_file(filename, content)

        parser = TCPyParser(filename)
        with self.assertRaises(InvalidTypeError):
            parser.parse()

    def test_invalid_format(self):
        filename = "invalid_format.tcpy"
        content = "id:int:1\ninvalid_format_line\n"
        self.create_test_file(filename, content)

        parser = TCPyParser(filename)
        with self.assertRaises(InvalidFormatError):
            parser.parse()

if __name__ == '__main__':
    unittest.main()
