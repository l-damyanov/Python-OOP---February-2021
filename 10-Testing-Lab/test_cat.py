import unittest

class CatTests(unittest.TestCase):
    name = "Kitty"

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_eat_expect_size_to_be_increased_by_1(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_eat__expect_fed_to_be_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_sleep__when_fed__expect_not_to_be_sleepy(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_cat_eat_when_fed__expect_exception(self):
        self.cat.eat()

        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_sleep_when_not_fed__expect_exception(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

if __name__ == '__main__':
    unittest.main()
