from ModeJeu import FactoryModeJeu
from ModeJeu import ModeJeu, FactoryModeJeu
from Grille import Grille, afficher_grille
from Navire import FactoryNavire
import os
import pandas as pd


class CreationModeJeu():
    # Getters
    def get_nom(self):
        return self._nom

    def get_mode_jeu(self):
        return self._mode_jeu

    def get_navires(self):
        return self._navires

    def get_grille(self):
        return self._grille

    # Setters
    def set_nom(self, nom=None):
        if nom is None:
            nom = self.nom
        self._nom = nom

    def set_mode_jeu(self, mode_jeu: ModeJeu):
        self._mode_jeu = mode_jeu

    def set_navires(self, navires: set):
        self._navires = navires

    def set_grille(self, taille_grille: list):
        try :
            self._grille = Grille(taille_grille[0], taille_grille[1])
            self._grille.create()
        except :
            self._grille = None

    # Constructeur
    def __init__(self, nom: str):
        self.nom = nom
        self.navires: set = set()

        self._mode_jeu: ModeJeu

    # inputs concernant la grille
    def main(self):
        choix_grille_valide = False

        while not choix_grille_valide:
            print("\nVeillez définir la taille de la grille")
            # Assertion sur les choix de l'utilisateur
            try:
                nb_lignes = int(input("Indiquez le nombre de lignes : "))
                nb_colonnes = int(input("Indiquez le nombre de colonnes : "))
                grille_test = Grille(nombre_lignes=nb_lignes, nombre_colonnes=nb_colonnes)
                grille_test.create()
                taille_grille = [nb_lignes, nb_colonnes]
                choix_grille_valide = True
            except ValueError as current_error:
                if str(current_error)[0:39] == 'invalid literal for int() with base 10:':
                    print("Vous devez saisir des nombres entiers pour le nombre de lignes et de colonnes !")

        # Nombre de navires
        choix_nb_navires_valide = False
        taille_min_navire = 2

        while not choix_nb_navires_valide:
            try:
                nb_navires = int(input("\nCombien de navires souhaitez-vous dans ce mode de jeu ?\n"))

                # revoir le critère de validite : depend aussi (et surtout de la taille des navires)
                critere_validite = nb_navires * taille_min_navire / (nb_lignes * nb_colonnes)
                if critere_validite < 0.6:
                    choix_nb_navires_valide = True
                else:
                    print("Ce mode de jeu n'est pas valide !")
                    print("Le nombre de navires est trop important pour une grille de cette taille !")
            except ValueError:
                pass

        # Appel de la méthode de classe pour chacun des navires.
        # vérification à chaque itération de la validité du mode de jeu avec la méthode de classe de verification
        # de validite de la classe : ModeJeu.
        print("\nVous devez maintenant définir les caractéristiques de chacun de vos navires.")
        input("Tapez 'entrer' pour continuer.\n")
        
        caracteristique_valide = False
        while not caracteristique_valide:
            for i in range(nb_navires):
                inputs_navire_valide = False

                while not inputs_navire_valide:
                    os.system('cls')
                    print("Caractéritiques de la grille :")
                    print(f"Nombre de lignes : {nb_lignes}")
                    print(f"Nombre de lignes : {nb_colonnes}")
                    print('')
                    print(f'Il reste encore {nb_navires - i} navires dont les caractéristiques sont à définir.\n')

                    if len(self.navires) > 0:
                        print("Voici la liste de vos navires créés actuellement :")
                        self.afficher_navires(self.navires)
                        print("")

                    print(f"\nDéfinissez les caractéristiques du navire n°{i + 1}")
                    navire = self.inputs_navire(taille_grille)

                    self.navires.add(navire)
                    mode_jeu = FactoryModeJeu(nom=self.nom, navires=self.navires,
                                              taille_grille=taille_grille).get_mode_jeu()

                    critere_validite = mode_jeu.verifier_validiter_navires()
                    if critere_validite[0]:
                        inputs_navire_valide = True
                        caracteristique_valide = True
                        break

                    # critères de validités non-valides.
                    input("Tapez 'entrer' pour continuer.\n")
                    self.navires.remove(navire)

                    if critere_validite[1] == 2:
                        caracteristique_valide = False
                        break

                if not caracteristique_valide:
                    self.navires = set()
                    break

        # On appelle les setters afin de paramétrer correctement les informations du mode de jeu.
        self.set_mode_jeu(mode_jeu)
        self.set_navires(self.navires)
        self.set_grille(taille_grille)

    # Appel de cette méthode pour chacun des navires
    # Demande du nom du navire -> attention pour les symbole les noms doivent avoir des initiales différentes.
    # Demande de la taille -> appliquer une fonction de vérification des critères de validité.
    def inputs_navire(self, taille_grille: list):
        # 1. Demande de la longueur du navire : assertion sur les critère de validité du mode de jeu (classe ModeJeu).
        choix_taille_valide = False

        while not choix_taille_valide:
            try:
                choix_taille = int(input("\nChoisissez la taille du navire :\n"))
                if choix_taille > max(taille_grille):
                    raise ValueError("La taille saisie est supérieure à la taille maximale des lignes et colonnes !")

                # on essaye de construire une instance de la classe Navire avec l'input de l'utlisateur
                # => soumission au tests de validité de la taille
                FactoryNavire(nom='test', taille=choix_taille)
                choix_taille_valide = True
            except ValueError as current_error:
                if str(current_error)[0:39] == "invalid literal for int() with base 10:":
                    print('\nLa taille saisie doit être un nombre entier !\n')
                else:
                    print(str(current_error) + "\n")

        # 2. Demande du nom
        #       passage du nom en minuscule, sans espace (' ' => '-')
        choix_nom_symbole_valide = False

        while not choix_nom_symbole_valide:
            choix_nom_valide = False

            while not choix_nom_valide:
                try:
                    choix_nom = input("\nChoisissez un nom au navire :\n")
                    if len(choix_nom) < 4:
                        raise ValueError("Le nom est trop court !")
                    # passage en minuscule
                    choix_nom = choix_nom.lower()
                    # remplacement des espaces par des tirets
                    choix_nom = choix_nom.replace(' ', '-')
                    # verification que le nom ne soit pas le même que celui d'un autre navire déjà présent de ce mode de jeu
                    for navire in self.navires:
                        if navire.get_nom() == choix_nom:
                            raise ValueError("Un navire avec un nom similaire existe déjà dans ce mode de jeu !\n")
                    choix_nom_valide = True
                except ValueError as current_error:
                    print(str(current_error))

            # 3. Extraction du symbole : premiere lettre du nom
            #       Si pas de symbole similaire dans la liste de navires => tout va bien on continue le code,
            #       Sinon : soit l'utlisateur change le nom du navire, soit il saisi un symbole mannuellement pour ce navire.
            #       Nt : les symboles sont des lettres majuscules, chaine de caractères de longueur 1.
            try:
                choix_symbole = choix_nom[0]
                choix_symbole = choix_symbole.upper()
                # vérifier que le symbole n'est pas déjà utilisé par les navires déjà créé dans ce mode de jeu.
                for navire in self.navires:
                    if navire.get_symbole() == choix_symbole:
                        raise ValueError("Le symbole existe déjà !")
                choix_nom_symbole_valide = True
            except ValueError as current_error:
                # Affichage de l'erreur pour que l'utilisateur comprenne bien.
                print(str(current_error))

                choix_utilisateur_symbole_valide = False

                while not choix_utilisateur_symbole_valide:
                    choix_utilisateur_symbole = input(
                        "Voulez vous choisir un symbole pour le navire ou changer le nom du navire ? (choisir/changer)\n")
                    try:
                        assert choix_utilisateur_symbole == "choisir" or choix_utilisateur_symbole == "changer"
                        choix_utilisateur_symbole_valide = True
                    except AssertionError:
                        print("Saisie invalide !")
                        print("Veuillez choisir l'un des choix proposé !\n")

                if choix_utilisateur_symbole == "changer":
                    choix_nom_symbole_valide = False
                elif choix_utilisateur_symbole == "choisir":
                    choix_symbole_valide = False
                    while not choix_symbole_valide:
                        choix_symbole = input(f"Choisissez le symbole associé au navire : {choix_nom}\n")
                        choix_symbole = choix_symbole.replace(' ', '')
                        try:
                            # instanciation d'un objet de la classe Navire pour passer les tests relatifs au symboles
                            test_navire = FactoryNavire(nom=choix_nom, taille=choix_taille, symbole=choix_symbole)
                            choix_symbole_valide = True
                            choix_nom_symbole_valide = True
                        except:
                            print("Le symbole choisi est invalide !")
                            print("Le symbole doit être une unique lettre.\n")

        navire = FactoryNavire(nom=choix_nom, taille=choix_taille, symbole=choix_symbole).get_navire()
        return navire

    # objectif de la méthode de classe :
    # afficher un df.pandas à partir d'un set d'instance de la classe 'Navire'
    def afficher_navires(self, navires: set):
        list_noms = []
        list_symboles = []
        list_tailles = []

        for navire in navires:
            list_noms.append(navire.get_nom())
            list_symboles.append(navire.get_symbole())
            list_tailles.append(navire.get_taille())

        df = pd.DataFrame({"noms": list_noms, "symboles": list_symboles, 'tailles': list_tailles})
        print(df)
        return True


class FactoryCreationModeJeu():
    def get_creation_mode_jeu(self):
        return self.creation_mode_jeu

    def get_mode_jeu(self):
        self.creation_mode_jeu.get_mode_jeu()

    def __init__(self, nom: str):
        self.creation_mode_jeu = CreationModeJeu(nom=nom)
        self.creation_mode_jeu.main()
