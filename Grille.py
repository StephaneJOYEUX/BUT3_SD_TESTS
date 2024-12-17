class Grille():

    def __init__(self, nombre_lignes: int, nombre_colonnes: int):
        self.__nb_lignes = abs(nombre_lignes) if nombre_lignes != 0 else 1 #or if nombre_lignes >= 10 else 10
        self.__nb_colonnes = abs(nombre_colonnes) if nombre_colonnes != 0 else 1 #or if nombre_colonnes >= 10 else 10
        self.grille = []
        self.creation_grille_de_jeu()

    def get_nb_lignes(self):
        return self.__nb_lignes

    def get_nb_colonnes(self):
        return self.__nb_colonnes

    def creation_grille_de_jeu(self):
        self.grille = []
        for i in range(self.get_nb_lignes()):
            self.grille.append([])
            for j in range(self.get_nb_colonnes()):
                self.grille[i].append("-")
        return True

# Fonction d'affichage
def afficher_grille(grille):
    reslt = ""
    for ligne in grille:
        reslt += " ".join(ligne) + "\n"
        print(" ".join(ligne))
    print("")
    return reslt

def afficher_couple_grilles(grille1, grille2):
    reslt = "     Vos navires :                      Champ de tir :\n"
    print("     Vos navires :                      Champ de tir :")
    for index_ligne in range(max(len(grille1), len(grille2))):
        ligne1 = " ".join(grille1[index_ligne]) if index_ligne < len(grille1) else ""
        ligne2 = " ".join(grille2[index_ligne]) if index_ligne < len(grille2) else ""
        print(f"     {ligne1}                {ligne2}")
        reslt += f"{ligne1}                {ligne2}\n"
    return reslt
