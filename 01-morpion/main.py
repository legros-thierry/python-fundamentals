from morpion_core import (insert_pion, 
                          test_victoire, 
                          test_match_nul,
                          nouvelle_partie,
                          COMBINAISONS_GAGNANTES,
                          COORDS_VALIDES)

from datetime import datetime

import os


# -----   ENTREE / SORTIE  / AFFICHAGE.  --------
def affiche(board):
    print("   A   B   C")
    print("           ")
    print(f"1  {board['A1']} | {board['B1']} | {board['C1']} ")
    print("  -----------")
    print(f"2  {board['A2']} | {board['B2']} | {board['C2']} ")
    print("  -----------")
    print(f"3  {board['A3']} | {board['B3']} | {board['C3']} ")
    print("           ")

def demande_coord(board, pion, coord_valides):
    while True:
        coord = input(f"Joueur {pion}: Entrer la coordonnée: ")
        if coord in coord_valides and board[coord] == " ":
            return coord

def resultat(etat):
    if etat["gagne"]:
        print("----------------------")
        print(f"--  BRAVO Joueur {etat['pion']}  --")
        print("----------------------")

        # Crée le dossier rsc/ s'il n'existe pas (sans erreur s'il existe déjà)
        os.makedirs("rsc", exist_ok=True)
        with open("./rsc/histo.txt", "a", encoding="utf-8") as f:
            f.write(f"Le {datetime.now().strftime('%d %m %Y à %H:%M:%S')} - victoire de Joueur {etat['pion']} \n")
    else:
        print("-------------------")
        print("--   EGALITE !   --")
        print("-------------------")
        with open("./rsc/histo.txt", "a", encoding="utf-8") as f:
            f.write(f" le {datetime.now().strftime('%d %m %Y à %H:%M:%S')} - Egalité\n")

def jouer_partie():
    etat = nouvelle_partie()
    affiche(etat["board"])
    while not etat["gagne"] and not etat["matchnul"]:
        coord = demande_coord(etat["board"], etat["pion"], COORDS_VALIDES)
        insert_pion(etat["board"], coord, etat["pion"])
        affiche(etat["board"])  
        etat["gagne"] = test_victoire(etat["board"], etat["pion"], COMBINAISONS_GAGNANTES)
        etat["matchnul"] = test_match_nul(etat["board"])
        if not etat["gagne"] and not etat["matchnul"]:
            etat["pion"] = "O" if etat["pion"] == "X" else "X"  
    return etat

# ------    Boucle de jeu.    ----------
while True:
    etat = jouer_partie()
    resultat(etat)
    reponse = input("**** Voulez-vous rejouer ? (O/N) ").strip().upper()
    if reponse != "O":
        break




