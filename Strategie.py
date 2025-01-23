"""
La classe Strategie fait appel à Grille et navires et est appelée par la classe CreationStrategie().
Elle permet de définir le placement de tous les navires d'un joueur dans la grille rentrée en paramètre.
Pour être plus précis, elle donne les informations nécéssaires au placement de chacun des navires
dans les grilles de la partie.

Les inputs de cette classe sont :
    - inputs_strategie : Dataframe pandas contenant les information nécéssaire à la Strategie.

    - navires : Il s'agit d'un set d'instance de la classe Navire.
                Ces instances contiennent toute les informations nécessaire pour la classe Strategie.

    - grille : Instance de la classe Grille. Elle permet l'affichage des strategies. Définie par défault à 10x10.

    - complete (booleen) : Permet de savoir si une strategie est complete ou pas.
                            => utile pour tester la validité d'une strategie OU tester la plaçabilité des navires.*
                            => il est possible de tester la plaçabilité des navires d'une strategie non-complete (CreationStrategie).

Methodes de classes :
    - verifier_placabilite : permet de verifier que les navires sont plaçable dans la grille
                            (pas de collision, chevauchement, nombre de cases suffisant, ...)

    - verifier_correspondance_parametres_navires : permet de verifier que les navires du parametre : 'navires',
                                                    correspondent aux navires du parametre : 'inputs_strategie'

    - verifier_validite : permet de verifier qu'une strategie est valide selon différents critères
                            (en se servant notamment des 2 methodes précédentes).

    - placement_navires : permet de placer un les navires (symbole) dans la grille, à partir du df pandas : inputs_strategie

    - placement_navires : permet de placer tous les navires (symbole) dans la grille, à partir du df pandas : inputs_strategie
                            => utilise la méthode placement_un_navire

    - affichage_strategie : permet d'afficher la strategie en utlisant la fonction afficher_grille() du module Grille.py
"""
import pandas as pd

from Grille import Grille, afficher_grille
from Navire import Navire
from copy import deepcopy


