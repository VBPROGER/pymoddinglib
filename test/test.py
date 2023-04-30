#!/usr/bin/env python3
import unittest, pymoddinglib, pymoddinglib.magic as magic

class TestPyModdingLib(unittest.TestCase):
    def setUp(self): self.pml = pymoddinglib
    def test_check_is_bytecode(self):
        with self.assertRaises(TypeError): self.pml.check_is_bytecode('test')
        self.assertFalse(self.pml.check_is_bytecode(b'test'))
        self.assertTrue(self.pml.check_is_bytecode(magic.PY_MAGIC))
    def test_check_file_format(self):
        self.assertFalse(self.pml.check_file_format())
    def test_get_fields(self):
        AssemblyError = self.pml.AssemblyError
        AssemblyInformationExample = lambda: None
        AssemblyInformationExample.Information = self.pml.PyAssemblyInformation(AssemblyName = 'Example')
        with self.assertRaises(AssemblyError): self.pml.get_fields('test')
        with self.assertRaises(AssemblyError): self.pml.get_fields(b'test')
        self.assertEqual(self.pml.get_fields(AssemblyInformationExample), AssemblyInformationExample.Information)

if __name__ == '__main__':
    unittest.main()
