import unittest

from hero.project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.main_hero = Hero("Main hero", 5, 100, 10)
        self.second_hero = Hero("Second hero", 10, 80, 20)

    def test_check_attr_are_set(self):
        self.assertEqual("Main hero", self.main_hero.username)
        self.assertEqual(5, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(10, self.main_hero.damage)

    def test_battle_raises_if_fight_self(self):
        hero_self = Hero("Main hero", 3, 60, 10)
        with self.assertRaises(Exception) as ex:
            self.main_hero.battle(hero_self)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_health_not_enough_raises(self):
        self.main_hero.health = 0
        self.assertEqual(0, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.second_hero)

        self.assertEqual("Your health is lower than or equal to 0. "
                         "You need to rest", str(ex.exception))

    def test_health_is_less_than_zero_raises(self):
        self.main_hero.health = -5
        self.assertEqual(-5, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.second_hero)

        self.assertEqual("Your health is lower than or equal to 0. "
                         "You need to rest", str(ex.exception))

    def test_health_enemy_is_less_than_zero_raises(self):
        self.second_hero.health = -5
        self.assertEqual(-5, self.second_hero.health)
        self.assertEqual(100, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.second_hero)

        self.assertEqual('You cannot fight Second hero. He needs to rest', str(ex.exception))

    def test_fight_draw_case(self):
        self.second_hero.health = 50

        result = self.main_hero.battle(self.second_hero)
        self.assertEqual("Draw", result)

    def test_main_hero_wins(self):
        self.main_hero.damage = 200
        self.main_hero.health = 300

        result = self.main_hero.battle(self.second_hero)
        self.assertEqual("You win", result)
        self.assertEqual(205, self.main_hero.damage)
        self.assertEqual(105, self.main_hero.health)
        self.assertEqual(6, self.main_hero.level)

    def test_enemy_wins(self):
        result = self.main_hero.battle(self.second_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(35, self.second_hero.health)
        self.assertEqual(25, self.second_hero.damage)
        self.assertEqual(11, self.second_hero.level)

        self.assertTrue(self.main_hero.health < 0)

    def test_string_represent(self):
        self.assertEqual("Hero Main hero: 5 lvl\nHealth: 100\nDamage: 10\n", str(self.main_hero))

    def test_enemy_health_zero_raises(self):
        self.second_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.second_hero)
        self.assertEqual("You cannot fight Second hero. He needs to rest", str(ex.exception))

if __name__ == '__main__':
    unittest.main()
