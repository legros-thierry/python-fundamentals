class Plateau:

    def __init__(self, nbcase):
        self.nbcase = nbcase
        self.board = self.init_board()
        self.gagne = False
        self.matchnul = False


    # ----------  Initialisation  -------------
    _COORDS_VALIDES = {"A1","A2","A3","B1","B2","B3","C1","C2","C3"}

    _COMBINAISONS_GAGNANTES = [
            ("A1", "B1", "C1"),
            ("A2", "B2", "C2"),
            ("A3", "B3", "C3"),
            ("A1", "B2", "C3"),
            ("A3", "B2", "C1"),
            ("A1", "A2", "A3"),
            ("B1", "B2", "B3"),
            ("C1", "C2", "C3")
        ]

    def init_board(self):
        return {"A1":" ", "B1":" ", "C1":" ",
            "A2":" ", "B2":" ", "C2":" ",
            "A3":" ", "B3":" ", "C3":" ",}
        

    def insert_pion(self, coord, pion):
        self.board[coord] = pion

    def test_victoire(self, pion):
        
        for a, b, c in self._COMBINAISONS_GAGNANTES:
            if self.board[a] == pion and self.board[b] == pion and self.board[c] == pion:
                return True
        return False

    def test_match_nul(self):
        return all(case != " " for case in self.board.values())