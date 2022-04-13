import math as math
import Node as N

codes = dict()

# convertir le texte en binaire
#codage de source
#codage de canal

def calcul_probabilite(chaine):
    """
    calucle les probabilités des differents caracteres
    de la chaine en parametre
    """
    liste_proba = {}
    i = 0
    while i < len(chaine):
        courant = chaine[i]
        if courant not in liste_proba.keys() :
            cpt = 0
            for c in chaine :
                if courant == c :
                    cpt +=1
            liste_proba[courant] = cpt
        i += 1
    return liste_proba

def calcul_entropie(dico, longeur):
    """
    calcule l entropie des valeurs du diotionnaire
    """
    entropie = 0
    for valeur in dico.values():
        entropie += (valeur/longeur)*math.log2(valeur/longeur)
    return -entropie


def Calculate_Codes(node, val=''):
    """
    affiche les codes des symboles en parcourant
    l arbre de huffman
    """
    newVal = val + str(node.code)

    if(node.left):
        Calculate_Codes(node.left, newVal)
    if(node.right):
        Calculate_Codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal

    return codes


def Output_Encoded(data, coding):
    """
    une fonction qui retrouve et affiche le text encodé
    """
    encoding_output = []
    for c in data:
      #  print(coding[c], end = '')
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string

def Total_Gain(data, coding):
    """
    calcule le gain total qu'apporte le codage de huffman vs le codage
    normal ( un caractere sur 8 bits)
    """
    before_compression = len(data) * 8 # total bit space to stor the data before compression
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol]) #calculate how many bit is required for that symbol in total
    print("avant compression(avant Huffman):", before_compression, " bits")
    print("apres compression :",  after_compression, " bits")

def Huffman_Encoding(data):
    """
    fonction qui realise l encodage de Huffman
    """
    symbol_with_probs = calcul_probabilite(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols: ", symbols)
    print("probabilities: ", probabilities)

    nodes = []

    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(N.Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)
        # for node in nodes:
        #      print(node.symbol, node.prob)

        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        # combine the 2 smallest nodes to create new node
        newNode = N.Node(left.prob+right.prob, left.symbol+right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = Calculate_Codes(nodes[0])
    print("codes des symboles ", huffman_encoding)
    Total_Gain(data, huffman_encoding)
    encoded_output = Output_Encoded(data,huffman_encoding)
    return encoded_output, nodes[0]


if __name__ == "__main__" :
    data = "testdeti"
    print(data)
    encoding, tree = Huffman_Encoding(data)
    print("le texte encodé", encoding)
