"""
La classe BatailleNavale() contient le code de la partie à proprement parler.

Elle prend en input tous les paramètre d'initialisation de la partie configurés
dans le main.py avec l'appel des différentes précédentes classes.

Les tests sont ici d'une importance majeure.

Remarque :
    Afin de pouvoir automatiser la partie dans l'idée d'un scénario de test,
    il faudrait créer de fonction lorsqu'un joueur joue.
    La première contiendrait les inputs et serait utilisée comme 'masque' de la 2nd.
    La seconde contiendrait le code permettant de tirer aux coordonnées choisies.

    Ainsi, en automatisant, on utilise pas la fonction d'input, mais on choisit pour chaque joueur,
    à chaque tour, les coordonnées de tir.

    A voir.
"""

import random
from copy import deepcopy
from Grille import Grille, afficher_grille, afficher_couple_grilles
from Strategie import Strategie

# Declariation et initialisation des variables utilisées dans la classe :
class BatailleNavale:
    def __init__(self, navires, strategie_joueur1 : Strategie, strategie_joueur2 :Strategie, instance_grille = Grille(10, 10) , pseudo_j1 : str ='Ordinateur 1' ,  pseudo_j2 : str='Ordinateur 2', test : bool = False):

        self.navires = navires  # de la forme : {nom : [taille, symbole]}
        # répertoire de tout les navires de chacun des joueurs à placer sur la grille
        # Avec taille : la taille du navire sur la grille
        # Et symbole : sa lettre représentative dans la grille de jeu


        self.modele_grille_de_jeu = instance_grille.plateau

        self.pseudo_j1 = pseudo_j1
        self.pseudo_j2 = pseudo_j2

        # La methode instanciation strategie n'est peut etre pas utile ici
        # A voir avec des test : l'important est que les self.strategie soit des instance de la classe Strategie().
        self.strategie_j1 = self.instansiation_strategie(strategie_joueur1)
        self.strategie_j2 = self.instansiation_strategie(strategie_joueur2)


        # Création des grilles d'attaque et de défense de chaque joueur
        # Se définit bien dans la classe BatailleNavale car ces grilles sont propres à la partie.
        # La fonction deepcopy permet de rendre les grilles indépendantes les unes des autres.
        self.grille_att_j1 = deepcopy(self.modele_grille_de_jeu)

        self.grille_att_j2 = deepcopy(self.modele_grille_de_jeu)

        self.grille_def_j1 = deepcopy(self.modele_grille_de_jeu)

        self.grille_def_j2 = deepcopy(self.modele_grille_de_jeu)



        # Placement des navires pour chacun des joueurs

        self.strategie_j1.placement_navires_joueur(self.grille_def_j1, self.strategie_j1.informations)
        self.strategie_j2.placement_navires_joueur(self.grille_def_j2, self.strategie_j2.informations)


        # Permet de gérer le cas où l'on se trouve dans le code de test ou non -> viter les inputs
        if not test :
            # Code optionel :
            print(f"{self.pseudo_j1}, voici vos grilles :\n")
            afficher_couple_grilles(self.grille_def_j1, self.grille_att_j1)

            print('-----')

            print(f"{self.pseudo_j2}, voici vos grilles :\n")
            afficher_couple_grilles(self.grille_def_j2, self.grille_att_j2)

            # Activation de la boucle principale permettant de gerer le tour par tour.
            self.jeu()



    # Règlage du problème du 'niveau' différent entre les classes Strategie() et CreationStrategie().
    # Fonction peut etre inutile -> a verifier avec les tests
    def instansiation_strategie(self, input_strategie_joueur):
        # Pour résoudre le problème, on applique une méthode propre à la classe Strategie,
        # S'il y a une erreur, on sait qu'il faut changer d'objet :
        # mettre CreationStrategie.instance_strategie qui une instance de la classe Strategie().
        try :
            strategie_joueur = input_strategie_joueur
            grille_test = deepcopy(self.modele_grille_de_jeu)
            strategie_joueur.placement_navires_joueur(grille_test, strategie_joueur.informations)
        except :
            print(input_strategie_joueur.instance_strategie)
            strategie_joueur = input_strategie_joueur.instance_strategie
        return strategie_joueur


    # Permet de vérifier si un bateau est coulé
    def navire_coule(self,initiale, grille):
        for ligne in grille:
            if initiale in ligne:
                return False   
        return True


    # Fonction de vérification de la victoire
    def tous_les_navires_ont_coule(self,grille):
        for navire in self.navires.values():
                if not self.navire_coule(navire[1],grille):
                    return False
        return True


    # Fonction de tir sur la grille adverse
    # Le parametre numJoueur est le numero du joueur attaquant.
    def tir (self,numJoueur,ligne, colonne) -> str:
        if numJoueur == 1:
            grille_subit_Attaque =  self.grille_def_j2
            grille_d_Attaque = self.grille_att_j1
        else:
            grille_subit_Attaque =  self.grille_def_j1
            grille_d_Attaque = self.grille_att_j2
    
        if grille_subit_Attaque[ligne-1][colonne-1] == "-":
            grille_subit_Attaque[ligne-1][colonne-1] = "0"
            grille_d_Attaque[ligne-1][colonne-1] = "0"
            return "Raté"

        elif grille_subit_Attaque[ligne-1][colonne-1] == "X" or grille_subit_Attaque[ligne-1][colonne-1] == "0" :
            print("Coordonnées déjà visées, tour au joueur adverse")
            return "Raté"
                        
        else:
            
            initiale = grille_subit_Attaque[ligne-1][colonne-1]
            grille_subit_Attaque[ligne-1][colonne-1] = "X"
            grille_d_Attaque[ligne-1][colonne-1] = "X"
            if self.navire_coule(initiale,grille_subit_Attaque):
                print("Navire coulé !")
                return "Touché, Coulé"
            return "Touché"


    # Fonctioon d'input pour la fonction de tir
    # Choix du numéro de ligne
    def ligne_tir(self):
        ligne = 0
        while not (1 <= ligne  <= len(self.modele_grille_de_jeu)):
                    try:
                        ligne = int(input("Entrez le numéro de ligne: "))
                    except ValueError:
                        print("Veuillez entrer un numéro valide.")
        return ligne


    # Fonctioon d'input pour la fonction de tir
    # Choix du numéro de ligne
    def colonne_tir(self):
        colonne = 0
        while not (1 <= colonne  <= len(self.modele_grille_de_jeu[1])):
                    try:
                        colonne = int(input("Entrez le numéro de colonne: "))
                    except ValueError:
                        print("Veuillez entrer un numéro valide.")
        return colonne       


    
    #Le joueur doit choisir un numéro de ligne et un numéro de colonne pour essayer de toucher un navire:
    #On sort de la boucle dès que le joueur a raté son coup
    def play_joueur(self,numJoueur)-> bool:
            tour_joueur= True
            while tour_joueur:
                
                if numJoueur == 1:
                    print(f"Au tour du Joueur {self.pseudo_j1}")
                    print("Grille de jeu actuelle :")
                    grille_adverse = self.grille_def_j2
                    afficher_couple_grilles(self.grille_def_j1, self.grille_att_j1)
                else:
                    print(f"Au tour du Joueur {self.pseudo_j2}")
                    print("Grille de jeu actuelle :")
                    grille_adverse = self.grille_def_j1
                    afficher_couple_grilles(self.grille_def_j2, self.grille_att_j2)

                ligne = self.ligne_tir()
                colonne = self.colonne_tir()
                resultat= self.tir(numJoueur,ligne,colonne)
                print(resultat)

                if resultat == "Raté":
                     tour_joueur = False
                elif resultat == "Touché" :
                     tour_joueur = True
                elif resultat == "Touché, Coulé" :
                    tour_joueur = True
                    if self.tous_les_navires_ont_coule(grille_adverse) :
                        return True
            return False


    #L'ordinateur joue alétoirement la manche en essayant de faire couler un navire:
    #On sort de la boucle dès qu'un navire est raté par l'ordinateur
    def play_ordinateur(self):
            tour_ordinateur = True
            while tour_ordinateur:
    
                ligne = random.randint(0, len(self.modele_grille_de_jeu[0]))
                colonne = random.randint(0, len(self.modele_grille_de_jeu[1]))
                grille_adverse = self.grille_def_j1

                resultat= self.tir(2,ligne,colonne)
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
    def jeu(self)-> bool:

        partie_en_cours = True
        
        if self.pseudo_j2 == "_Ordinateur":
            while partie_en_cours :

                if self.play_joueur(1):
                    print ("Victoire, vous avez gagné !")
                    partie_en_cours = False

                if self.play_ordinateur():
                    print("Défaite, vous avez perdu.")
                    partie_en_cours = False

        while partie_en_cours :

            if self.play_joueur(1):
                print(f"Victoire du joueur: {self.pseudo_j1}")
                partie_en_cours = False

            if self.play_joueur(2):
                print(f"Victoire du joueur: {self.pseudo_j2}")
                partie_en_cours = False

        return True
