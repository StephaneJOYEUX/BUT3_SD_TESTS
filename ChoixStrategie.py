"""
Classe ChoixStrategie()
Il s'agit de la classe qui permet l'interaction avec l'utilisateur. (!!ATTENTION!! : beaucoup d'input)

Fonctionnement : Guider l'utilisateur dans ses choix et actions jusqu'à qu'il se voit attribué un stratégie.

1er choix :
    - créer une strategie
    - choisir une strategie existante

- Créer une strategie :
    Appel de la classe CreationStrategie().
    Appel de la methode get() de cette même classe après la création.

- Choisir une strategie existante :
    Afficher la liste des strategie présentent dans le referentiel. (nous reviendront apres à ce référentiel)
    2ème Choix : choisir l'une des proposition + choix de retour
    Afficher la strategie dans la grille avec la methode affichage_strategie() de la Classe Strategie().
    3ème choix : confirmer la selection ou retour au choix precedent
    Si confirmation : attribution de la strategie.

Programmer une methode get() pour sortir la strategie choisie de la classe
afin de l'utiliser ensuite dans la classe BatailleNavale().


Méthode main() :
    méthode principale du programme qui agit comme une interface utilisateur.
    Dans cette méthode nous guidons l'utilisateur dans ses choix afin de lui proposer une expérience de jeu optimale.


Méthode valider_input_utilisateur():
    Prend en input une requette faite à l'utilisateur, ainsi que 2 choix possible pour l'utilisateur. (str)
    Cette méthode permet de vérifier si l'utilisateur à bien rentrer un choix cohérent.
    Elle permet d'éviter des erreurs liées aux input.

    Remarque : Le code de vérification des inputs n'est pas exclusif à cette méthode, pour les cas plus spécifiques,
    il est difficile de centraliser la vérification des données d'input.

Le référentiel :
    C'est une liste qui contient des dictionnaires/ des instances de la classe Strategie (à déterminer lors de la prog)
    Ce référentiel est vide à l'initialisation.
    Il faut le remplir en récupérant les information d'un fichier txt annexe.
    A la fin de l'execution de la classe, on efface les informations du fichier txt et on écrit les informations contenues
    dans le référentiel.
    Cela permet de 'sauvegarder' des stratégies.

La classe contient aussi des méthodes de lecture et d'écriture dans un fichier de sauvegarde annexe (.txt).
"""
from ast import literal_eval

import pandas as pd
from unidecode import unidecode
from CreationStrategie import CreationStrategie
from Grille import Grille, afficher_grille
from Strategie import Strategie


