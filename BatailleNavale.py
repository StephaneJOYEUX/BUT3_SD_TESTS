"""
La classe BatailleNavale() contient le code de la partie à proprement parler.

Elle prend en input tous les paramètre d'initialisation de la partie configurés
dans le main.py avec l'appel des différentes précédentes classes, à savoir :
    - navires : Il s'agit d'un set d'instance de la classe Navire.
                Ces instances contiennent toute les informations nécessaire pour la classe Strategie.

    - instance_grille : Instance de la classe Grille. Elle permet l'affichage des strategies. Définie par défault à 10x10.

    - strategie_joueur1 : Une instance de la classe Strategie contenant les informations strategique du joueur 1.

    - strategie_joueur2 : Une instance de la classe Strategie contenant les informations strategique du joueur 2.

    - pseudo_j1 : Le pseudo du joueur 1.

    - pseudo_j2 : Le pseudo du joueur 2.

    - test : un booléen utile pour différencier une excution standard d'une execution dans un contxte de tests.


Methodes de classe :
    - navire_coule : Retourne un booléen - True, si le navire a coulé, False sinon.
                        On observe dans la grille s'il reste une trace du symbole du navire ou non
                        (d'où l'unicité des symbole pour chacun des navires en plus de l'argument de lisibilité).

    - tous_les_navires_ont_coule : Même chose avec l'ensemble des navires.

    - tir : Permet de tirer, en changeant le symbole dans la grille en fonction de la réussite ou non du tir :
                - 'X' : si touché.
                - '0' si raté.

    - ligne_tir : Méthode d'inputs pour la coordonnées en ligne du tir.

    - colonne_tir : Même chose en colonne.

    - play_joueur : Méthode qui définit le déroulement du tour d'un joueur. Appelée à chaque tour de chacun des joueurs.

    - play_ordinateur : Même chose lorsque le second joueur est un ordinateur. Cette méthode lui est alors réservée.

    - jeu : Methode principale : Elle appelle les autres méthodes en fonction du déroulement de la partie.
                                    Elle s'arrête lorsque'un joueur a gagné la partie.
"""

import os
import random
from copy import deepcopy
from Grille import Grille, afficher_couple_grilles
from Strategie import Strategie


