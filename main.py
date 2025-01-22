'''
Fichier principal du projet.

Contient la fonction lancer_partie() ou du code correspondant à ça.
Cette fonction réalise les appels nécéssaire au bon déroulement de la partie.
Elle permet de regrouper les phases d'initialisation et de jeu :
 - La phase d'initialisation concerne la gestion/ création des paraètres, stratégie, etc...
 - La phase de jeu lance la partie avec la classe BatailleNavale() avec les paramètres définis précédement.

La fin de partie est gérée dans la classe BatailleNavale().
'''

from ChoixStrategie import ChoixStrategie
from Strategie import Strategie
from BatailleNavale import BatailleNavale
from Grille import Grille

# Fonction d'input.
# Prend en parametre le n° du joueur.
# Demande le nom du joueur.
# Appel de la classe ChoisirStrategie() pour le joueur concerné.
# La fonction renvoie une liste qui contient le nom du joueur saisi
# et sa strategie sous la forme d'une instance de la classe Strategie.
def choix_nom_et_strategie_joueur(numero_joueur):
    # initialisation de variables locales
    pseudo_joueur = ''
    # Le booléen choix_valide_joueur permet de gérer les cas d'erreur sur les inputs et d'y répondre de manière efficace :
    # en redemandant à l'utilisateur de rentrer sa données en précisant pourquoi cela n'a pas marché la 1ère fois.
    choix_valide_joueur = False


    while not choix_valide_joueur :
        pseudo_joueur = input(f"Joueur {numero_joueur}, quel est votre pseudo ? \n")

        try :
            pseudo_joueur = pseudo_joueur.replace(" ", "")
            assert len(pseudo_joueur) < 15
            if not pseudo_joueur.isalnum() :
                raise ValueError
            elif pseudo_joueur == '_Ordinateur':
                raise ZeroDivisionError
            choix_valide_joueur = True
        except AssertionError :
            print("Le nom du joueur est trop long !\n")
        except ValueError :
            print('Le nom doit être composé de lettres et/ou de chiffres.\n')
        except ZeroDivisionError :
            print("Ce pseudo est privatisé, vous ne pouvez pas l'utiliser. Choisissez en un autre :\n")

    print("")
    strategie_joueur = ChoixStrategie(pseudo_joueur, navires=navires).get_strategie()

    return [pseudo_joueur, strategie_joueur]



if __name__ == "__main__":
    print('Bienvenue dans le jeu de Bataille Navale !')

    choix_adversaire=''

    # Le booléen choix_valide_joueur permet de gérer les cas d'erreur sur les inputs et d'y répondre de manière efficace :
    # en redemandant à l'utilisateur de rentrer sa données en précisant pourquoi cela n'a pas marché la 1ère fois.
    choix_adversaire_valide = False
    while not choix_adversaire_valide :

        # Choix de l'adversaire + rajouter une gestion d'erreur + texte de réponse adapté à la variable.
        choix_adversaire = input("Voulez-vous jouer contre un joueur ou contre l'ordinateur ? (joueur / ordinateur)\n")

        try :
            choix_adversaire = choix_adversaire.lower()
            choix_adversaire = choix_adversaire.replace(" ", "")
            assert choix_adversaire == 'ordinateur' or choix_adversaire == 'joueur'
            choix_adversaire_valide = True
        except AssertionError :
            print('Erreur !\nVeuillez saisir une valeur valide.')


    print("")
    choix_adversaire.lower()

    navires = {'Torpilleur': [2, 'T'], 'Sous-marin':[3, 'S'], 'Frégate':[3, 'F'], 'Cuirassé':[4, 'C'], 'Porte-avions':[5, 'P']}


    # Choix des stratégie -> appel de la classe ChoixStrategie()
    if choix_adversaire == 'joueur' :
        # 1er joueur
        information_j1 = choix_nom_et_strategie_joueur(1)
        nom_j1 = information_j1[0]
        strategie_j1 = information_j1[1]

        print("")

        # 2eme joueur
        information_j2 = choix_nom_et_strategie_joueur(2)
        nom_j2 = information_j2[0]
        strategie_j2 = information_j2[1]

    elif choix_adversaire == 'ordinateur':
        # 1er joueur
        information_j1 = choix_nom_et_strategie_joueur(1)
        nom_j1 = information_j1[0]
        strategie_j1 = information_j1[1]

        # Rajouter du code pour initialiser la strategie de l'ordinateur (définie par défault).
        # La privatisation (théorique) du nom permet dans la classe BatailleNavale() de passer le jeu de l'ordinateur en auto.
        nom_j2 = '_Ordinateur'
        strategie_j2 = Strategie({'Torpilleur': [2, 1, 1, 'S'],
                                  'Sous-marin': [3, 5, 1, 'S'],
                                  'Frégate': [3, 3, 5, 'E'],
                                  'Cuirassé': [4, 5, 6, 'O'],
                                  'Porte-avions': [5, 9, 9, 'N']},
                                 navires,
                                 Grille(10, 10))

    BatailleNavale(navires, strategie_j1, strategie_j2, Grille(10,10),nom_j1, nom_j2)