class ChoixStrategie() :
    def __init__(self, pseudo_joueur, navires, Grille = Grille(10,10), test : bool = False):

        self.navires = navires
        self.referentiel = []
        self.lire_fichier_sauvegarde()

        self.instance_grille=Grille
        self.pseudo_joueur = pseudo_joueur

        self.strategie : Strategie

        if not test :
            # lancement de la méthode principale.
            self.main()

        # dernière méthode : écriture des données du référentiel dans le fichier de sauvegarde.
        self.ecrire_fichier_sauvegarde()

    # Lecture du fichier et récupération des strategie enregistrées dans le référentiel.
    def lire_fichier_sauvegarde(self):
        # Ouverture du fichier + lecture des lignes une à une + fermeture du fichier.
        file = open('sauvegardes_strategies.txt', 'r', encoding='UTF-8')
        donnees_lecture = file.readlines()
        file.close()

        # Formatage des données en dict avant de créer des instances de la classe Strategie() à partir de chacun des dict.
        for str_strategie in donnees_lecture:
            # Suppression des sauts de lignes
            str_strategie.replace("\n", "")

            # Utilisation de la fonction literal_eval() du module ast.
            # Elle permet de passer les chaine de caractères en dict.
            str_strategie = literal_eval(str_strategie)

            #print(strategie)
            #print(type(strategie))
            strategie = Strategie(str_strategie, self.navires)

            # remplacer strategie par var dazns l'append de liste
            self.referentiel.append(strategie)


    # On écrit le fichier de sauvegarde à partir des données du référentiel.
    def ecrire_fichier_sauvegarde(self):
        # Variable locale pour 'protéger' notre référentiel.
        liste_ecriture = []


        # Formatage des données pour l'écriture (passage en str)

        for instance_strategie in self.referentiel :
            donnee = instance_strategie.informations
            # Vérification du type (attendu : dict)
            donnee = str(donnee) + '\n'
            liste_ecriture.append(donnee)


        # Création d'une chaine unique -> application unique de la fonction write()
        chaine_ecriture = "".join(liste_ecriture)

        # Ouverture du fichier + écriture + fermeture du fichier
        test = open('sauvegardes_strategies.txt', 'w', encoding='UTF-8')
        test.write(chaine_ecriture)
        test.close()


    # Méthode principale qui appelle toutes les autres en fonction des choix du joueur.
    def main(self):

        print(f"C'est à {self.pseudo_joueur} de choisir sa stratégie de bataille.")
        choix_choisir_creer = f"{self.pseudo_joueur}, voulez-vous choisir une stratégie enregistrée ou en créer une nouvelle ?"
        choix_choisir = 'choisir'
        choix_creer = 'creer'
        # validation de l'input avec la méthode associée
        choix = self.valider_input_utilisateur(choix_choisir_creer, choix_choisir, choix_creer)

        # Définition des variables associée aux choix OUI/NON.
        # Utile pour la méthode de validation d'input.
        choix_oui = 'o'
        choix_non = 'n'

        if choix == 'creer' :
            # Appel de la classe CreationStrategie() -> lancement du code de création
            # Appel de la methode get_instance_strategie() qui retourne l'instance de la classe Strategie() créée.
            self.strategie = CreationStrategie(self.navires, self.instance_grille).get_instance_strategie()

            # Création de la chaine rentrée ensuite en paramètre de la fonction input()
            choix_action_enregistrement = "Voulez-vous enregistrer la stratégie créée ?"
            # validation de l'input avec la méthode associée
            choix_enregistrement = self.valider_input_utilisateur(choix_action_enregistrement, choix_oui, choix_non)

            if choix_enregistrement == 'o' :
                # Ajout de la stratégie au référentiel.
                # il s'agit ici d'une instance de la classe Strategie().
                self.referentiel.append(self.strategie)
                print("La stratégie a bien été enregistrée.")
            else :
                print('Vous avez choisi de ne pas enregistrer la strategie.')


            # Affichage de la strategie du joueur + Fin du main
            print("")
            print(f"{self.pseudo_joueur}, votre stratégie a bien été définie.")
            print("")

            self.instance_grille.create()
            self.strategie.placement_navires_joueur(self.instance_grille.plateau, self.strategie.informations)
            afficher_grille(self.instance_grille.plateau)
            return True

        elif choix == 'choisir':

            strategie_correctement_choisie = False
            while not strategie_correctement_choisie :
                self.instance_grille.create()
                print('Voici la liste des stratégies enregistrée :')

                for index_strat in range(len(self.referentiel)) :
                    print("Stratégie n°"+str(index_strat)+ "  "+str(self.referentiel[index_strat].informations))
                print("")


                valider_choix_numero_strategie = False

                while not valider_choix_numero_strategie :
                    choix_numero_strategie = input("Quelle stratégie voulez-vous choisir ?  (Choisir une numéro de stratégie)\n")
                    print("")

                    try :
                        choix_numero_strategie = int(choix_numero_strategie)

                        # On associe la strategie choisie en input à la variable locale strategie_choisie.
                        strategie_choisie = self.referentiel[choix_numero_strategie]
                        print(strategie_choisie.informations)

                        valider_choix_numero_strategie = True
                    except IndexError :
                        print(f"La stratégie n°{choix_numero_strategie} n'existe pas !")
                        print("Choisissez une stratégie existante.")
                    except :
                        print("Erreur de saisie !")
                        print('Choisissez le numéro de la stratégie parmis les stratégie existantes.')



                print(f"Vous avez choisi la stratégie n°{choix_numero_strategie} :\n")

                # On place la strategie dans la grille
                strategie_choisie.placement_navires_joueur(self.instance_grille.plateau, strategie_choisie.informations)
                # On l'affiche
                afficher_grille(self.instance_grille.plateau)

                # Confirmation du choix de la strategie
                choix_action_confirmation_strategie = "Confirmez votre choix ?"
                # validation de l'input
                confirmation_choix_strategie = self.valider_input_utilisateur(choix_action_confirmation_strategie, choix_oui, choix_non)

                # Condition de sortie de boucle -> OK
                if confirmation_choix_strategie == 'o' :
                    print(f'Vous avez bien choisi la stratégie n°{choix_numero_strategie}')
                    self.strategie = strategie_choisie
                    strategie_correctement_choisie = True


            # Affichage de la strategie du joueur + Fin du main
            print("")
            print(f"{self.pseudo_joueur}, votre stratégie a bien été définie.")
            print("")

            self.instance_grille.create()
            self.strategie.placement_navires_joueur(self.instance_grille.plateau, self.strategie.informations)
            afficher_grille(self.instance_grille.plateau)
            return True


    # Méthode permettant de protéger les inputs utilisateur et de gérer les cas d'erreur.
    def valider_input_utilisateur(self, requette : str, choix_1 : str, choix_2 : str):
        # condition de validité de l'input
        validite_choix_utilisateur = False

        # boucle de vérification / modification de la valeur précédente.
        while not validite_choix_utilisateur :
            choix_utilisateur = input(requette + '  (' + choix_1 + '/' + choix_2 + ')\n')

            try :
                # Suppression des accents potentiels
                choix_utilisateur = unidecode(choix_utilisateur)
                # Passage de la chaine en minuscule
                choix_utilisateur = choix_utilisateur.lower()
                choix_1 = choix_1.lower()
                choix_2 = choix_2.lower()

                assert choix_utilisateur == choix_1 or choix_utilisateur == choix_2
                validite_choix_utilisateur = True

            except AssertionError:
                print("Erreur de saisie !")
                print("Vous devez choisir l'une des propositions\n")
            except :
                print('Erreur !')
                print('Suivez les instructions pour pouvoir jouer correctement !\n')

        print("")
        return choix_utilisateur


    def get_referentiel(self):
        return self.referentiel

    def get_strategie(self):
        return self.strategie





