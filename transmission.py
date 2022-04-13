import random as rd
import traitement as ttt

def bruit(encode):
    """
    effectue le bruitage du texte encode en parametre
    le bruitage consistera a prendre un entier au hasard de chaque mot de encode
    et de lui changer sa valeur soit en 1 soit en 0
    donc le mot peut etre bruitée ou non
    """
    for el in encode :
         i = rd.randint(0, len(el)-1) # le bit a changer
         j = rd.randint(0, 1)
         el[i] = j
    return encode

def transmis(encode):
    """
    retourne le message finale regroupe bruite
    a envoyer
    """
    trans = ""
    br = bruit(encode)
    return ttt.convert_en_str(br)

print(transmis([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 0, 0], [1, 0, 1, 1]]))

