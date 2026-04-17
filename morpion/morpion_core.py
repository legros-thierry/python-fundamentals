# --------- LOGIQUE DU JEU (MOTEUR) ------------


# ----------  Initialisation  -------------
COORDS_VALIDES = {"A1","A2","A3","B1","B2","B3","C1","C2","C3"}

COMBINAISONS_GAGNANTES = [
        ("A1", "B1", "C1"),
        ("A2", "B2", "C2"),
        ("A3", "B3", "C3"),
        ("A1", "B2", "C3"),
        ("A3", "B2", "C1"),
        ("A1", "A2", "A3"),
        ("B1", "B2", "B3"),
        ("C1", "C2", "C3")
    ]

def nouvelle_partie():
    return { "board": init_board(),
            "gagne": False,
            "matchnul": False,
            "pion":"X"}

def init_board():
    return {"A1":" ", "B1":" ", "C1":" ",
         "A2":" ", "B2":" ", "C2":" ",
         "A3":" ", "B3":" ", "C3":" ",}

def insert_pion(board, coord, pion):
    board[coord] = pion

def test_victoire(board, pion, combinaisons_gagnantes):
    
    for a, b, c in combinaisons_gagnantes:
        if board[a] == pion and board[b] == pion and board[c] == pion:
            return True
    return False

def test_match_nul(board):
   return all(case != " " for case in board.values())
