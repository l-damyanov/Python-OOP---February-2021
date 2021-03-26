import unittest


class IntegerListTest(unittest.TestCase):
    def test__integer_list_add__when_int__should_add_it(self):
        integer_list = IntegerList()
        internal_list = integer_list.add(1)
        self.assertEqual([1], internal_list)

    def test__integer_list_add__when_str__expect_expectation(self):
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add('as')

    def test_integer_list_remove_index__when_valid_index__expect_to_remove_and_return_it(self):
        value_to_be_removed = 3
        integer_list = IntegerList(1, 2, 3, 4)

        result = integer_list.remove_index(2)
        self.assertEqual(value_to_be_removed, result)
        self.assertEqual([1, 2, 4], integer_list.get_data())

    def test_integer_list_remove_index__when_invalid_negative_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = -4
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)


    def test_integer_list_remove_index__when_invalid_positive_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 3
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)

    def test_integer_list_get__when_valid_index__expect_to_return_it(self):
        integer_list = IntegerList(1, 2, 3, 4)
        index = 2
        result = integer_list.get(index)
        self.assertEqual(3, result)

    def test_integer_list_get__when_invalid_positive_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3, 4)
        index = 6
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integer_list_get__when_invalid_negative_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3, 4)
        index = -6
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integer_list_insert__when_valid_index_and_value__expect_to_insert_it(self):
        integer_list = IntegerList(1, 2, 3)
        index = 1
        value = 5
        integer_list.insert(index, value)
        result = integer_list.get_data()
        self.assertEqual([1, 5, 2, 3], result)

    def test_integer_list_insert__when_invalid_positive_index__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 6
        value = 5
        with self.assertRaises(IndexError):
            integer_list.insert(index, value)

    def test_integer_list_insert__when_value_is_str__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        index = 1
        value = 'yeet'
        with self.assertRaises(ValueError):
            integer_list.insert(index, value)

    def test_integer_list_get_biggest__expect_to_return_the_biggest(self):
        biggest = 17
        integer_list = IntegerList(1, 2, 17, 3, 4)
        actual = integer_list.get_biggest()
        self.assertEqual(biggest, actual)

    def test_integer_list_get_index__when_value_in_list__expect_to_return_the_index(self):
        integer_list = IntegerList(1, 2, 3)
        value = 1
        result = integer_list.get_index(value)
        self.assertEqual(0, result)

    def test_integer_list_get_index__when_value_not_in_list__expect_exception(self):
        integer_list = IntegerList(1, 2, 3)
        value = 23
        with self.assertRaises(ValueError):
            integer_list.get_index(value)

if __name__ == '__main__':
    unittest.main()
