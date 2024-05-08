import unittest
from poker_spades_games import check_straight, check_3ofa_kind, check_royal_flush, play_cards


class TestspgFunctions(unittest.TestCase):
    def test_check_straight(self):
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S6', 'S5', 'S7'), 7)
        self.assertEqual(check_straight('S3', 'SQ', 'SK'), 0)

    def test_check_3ofa_kind(self):
        self.assertEqual(check_3ofa_kind('S5', 'S5', 'S5'), 5)
        self.assertEqual(check_3ofa_kind('S2', 'S4', 'S2'), 0)
        self.assertEqual(check_3ofa_kind('S8', 'S4', 'SJ'), 0)

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 14)
        self.assertEqual(check_royal_flush('S10', 'SJ', 'SK'), 0)
        self.assertEqual(check_royal_flush('S6', 'SQ', 'S3'), 0)

    def test_play_cards(self):
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'S8', 'S9', 'S10'), 1)
        self.assertEqual(play_cards('S8', 'S6', 'S7', 'S4', 'S3', 'S2'), -1)
        self.assertEqual(play_cards('S9', 'S9', 'S9', 'S7', 'S7', 'S7'), -1)
        self.assertEqual(play_cards('S4', 'S4', 'S4', 'S10', 'S10', 'S10'), 1)
        self.assertEqual(play_cards('SA', 'SK', 'SQ', 'S10', 'SJ', 'SK'), -1)
        self.assertEqual(play_cards('S10', 'SJ', 'SK', 'SA', 'SK', 'SQ'), 1)
        self.assertEqual(play_cards('S10', 'SJ', 'SQ', 'S8', 'SK', 'SQ'), 0)


if __name__ == '__main__':
    unittest.main()
