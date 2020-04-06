import unittest
from jsonable import Jsonable
from xmlable import Xmlable
from main import Panda


class TestSerialization(unittest.TestCase):
    def test_serialization_to_json(self):
        p = Panda(name='Marto')

        result = p.to_json()

        self.assertEqual(result,\
         '{\n    "dict": {\n        "name": "Marto"\n    },\n    "type": "Panda"\n}')


    def test_serialization_to_xml(self):
        p = Panda(name='Marto')

        result = p.to_xml()

        self.assertEqual(result,\
         '<Panda><name>Ivo</name></Panda>')



if __name__ == '__main__':
    unittest.main()
