import unittest

from workshop_hash_table.hashtable import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable()

    def test_attributes(self):
        self.assertEqual(4, len(self.hash_table.keys))
        self.assertEqual(4, len(self.hash_table.values))
        self.assertEqual(4, self.hash_table.max_capacity)

    def test_add_available_space(self):
        self.hash_table.add("test_key_1", "Value_1")
        self.assertEqual(1, self.hash_table.actual_length)
        self.assertEqual(4, self.hash_table.max_capacity)
        self.assertEqual("Value_1", self.hash_table["test_key_1"])

    def test_add_available_with_no_available_space_resize(self):
        for number in range(1, self.hash_table.max_capacity + 1):
            self.hash_table.add(f"test_key_{number}", f"Value_{number}")
        self.assertEqual(4, self.hash_table.actual_length)
        self.assertEqual(4, self.hash_table.max_capacity)

        # Here we overload the dict and it should resize
        self.hash_table.add("test_key_9", "Value_9")
        self.assertEqual(5, self.hash_table.actual_length)
        self.assertEqual(8, self.hash_table.max_capacity)
        self.assertIn("test_key_9", self.hash_table.keys)

    def test_value_is_replaced_when_key_exists(self):
        self.hash_table.add("test_key", "value")
        self.assertEqual("value", self.hash_table["test_key"])
        self.hash_table["test_key"] = "new_value"
        self.assertEqual("new_value", self.hash_table["test_key"])

    def test_get_with_not_existing_key(self):
        self.hash_table.add("test_key", "value")
        self.assertIsNone(self.hash_table.get("non_existing"))

    def test_get_with_not_existing_key_with_default_value(self):
        self.hash_table.add("test_key", "value")
        self.assertEqual("DEFAULT", self.hash_table.get("non_existing", "DEFAULT"))

    def test_representation(self):
        self.hash_table.add("test_key", "value")
        self.assertEqual("{test_key: value}", str(self.hash_table))

    def test_collision_set_next_available_index(self):
        self.hash_table["name"] = "Peter"
        self.assertEqual(1, self.hash_table.keys.index("name"))
        self.hash_table["age"] = 25
        self.assertEqual(2, self.hash_table.keys.index("age"))
        self.hash_table["name"] = "Peter"
