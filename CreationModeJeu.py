from ModeJeu import FactoryModeJeu
from ModeJeu import ModeJeu, FactoryModeJeu
from Grille import Grille

class CreationModeJeu() :
    # Getters
    def get_nom(self):
        return self._nom


    # Setters
    def set_nom(self, nom = None):
        if nom is None :
            nom = self.nom
        self._nom = nom


    # Constructeur
    def __init__(self, nom:str):
        self.nom = nom

        self.mode_jeu : ModeJeu


    # inputs concernant la grille
    def input_taille_grille(self):
        choix_grille_valide = False

        while not choix_grille_valide :
            print("Veillez définir la taille de la grille")
            # Assertion sur les choix de l'utilisateur
            nb_lignes = int(input("Indiquez le nombre de lignes : "))
            nb_colonnes = int(input("Indiquez le nombre de colonnes : "))
            try :
                grille_test = Grille(nombre_lignes=nb_lignes, nombre_colonnes=nb_colonnes)
                grille_test.create()
                choix_grille_valide = True
            except ValueError as current_error :
                current_error = str(current_error)
                # utiliser les regexp pour trouver les mots lignes / colonnes dans le str d'erreur +
                # gerer cas d'erreur ou la valeur rentrée en saisie est la mauvaise
                if current_error == "" :
                    pass


        # Nombre de navires
        choix_nb_navires_valide = False
        taille_min_navire = 2

        while not choix_nb_navires_valide :
            try :
                nb_navires = int(input("Combien de navires souhaitez-vous dans ce mode de jeu ?\n"))



                # revoir le critère de validite : depend aussi (et surtout de la taille des navires)
                critere_validite = nb_navires*taille_min_navire/(nb_lignes*nb_colonnes)
                if critere_validite < 0.6 :
                    choix_nb_navires_valide = True
                else :
                    print("Ce mode de jeu n'est pas valide !")
                    print("Le nombre de navires est trop important pour une grille de cette taille !")
            except ValueError :
                pass


            # Appel de la méthode de classe pour chacun des navires.
            # vérification à chaque itération de la validité du mode de jeu avec la méthode de classe de verification
            # de validite de la classe : ModeJeu.
            for i in range(1, nb_navires):
                self.inputs_navires()




    # Appel de cette méthode pour chacun des navires
    # Demande du nom du navire -> attention pour les symbole les noms doivent avoir des initiales différentes.
    # Demande de la taille -> appliquer une fonction de vérification des critères de validité.
    def inputs_navires(self):
        pass


class FactoryCreationModeJeu():
    def __init__(self, nom:str):
        self.creation_mode_jeu = CreationModeJeu(nom=nom)