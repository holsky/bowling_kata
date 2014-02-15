import unittest
from bowling_array_index import Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game()

    def roll(self, rolls):
        for pins in rolls:
            self.game.record_roll(pins)

    def assert_score(self, score):
        self.assertEquals(self.game.score(), score)

    def test_gutter_game(self):
        self.roll([0] * 20)

        self.assert_score(0)

    def test_all_ones(self):
        self.roll([1] * 20)

        self.assert_score(20)

    def test_one_spare(self):
        self.roll([5,5,1] + [0] * 17)

        self.assert_score(12)

    def test_one_strike(self):
        self.roll([10, 1, 2] + [0] * 16)
        
        self.assert_score(16)

    def test_perfect_game(self):
        self.roll([10] * 12)

        self.assert_score(300)

if __name__ == '__main__':
    unittest.main()