class Strategie():

    # Getters
    def get_navires(self):
        return self._navires

    def get_informations(self):
        return self._informations

    def get_grille(self):
        return self._grille

    # Setters
    def set_navires(self, navires=None):
        # Il ne peut pas y avoir de Navire identiques du à la propriété ensembliste des sets en Python
        if navires is None:
            navires = self.navires
        # le nombre de navires dans les informations de la strategie rentrés en paramètre peut ne pas être forcement
        # égal au nombre de navires dans le set : navires
        if self.complete:
            self.verifier_correspondance_parametres_navires()

        self._navires = navires

    def set_informations(self, informations=None):
        if informations is None:
            informations = self.informations
        self._informations = informations

    def set_grille(self, grille=None):
        if grille is None:
            grille = self.grille
        self._grille = grille
        self._grille.create()
        self._plateau = self._grille.plateau

    # Constructeur
    def __init__(self, inputs_strategie: pd.DataFrame, navires: set, grille=Grille(10, 10), complete=True):
        # Variables privées
        self._grille: Grille
        self._navires: set
        self._infomations: pd.DataFrame

        # Variables publiques
        self.navires = navires
        self.informations = inputs_strategie
        self.grille = grille
        self.complete = complete

    # verification de la validité de la stratégie créée.
    # Il y a plusieurs règles à respecter pour qu'une stratégie soit valide :
    #   1. Aucun navire ne doit sortir de la grille : déjà réglé avec la fonction de création de stratégie
    #   2. Aucun navire ne doit en chevaucher un autre : à vérifier dans cette classe
    # La fonction doit renvoyer un booléen :
    #   True : pas de problème, le programme continue
    #   False : suppression du dernier placement et ressaisie des caractéristique à partir du navire qui pose problème.

    # Cette methode est directement appelée dans le code de création de la stratégie.
    # Elle nous permet, à chaque ajout de données dans l'objet strategie, de vérifier que ces données sont valides.
    def verifier_validite(self):
        self.verifier_correspondance_parametres_navires()

        # vérifions la correspondance entre les navires des informations de placement et les navires du set de paramètre.
        copy_set_navire = deepcopy(self._navires)

        for i in list(self._informations.index):
            for navire_set in self._navires:
                if self._informations.loc[i, "nom"] == navire_set.get_nom():
                    copy_set_navire.remove(navire_set)
        if len(copy_set_navire) != 0:
            return False

        return self.verifier_placabilite()

    # Permet de vérifier si un navire est plaçable dans le plateau ou non
    # methode utilisée lors de la création de strategie.
    def verifier_placabilite(self):
        # vérification que le navire est bien plaçable sur la grille
        if self.placement_navires(self._grille.get_plateau(), self.informations):
            return True
        else:
            return False

    def verifier_correspondance_parametres_navires(self):
        # Test de validité : nombre de navire égaux entre les différents paramètres d'initialisation.
        if len(self.navires) != len(self.informations):
            raise ValueError(
                "Strategie non valide !\nLe nombre de navires de la stratégie diffère du nombre de navires attendus dans le mode de jeu associé.")

    # Boucle sur tous les navire de la strategie et essaie de les placer dans la grille
    # retourne un booléen pour indiquer si les navires ont correctement été placés ou non
    def placement_navires(self, plateau, informations: pd.DataFrame):
        try:
            for i in list(informations.index):
                informations_navires = informations.loc[i]
                # print(informations_navires)
                if not self.placement_un_navire(plateau, informations_navires):
                    # Ré-itialisation du plateau
                    self._plateau = self._grille.reinit_plateau()
                    return False
            return True
        except:
            return False

    # Fonction permettant de placer un navire sur la grille
    # retourne un booléen pour indiquer si le navire a correctement été placé ou non
    def placement_un_navire(self, plateau, informations_navire):
        # définition des variables propres au placement d'un navire
        taille_navire = informations_navire.loc["taille"]

        # Pour les coordonnées, il faut retirer 1 afin d'être en raccord avec l'idexation de la grille.
        # Il est plus simple de modifier ça ici qu'avant car avant, l'information est accessible par les joueurs et ce '-1'
        # n'est pas compréhensible pour tous
        coord_ligne = informations_navire.loc["coord_x"] - 1
        coord_colonne = informations_navire.loc["coord_y"] - 1
        orientation = informations_navire.loc["orientation"]

        # variable associée au navire :
        navire: None | Navire = None
        for navire_set in self.navires:
            if navire_set.get_nom() == informations_navire.loc["nom"]:
                navire = navire_set
                break

        # Cette boucle permet d'ajouter l'ensemble du navire à la grille si la taille du navire est >1.
        while taille_navire != 0:
            # Modification du symbole dans le plateau de la grille.
            if plateau[coord_ligne][coord_colonne] == '-' or plateau[coord_ligne][
                coord_colonne] == navire.get_symbole():
                plateau[coord_ligne][coord_colonne] = navire.get_symbole()
                taille_navire -= 1
            else:

                return False

            if orientation == 'N':
                coord_ligne -= 1
            elif orientation == 'S':
                coord_ligne += 1
            elif orientation == 'E':
                coord_colonne += 1
            else:
                coord_colonne -= 1

        return True

    # Méthode pour afficher la stratégie
    def affichage_strategie(self):
        if self.complete:
            critere_bool = self.verifier_validite()
        else:
            critere_bool = self.verifier_placabilite()

        if critere_bool:
            afficher_grille(self.grille.plateau)
            return True
        else:
            print('Stratégie non valide !')
            return False

    # redefinition de l'operateur d'egalité pour la classe Strategie.
    def __eq__(self, other):
        try:
            if self._informations == other._informations:
                return True
        except:
            print('Vous ne comparez pas 2 instances de la classe Strategie')


class FactoryStrategie():
    def get_strategie(self):
        return self.strategie

    def __init__(self, inputs_strategie: pd.DataFrame, navires: set, grille=Grille(10, 10), complete=True):
        # intialisation de la classe Strategie
        self.strategie = Strategie(inputs_strategie, navires, grille, complete)
        self.strategie.set_navires(self.strategie.navires)
        self.strategie.set_informations(self.strategie.informations)
        self.strategie.set_grille(self.strategie.grille)

        if complete:
            self.strategie.verifier_validite()
        else:
            self.strategie.verifier_placabilite()
