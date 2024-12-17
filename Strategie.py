"""
La classe Strategie fait appel à Grille et navires et est appelée par la classe CreationStrategie().
Elle permet de définir le placement de tous les navires d'un joueur dans la grille rentrée en paramètre.
Pour être plus précis, elle donne les informations nécéssaires au placement de chacun des navires
dans les grilles de la partie.

Les inputs de cette classe sont :
  - inputs_strategie :  Dictionnaire contenant les information nécéssaire à la Strategie.
                        C'est la strategie du joueur à proprement parler.

  - navires :   Dictionnaire contenant les informations des navires relatifs à la partie.
                Utile notamment pour l'affichage des stratégies dans la grille.
                Nous avons besion du symbole du navire dans la grille qui est contenu dans ce dictionnaire.

  - Grille :    Instance de la classe Grille. Elle permet l'affichage des strategies. Définie par défault à 10x10.


Tests : (à programmer et automatiser)
    La fonction la plus importante à tester ici est la fonction verifier_validite(). -> testable facilement
    Une autre fonction intérressante à tester est le getter de la grille de la stratégie. (pas encore programmée)

    Il est aussi tout à fait possible de tester les autres fonctions de la classe.
"""

from Grille import Grille, afficher_grille
from copy import deepcopy


class Strategie():
    def __init__(self, inputs_strategie : dict, navires : dict,  Grille = Grille(10,10)):
        self.navires = navires

        self.instance_grille = Grille
        self.instance_grille.creation_grille_de_jeu()

        self.informations = inputs_strategie
        self.verifier_validite()


    # verification de la validité de la stratégie créée.
    # Il y a plusieurs règles à respecter pour qu'une stratégie soit valide :
    #   1. Aucun navire ne doit sortir de la grille : déjà réglé avec la fonction de création de stratégie
    #   2. Aucun navire ne doit en chevaucher un autre : à vérifier ici
    # La fonction doit renvoyer un booléen :
    #   True : pas de problème, le programme continue
    #   False : suppression du dernier placement et ressaisie des caractéristique à partir du navire qui pose problème.

    # Cette fonction est directement intégrée dans le code de création de la stratégie.
    # Elle nous permet, à chaque ajout de données dans l'objet strategie, de vérifier que ces données sont valides.
    # Du point de vue des tests, il pourrait être intérressant de tester plusieurs scénarios de validité.
    def verifier_validite(self):
        # à modifier, on ne vas pas afficher le message de validation a chaque itération de la boucle dans créer stratégie...
        if self.placement_navires_joueur(self.instance_grille.grille, self.informations):
            return True
        else :
            return False


    # boucle sur tous les navire de la strategie et essaie de les placer dans la grille
    # retourne un booléen pour indiquer si les navires ont correctement été placés ou non
    def placement_navires_joueur(self, grille, strategie):
        try :
            for navire in strategie.keys():
                if not self.placement_un_navire(grille, strategie, navire) :
                    return False
            return True
        except :
            return False


    # fonction permettant de placer un navire sur la grille
    # retourne un booléen pour indiquer si le navire a correctement été placé ou non
    def placement_un_navire(self, grille, strategie, navire):
        # définition des variables propres au placement d'un navire
        taille_navire = strategie[navire][0]

        # Pour les coordonnées, il faut retirer 1 afin d'être en raccord avec l'idexation de la grille.
        # Il est plus simple de modifier ça ici qu'avant car avant, l'information est accessible par les joueurs et ce '-1'
        # n'est pas compréhensible pour tous
        coord_ligne = strategie[navire][1]-1
        coord_colonne = strategie[navire][2]-1
        sens = strategie[navire][3]

        if grille[coord_ligne][coord_colonne] == '-' or grille[coord_ligne][coord_colonne] == self.navires[navire][1] :
            grille[coord_ligne][coord_colonne] = self.navires[navire][1]
            taille_navire -= 1
        else :
            return False

        # Cette boucle permet d'ajouter l'ensemble du navire à la grille si la taille du navire est >1.
        while taille_navire != 0 :
            if sens == 'N':
                coord_ligne -= 1
            elif sens == 'S':
                coord_ligne += 1
            elif sens == 'E':
                coord_colonne += 1
            else :
                coord_colonne -= 1

            if grille[coord_ligne][coord_colonne] == '-' or grille[coord_ligne][coord_colonne] == self.navires[navire][1]:
                grille[coord_ligne][coord_colonne] = self.navires[navire][1]
                taille_navire -= 1
            else:
                return False
        return True


    # Méthode pour afficher la stratégie
    def affichage_strategie(self):
        if self.verifier_validite() :
            afficher_grille(self.instance_grille.grille)
        else:
            print('Stratégie non valide !')

    def __eq__(self, other):
        try :
            if self.informations == other.informations :
                return True
        except :
            print('Vous ne comparez pas 2 instances de la classe Strategie')
