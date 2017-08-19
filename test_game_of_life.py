import unittest
from patterns import blinker_pattern
from game_of_life import next_generation

class Test_Game_Of_Life(unittest.TestCase):

    def test_two_generations_of_blinker_resets_it(self):
        blinker = blinker_pattern()
        next = next_generation(next_generation(blinker))
        self.assertEqual(set(blinker), set(next))