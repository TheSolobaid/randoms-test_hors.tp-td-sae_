import os
import csv


def charger_fichier_csv(nom_fichier):
    """Charge le contenu d'un fichier CSV dans une liste de dictionnaires"""
    result = []
    with open(nom_fichier, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)
    return result


def ecrire_fichier_csv(nom_fichier, donnees):
    """Écrit les données dans un fichier CSV"""
    with open(nom_fichier, 'w', newline='') as csvfile:
        fieldnames = donnees[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(donnees)


def combiner_fichiers_csv(dossier_input, fichier_sortie):
    # Liste de tous les fichiers CSV dans le dossier d'entrée
    fichiers_csv = [f for f in os.listdir(dossier_input) if f.endswith('.csv')]

    # Créer un ensemble pour stocker les lignes uniques
    lignes_uniques = set()

    # Liste pour stocker les données combinées
    donnees_combinees = []

    for fichier_csv in fichiers_csv:
        chemin_fichier = os.path.join(dossier_input, fichier_csv)

        # Charger le fichier CSV
        donnees_fichier = charger_fichier_csv(chemin_fichier)

        # Ajouter les lignes du fichier au résultat si elles ne sont pas déjà présentes
        for ligne in donnees_fichier:
            if tuple(ligne.values()) not in lignes_uniques:
                donnees_combinees.append(ligne)
                lignes_uniques.add(tuple(ligne.values()))

    # Écrire les données combinées dans le fichier de sortie
    ecrire_fichier_csv(fichier_sortie, donnees_combinees)


# Dossier d'entrée contenant les fichiers CSV

dossier_input = 'test_combinne_csv/input'

# Fichier de sortie combinant tous les fichiers CSV
fichier_sortie = 'test_combinne_csv/output/fichier_combine.csv'

# Appel de la fonction pour combiner les fichiers CSV
combiner_fichiers_csv(dossier_input, fichier_sortie)