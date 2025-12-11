"""Tuple"""
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    if not s:
        return []

    resultat = []
    car = s[0]
    tmp = 1

    for i in range (1, len(s)):
        if s[i] == car:
            tmp += 1
        else :
            car = s[i]
            tmp = 1

    resultat.append((car, tmp))
    return resultat


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée
    en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    if not s:
        return []

    tmp = 1
    while tmp < len(s) and s[tmp] == s[0]:
        tmp += 1

    return [(s[0], tmp)] + artcode_r(s[tmp:])

#### Fonction principale

def main():
    """Appel principal"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