class BatailleNavale:
    def __init__(self, navires: set, strategie_joueur1: Strategie, strategie_joueur2: Strategie,
                 instance_grille: Grille = Grille(10, 10), pseudo_j1: str = 'Ordinateur 1',
                 pseudo_j2: str = 'Ordinateur 2',
                 test: bool = False):

        self.navires = navires  # de la forme : {Navire}
        # répertoire de tout les navires de chacun des joueurs à placer sur la grille
        # Avec taille : la taille du navire sur la grille
        # Et symbole : sa lettre représentative dans la grille de jeu

        self.instance_grille = instance_grille
        self.instance_grille.create()
        self.modele_plateau = self.instance_grille.plateau
        # afficher_grille(self.modele_plateau)

        self.pseudo_j1 = pseudo_j1
        self.pseudo_j2 = pseudo_j2

        self.strategie_j1 = strategie_joueur1
        self.strategie_j2 = strategie_joueur2

        # Création des grilles d'attaque et de défense de chaque joueur
        # Se définit bien dans la classe BatailleNavale car ces grilles sont propres à la partie.
        # La fonction deepcopy permet de rendre les grilles indépendantes les unes des autres.
        self.grille_att_j1 = deepcopy(self.modele_plateau)

        self.grille_att_j2 = deepcopy(self.modele_plateau)

        self.grille_def_j1 = deepcopy(self.modele_plateau)

        self.grille_def_j2 = deepcopy(self.modele_plateau)

        # Placement des navires pour chacun des joueurs
        self.strategie_j1.placement_navires(self.grille_def_j1, self.strategie_j1.informations)
        self.strategie_j2.placement_navires(self.grille_def_j2, self.strategie_j2.informations)

        # Permet de gérer le cas où l'on se trouve dans le code de test ou non -> éviter les inputs
        if not test:
            # Activation de la boucle principale permettant de gérer le tour par tour.
            self.jeu()

    # Permet de vérifier si un bateau est coulé
    def navire_coule(self, initiale, grille):
        for ligne in grille:
            if initiale in ligne:
                return False
        return True

    # Fonction de vérification de la victoire
    # => tous les navires ont coulé.
    def tous_les_navires_ont_coule(self, grille):
        for navire in self.navires:
            if not self.navire_coule(navire.get_symbole(), grille):
                return False
        return True

    # Fonction de tir sur la grille adverse
    # Le parametre numJoueur est le numero du joueur attaquant.
    def tir(self, numJoueur, ligne, colonne) -> str:
        if numJoueur == 1:
            grille_subit_Attaque = self.grille_def_j2
            grille_d_Attaque = self.grille_att_j1
        else:
            grille_subit_Attaque = self.grille_def_j1
            grille_d_Attaque = self.grille_att_j2

        # modification du symbole si tir = raté
        if grille_subit_Attaque[ligne - 1][colonne - 1] == "-":
            grille_subit_Attaque[ligne - 1][colonne - 1] = "0"
            grille_d_Attaque[ligne - 1][colonne - 1] = "0"
            return "Raté"

        elif grille_subit_Attaque[ligne - 1][colonne - 1] == "X" or grille_subit_Attaque[ligne - 1][colonne - 1] == "0":
            print("Coordonnées déjà visées, tour au joueur adverse")
            return "Raté"

        # mdofocation du symbole si tir = touché
        else:
            initiale = grille_subit_Attaque[ligne - 1][colonne - 1]
            grille_subit_Attaque[ligne - 1][colonne - 1] = "X"
            grille_d_Attaque[ligne - 1][colonne - 1] = "X"
            if self.navire_coule(initiale, grille_subit_Attaque):
                print("Navire coulé !")
                return "Touché, Coulé"
            return "Touché"

    # Fonction d'input pour la fonction de tir
    # Choix du numéro de ligne
    def ligne_tir(self):
        ligne = 0
        while not (1 <= ligne <= len(self.modele_plateau)):
            try:
                ligne = int(input("Entrez le numéro de ligne: "))
                if not (1 <= ligne <= len(self.modele_plateau)):
                    raise ValueError
            except ValueError:
                print("Veuillez entrer un numéro valide.")
        return ligne

    # Fonction d'input pour la fonction de tir
    # Choix du numéro de ligne
    def colonne_tir(self):
        colonne = 0
        while not (1 <= colonne <= len(self.modele_plateau[1])):
            try:
                colonne = int(input("Entrez le numéro de colonne: "))
                if not (1 <= colonne <= len(self.modele_plateau[1])):
                    raise ValueError
            except ValueError:
                print("Veuillez entrer un numéro valide.")
        return colonne

    # On sort de la boucle dès que le joueur a raté son coup
    def play_joueur(self, numJoueur) -> bool:
        tour_joueur = True
        while tour_joueur:
            # changement de l'affichage en fonction du joueur.
            if numJoueur == 1:
                os.system('cls')
                input(f"Au tour du Joueur {self.pseudo_j1} (tapez 'entrer' pour continuer)\n")
                os.system('cls')
                print("Grille de jeu actuelle :")
                grille_adverse = self.grille_def_j2
                afficher_couple_grilles(self.grille_def_j1, self.grille_att_j1)
            else:
                os.system('cls')
                input(f"Au tour du Joueur {self.pseudo_j2} (tapez 'entrer' pour continuer)\n")
                os.system('cls')
                print("Grille de jeu actuelle :")
                grille_adverse = self.grille_def_j1
                afficher_couple_grilles(self.grille_def_j2, self.grille_att_j2)

            ligne = self.ligne_tir()
            colonne = self.colonne_tir()
            resultat = self.tir(numJoueur, ligne, colonne)
            print(resultat)

            if resultat == "Raté":
                tour_joueur = False
            elif resultat == "Touché":
                tour_joueur = True
            elif resultat == "Touché, Coulé":
                tour_joueur = True
                if self.tous_les_navires_ont_coule(grille_adverse):
                    return True

            input("tapez 'entrer' pour continuer")
            os.system('cls')
        return False

    # L'ordinateur joue alétoirement la manche en essayant de faire couler un navire:
    # On sort de la boucle dès qu'un navire est raté par l'ordinateur
    def play_ordinateur(self):
        tour_ordinateur = True
        while tour_ordinateur:
            # tir sur des coordonnées aléatoires
            ligne = random.randint(0, len(self.modele_plateau[0]))
            colonne = random.randint(0, len(self.modele_plateau[1]))
            grille_adverse = self.grille_def_j1

            resultat = self.tir(2, ligne, colonne)
            print(resultat)

            if resultat == "Raté":
                tour_ordinateur = False
            elif resultat == "Touché":
                tour_ordinateur = True
            elif resultat == "Touché, Coulé":
                tour_ordinateur = True
                if self.tous_les_navires_ont_coule(grille_adverse):
                    return True
        return False

    # Fonction principale qui permet d'appeler les fonction de tour à tour et de tir.
    # S'arrête quand la partie est remportée par un joueur ou par l'ordinateur.
    def jeu(self) -> bool:

        partie_en_cours = True

        # cas d'une partie contre l'ordinateur
        if self.pseudo_j2 == "_Ordinateur":
            while partie_en_cours:
                if self.play_joueur(1):
                    os.system('cls')
                    print("Victoire, vous avez gagné !")
                    input("Tapez 'entrer' pour quitter le jeu\n")
                    partie_en_cours = False
                    break

                if self.play_ordinateur():
                    os.system('cls')
                    print("Défaite, vous avez perdu.")
                    input("Tapez 'entrer' pour quitter le jeu\n")
                    partie_en_cours = False
                    break

        # cas d'une partie contre un autre joueur
        while partie_en_cours:
            if self.play_joueur(1):
                os.system('cls')
                print(f"Victoire du joueur: {self.pseudo_j1}")
                input("Tapez 'entrer' pour quitter le jeu\n")
                partie_en_cours = False
                break

            if self.play_joueur(2):
                os.system('cls')
                print(f"Victoire du joueur: {self.pseudo_j2}")
                input("Tapez 'entrer' pour quitter le jeu\n")
                partie_en_cours = False
                break

        return True
