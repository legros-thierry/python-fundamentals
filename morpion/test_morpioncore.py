import unittest
from morpion_core import (
    init_board,
    insert_pion,
    test_victoire,
    test_match_nul,
    COMBINAISONS_GAGNANTES,
)


class TestMorpionCore(unittest.TestCase):
    def test_init_board_vide(self):
        board = init_board()
        # toutes les cases doivent être vides
        self.assertTrue(all(case == " " for case in board.values()))

    def test_insert_pion(self):
        board = init_board()
        insert_pion(board, "A1", "X")
        self.assertEqual(board["A1"], "X")

    def test_victoire_ligne(self):
        board = init_board()
        board["A1"] = board["B1"] = board["C1"] = "X"
        self.assertTrue(test_victoire(board, "X", COMBINAISONS_GAGNANTES))

    def test_pas_victoire(self):
        board = init_board()
        board["A1"] = "X"
        board["B1"] = "O"
        board["C1"] = "X"
        self.assertFalse(test_victoire(board, "X", COMBINAISONS_GAGNANTES))

    def test_match_nul(self):
        # plateau sans cases vides
        board = {
            "A1": "X", "B1": "O", "C1": "X",
            "A2": "X", "B2": "O", "C2": "O",
            "A3": "O", "B3": "X", "C3": "X",
        }
        self.assertTrue(test_match_nul(board))


if __name__ == "__main__":
    unittest.main()