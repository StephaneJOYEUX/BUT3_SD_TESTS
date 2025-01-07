'''
La classe de CreationStrategie() est appelée par la classe ChoixStrategie() et appelle la classe Strategie().
Elle permet de créer une nouvelle stratégie valide en demandant les inputs nécessaires à l'utilisateur.
ATTENTION : beaucoup d'inputs !


Remarques :
    (Optionel ?)
    Créer une getter pour récupérer la stratégie crée hors de la classe (utile notamment pour la classe ChoixStrategie()).

    Peut-être testable ? (difficile car beaucoup d'input)
    Pour tester cette classe, regarder les modules py comme PyAutoGUI ou keyboard
    -> pas très utiles... ou trop dur à apprendre à utiliser en 1 sem.

    Les test se font surtout au niveau de la classe Strategie.
'''
from Grille import Grille, afficher_grille
from copy import deepcopy
from Strategie import Strategie, FactoryStrategie


class CreationStrategie():
    def __init__(self, navires : dict,Grille = Grille(10,10), test : bool = False):
        self.navires = navires

        self.grille = Grille
        self.grille.create()

        self.premiere_ligne_grille = 1
        self.derniere_ligne_grille = self.grille.get_nb_lignes()
        self.premiere_colonne_grille = 1
        self.derniere_colonne_grille = self.grille.get_nb_colonne()

        self.inputs_strategie = {}

        if not test :
            self.creer_strategie()
        else :
            self.instance_strategie = Strategie({'Torpilleur': [2, 4, 9, 'O'], 'Sous-marin': [3, 3, 6, 'S'], 'Frégate': [3, 6, 9, 'S'],
                              'Cuirassé': [4, 9, 1, 'E'], 'Porte-avions': [5, 10, 7, 'N']}, self.navires,
                                 Grille)


    # Fonction principale : elle permet la création de l'objet strategie : {nom : [taille, coord_x, coord_y, sens]}
    # Cet objet strategie reuni les placement de tous les navires dans la grille.
    # Il faut bien sur que la strategie soit valide après sa création sinon cela n'aurait aucun sens.
    # Par 'valide' il faut entendre que la stratégie respecte les règles du jeu.
    def creer_strategie(self):
        print('Pour chacun des navires, vous devez choisir ses coordonnées en ligne, en colonne, '
              'et son orientation (Nord, Est, Sud, Ouest).')
        print("")

        coord_ligne : int
        coord_colonne :int
        sens : str
        taille :int

        # il faut boucler sur tous les navires du référentiel
        # on ne peut pas choisir de ne pas placer un navire, c'est impossible !
        for navire in self.navires.keys() :


            self.inputs_strategie [f'{navire}'] = self.input_donnees_placement_navire(navire)
            self.instance_strategie = FactoryStrategie(self.inputs_strategie,self.navires).strategie



            while not self.instance_strategie.verifier_validite() :
                print('Stratégie invalide !!!')
                print('Vous devez re-saisir les caractéristiques du dernier navire.')
                self.inputs_strategie [f'{navire}'] = self.input_donnees_placement_navire(navire)
                # initialisation de l'instance de la classe Strategie
                self.instance_strategie = FactoryStrategie(self.inputs_strategie,self.navires)



            print("Voici votre strategie actuelle :\n")
            self.instance_strategie.affichage_strategie()

        # A modifier
        return self.instance_strategie



    # Fonction Absolument nécéssaire pour la création des placements des navires.
    # Il s'agit principalement d'une fonction d'input avec beaucoup de condition sur le placement des navires.
    # Le but est de poser un cadre au placement des navires afin que les navires puisse être représentés dans la grille ensuite.
    def input_donnees_placement_navire(self, navire):
        taille = self.navires[navire][0]

        print(f'Choisissez les caractéritiques du navire suivant : {navire}.')
        coord_valides = False

        while not coord_valides:
            coord_ligne = input('Numéro de ligne : ')
            coord_colonne = input('Numéro de colonne : ')

            try:
                coord_ligne = int(coord_ligne)
                coord_colonne = int(coord_colonne)
                if coord_ligne <= self.derniere_ligne_grille and coord_ligne >= self.premiere_ligne_grille:
                    if coord_colonne <= self.derniere_colonne_grille and coord_colonne >= self.premiere_colonne_grille:
                        coord_valides = True
                    else:
                        print("Les coordonnées doivent être des nombres compris entre 1 et 10")
                else:
                    print("Les coordonnées doivent être des nombres compris entre 1 et 10")

            except:
                print("Veuillez rentrer un nombre !")

        # Gestion des cas en bord de grille + les coins
        sens_valide = False

        while not sens_valide:

            # La condition de validité du sens du navire dépend de la taille de ce dernier,
            # Exemple : un navire de taille 4 peut se positionner sur la 3ème ligne,
            # mais il ne peut dans ce cas pas s'orienter vers le nord !
            if coord_ligne < self.navires[navire][0]:
                # Coin supérieur gauche
                if coord_colonne < self.navires[navire][0]:
                    sens = input("Choisissez l'orientation du navire : (E/S)\n")
                    sens = sens.upper()
                    if sens == 'E' or sens == 'S':
                        sens_valide = True
                    else:
                        print('Orientation du navire non valide.')

                # Coin supérieur droit
                elif coord_colonne + self.navires[navire][0] > self.derniere_colonne_grille+1:
                    sens = input("Choisissez l'orientation du navire : (S/O)\n")
                    sens = sens.upper()
                    if sens == 'S' or sens == 'O':
                        sens_valide = True
                    else:
                        print('Orientation du navire non valide.')

                # Première ligne sans les coins
                else:
                    sens = input("Choisissez l'orientation du navire : (E/S/O)\n")
                    sens = sens.upper()
                    if sens == 'S' or sens == 'O' or sens == 'E':
                        sens_valide = True
                    else:
                        print('Orientation du navire non valide.')

            # Dernière ligne
            elif coord_ligne + self.navires[navire][0] > self.derniere_ligne_grille+1:
                # Coin inférieur gauche
                if coord_colonne < self.navires[navire][0]:
                    sens = input("Choisissez l'orientation du navire : (E/N)\n")
                    sens = sens.upper()
                    if sens == 'E' or sens == 'N':
                        sens_valide = True
                    else:
                        print('Orientation du navire non valide.')

                # Coin inférieur droit
                elif coord_colonne + self.navires[navire][0] > self.derniere_colonne_grille+1:
                    sens = input("Choisissez l'orientation du navire : (N/O)\n")
                    sens = sens.upper()
                    if sens == 'N' or sens == 'O':
                        sens_valide = True
                    else:
                        print('Orientation du navire non valide.')

                # Dernière ligne sans les coins
                else:
                    sens = input("Choisissez l'orientation du navire : (E/N/O)\n")
                    sens = sens.upper()
                    if sens == 'N' or sens == 'O' or sens == 'E':
                        sens_valide = True
                    else:
                        print('Orientation du navire non valide.')


            # Cas des lignes générales
            else:
                # Première colonne sans les coins
                if coord_colonne < self.navires[navire][0]:
                    sens = input("Choisissez l'orientation du navire : (E/N/S)\n")
                    sens = sens.upper()
                    if sens == 'E' or sens == 'S' or sens == 'N':
                        sens_valide = True
                    else:
                        print('Orientation du navire non valide.')

                # Dernière colonne sans les coins
                elif coord_colonne + self.navires[navire][0] > self.derniere_colonne_grille+1:
                    sens = input("Choisissez l'orientation du navire : (N/O/S)\n")
                    sens = sens.upper()
                    if sens == 'S' or sens == 'O' or sens == 'N':
                        sens_valide = True
                    else:
                        print('Orientation du navire non valide.')

                # Cas général
                else:
                    sens = input("Choisissez l'orientation du navire : (N/E/S/O)\n")
                    sens = sens.upper()
                    if sens == 'E' or sens == 'S' or sens == 'O' or sens == 'N':
                        sens_valide = True
                    else:
                        print('Orientation du navire non valide.')

        print("")
        return [taille, coord_ligne, coord_colonne, sens]


    def get_instance_strategie(self) :
        return self.instance_strategie