from Strategie import Strategie_2
from CreationStrategie import CreationStrategie_2, FactoryCreationStrategie_2



class ChoixStrategie_2() :
    def __init__(self, pseudo_joueur, navires, mode_jeu = "Normal",  Grille = Grille(10,10), test : bool = False):
        self.mode_jeu : str = mode_jeu
        self.navires = navires
        self.referentiel : pd.DataFrame = pd.DataFrame({
            "mode_jeu":[],
            "index_strategie":[],
            "nom":[],
            "taille":[],
            "coord_x":[],
            "coord_y": [],
            "orientation":[],
        })
        self.lire_fichier_sauvegarde()

        self.instance_grille=Grille
        self.pseudo_joueur = pseudo_joueur

        self.strategie : Strategie

        if not test :
            # lancement de la méthode principale.
            self.main()

        # dernière méthode : écriture des données du référentiel dans le fichier de sauvegarde.
        self.ecrire_fichier_sauvegarde()

    # Lecture du fichier et récupération des inputs_strategie enregistrées dans le référentiel.
    def lire_fichier_sauvegarde(self):
        # Ouverture du fichier + lecture des lignes une à une + fermeture du fichier.
        self.referentiel = pd.read_csv('sauvegardes_strategies_2.csv', encoding="UTF-8")


    # On écrit le fichier de sauvegarde à partir des données du référentiel.
    def ecrire_fichier_sauvegarde(self):
        self.referentiel.to_csv('sauvegardes_strategies_2.csv', index = False, encoding="UTF-8")


    # Méthode principale qui appelle toutes les autres en fonction des choix du joueur.
    def main(self):

        print(f"C'est à {self.pseudo_joueur} de choisir sa stratégie de bataille.")
        choix_choisir_creer = f"{self.pseudo_joueur}, voulez-vous choisir une stratégie enregistrée ou en créer une nouvelle ?"
        choix_choisir = 'choisir'
        choix_creer = 'creer'
        # validation de l'input avec la méthode associée
        choix = self.valider_input_utilisateur(choix_choisir_creer, choix_choisir, choix_creer)

        # Définition des variables associée aux choix OUI/NON.
        # Utile pour la méthode de validation d'input.
        choix_oui = 'o'
        choix_non = 'n'

        if choix == 'creer' :
            # Appel de la classe CreationStrategie() -> lancement du code de création
            # Appel de la methode get_instance_strategie() qui retourne l'instance de la classe Strategie() créée.
            creation_strategie = FactoryCreationStrategie_2(self.navires, self.instance_grille)
            self.strategie = creation_strategie.get_instance_strategie()
            print(type(creation_strategie))
            print(type(self.strategie))

            # Création de la chaine rentrée ensuite en paramètre de la fonction input()
            choix_action_enregistrement = "Voulez-vous enregistrer la stratégie créée ?"
            # validation de l'input avec la méthode associée
            choix_enregistrement = self.valider_input_utilisateur(choix_action_enregistrement, choix_oui, choix_non)

            if choix_enregistrement == 'o' :
                # Ajout des inputs de la stratégie au référentiel.
                # il s'agit ici des informations permettant d'instancier la classe Strategie
                new_inputs_strategie = self.strategie.get_informations()
                try:
                    index_strategie = max(self.referentiel["index_strategie"]) + 1
                except:
                    index_strategie = 1

                for line in new_inputs_strategie.values :
                    new_data = [self.mode_jeu, index_strategie] + list(line)
                    self.referentiel.loc[len(self.referentiel.index)] = new_data

                print("La stratégie a bien été enregistrée.")
            else :
                print('Vous avez choisi de ne pas enregistrer la strategie.')


            # Affichage de la strategie du joueur + Fin du main
            print("")
            print(f"{self.pseudo_joueur}, votre stratégie a bien été définie.")
            print("")

            self.instance_grille.create()
            self.strategie.placement_navires(self.instance_grille.plateau, self.strategie.informations)
            afficher_grille(self.instance_grille.plateau)
            return True

        elif choix == 'choisir':

            strategie_correctement_choisie = False
            while not strategie_correctement_choisie :
                self.instance_grille.create()
                print('Voici la liste des stratégies enregistrée :')

                # correspondance avec le mode de jeu
                df_strategie_to_choose = self.referentiel[self.referentiel.mode_jeu == self.mode_jeu]
                # extraction de l'ensemble des index_strategie correspondant au premier critère de filtrage (mode_jeu)
                liste_index_strategie = set(df_strategie_to_choose.index_strategie)
                # Boucle pour l'affichage
                for i in liste_index_strategie:
                    if i != 0 :
                        print(self.referentiel[self.referentiel.index_strategie==i])
                        print("------------------")

                for index_strat in range(len(self.referentiel)) :
                    print("Stratégie n°"+str(index_strat)+ "  "+str(self.referentiel[index_strat].informations))



                print("")


                valider_choix_numero_strategie = False

                while not valider_choix_numero_strategie :
                    choix_numero_strategie = input("Quelle stratégie voulez-vous choisir ?  (Choisir une numéro de stratégie)\n")
                    print("")

                    try :
                        choix_numero_strategie = int(choix_numero_strategie)

                        # On associe la strategie choisie en input à la variable locale strategie_choisie.
                        strategie_choisie = self.referentiel[choix_numero_strategie]
                        print(strategie_choisie.informations)

                        valider_choix_numero_strategie = True
                    except IndexError :
                        print(f"La stratégie n°{choix_numero_strategie} n'existe pas !")
                        print("Choisissez une stratégie existante.")
                    except :
                        print("Erreur de saisie !")
                        print('Choisissez le numéro de la stratégie parmis les stratégie existantes.')



                print(f"Vous avez choisi la stratégie n°{choix_numero_strategie} :\n")

                # On place la strategie dans la grille
                strategie_choisie.placement_navires_joueur(self.instance_grille.plateau, strategie_choisie.informations)
                # On l'affiche
                afficher_grille(self.instance_grille.plateau)

                # Confirmation du choix de la strategie
                choix_action_confirmation_strategie = "Confirmez votre choix ?"
                # validation de l'input
                confirmation_choix_strategie = self.valider_input_utilisateur(choix_action_confirmation_strategie, choix_oui, choix_non)

                # Condition de sortie de boucle -> OK
                if confirmation_choix_strategie == 'o' :
                    print(f'Vous avez bien choisi la stratégie n°{choix_numero_strategie}')
                    self.strategie = strategie_choisie
                    strategie_correctement_choisie = True


            # Affichage de la strategie du joueur + Fin du main
            print("")
            print(f"{self.pseudo_joueur}, votre stratégie a bien été définie.")
            print("")

            self.instance_grille.create()
            self.strategie.placement_navires_joueur(self.instance_grille.plateau, self.strategie.informations)
            afficher_grille(self.instance_grille.plateau)
            return True


    # Méthode permettant de protéger les inputs utilisateur et de gérer les cas d'erreur.
    def valider_input_utilisateur(self, requette : str, choix_1 : str, choix_2 : str):
        # condition de validité de l'input
        validite_choix_utilisateur = False

        # boucle de vérification / modification de la valeur précédente.
        while not validite_choix_utilisateur :
            choix_utilisateur = input(requette + '  (' + choix_1 + '/' + choix_2 + ')\n')

            try :
                # Suppression des accents potentiels
                choix_utilisateur = unidecode(choix_utilisateur)
                # Passage de la chaine en minuscule
                choix_utilisateur = choix_utilisateur.lower()
                choix_1 = choix_1.lower()
                choix_2 = choix_2.lower()

                assert choix_utilisateur == choix_1 or choix_utilisateur == choix_2
                validite_choix_utilisateur = True

            except AssertionError:
                print("Erreur de saisie !")
                print("Vous devez choisir l'une des propositions\n")
            except :
                print('Erreur !')
                print('Suivez les instructions pour pouvoir jouer correctement !\n')

        print("")
        return choix_utilisateur


    def get_referentiel(self):
        return self.referentiel

    def get_strategie(self):
        return self.strategie
