import os

import unicodedata
import string
 

print()
s = "string. With. Pun__ctuation?"


print(s)

def supprimeAccent(string):
    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode("utf-8")

def minusculeString(string):
    return string.lower()

def supprimePonctuation(string):
    for ponctuation in string.punctuation:
        string = string.replace(ponctuation, "")
    return string

def extractionDonner(chemin_racine) :
    """
    Fonction qui va extraire les titres des différents réperteroires ( et sous répertoires) ainsi que les fichiers textes.
    
    param : chemin_racine (string) -> chemin vers le dossier racine qui contient l'ensemble des sous repertoires et fichier texte.
    return : liste[string] -> liste de tous les titres des series et épisodes
    """
    mot = []
   
    for root, directories, files in os.walk(chemin_racine):  

        #Parcours l'ensemble des fichiers
        for file in files:
            mot.append(file)

        #Parcours l'ensemble des répertoires
        for directorie in directories:
            mot.append(directorie)
    
    return mot

def traduitDonner(string):
    """
    Fonction qui va traduire les titres des séries et épisodes en une seule langue.
    
    param : string -> chaine de caractere qui corresponds a un titres d'une serie ou d'un épisode.
    return : string -> chaine de caractere traduit en une unique langue.
    """
    return string

def normaliseDonner(string):
    """
    Fonction qui va normaliser une donner.
    Cette fonction va mettre en minuscule la string, retirer les caracteres spécifiques.
    
    param : string -> chaine de caractere a normaliser
    return : string -> chaine de caractere normaliser.
    """
    string = minusculeString(string) #mettre tous les mots en minuscules
    string = supprimePonctuation(string) #remplace accent 
    string = supprimePonctuation(string) #supprime la ponctuation
    return string

def filtreDonner(liste) :
    """
    Fonction qui va filtrer les donner.
    Cette fonction va filtrer les donners inutiles mot trop frequent ...
    
    param : liste[string] -> liste chaine de caractere a filtrer
    return : liste[string] -> liste chaine de caractere filtrer.
    """
    return liste




