import unittest

from mammal.project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Test mammal", "predator", "roar")

    def test_attr_set_up(self):
        self.assertEqual("Test mammal", self.mammal.name)
        self.assertEqual("predator", self.mammal.type)
        self.assertEqual("roar", self.mammal.sound)
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound_return(self):
        self.assertEqual("Test mammal makes roar", self.mammal.make_sound())

    def test_get_kingdom_return(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_return(self):
        self.assertEqual("Test mammal is of type predator", self.mammal.info())

if __name__ == '__main__':
    unittest.main()
