import codage_canal as cc
import codage_source as cs
import transmission as tr 

class Serveur :
    """
    pour le chiffrage, le codage, et la transmission des donnees
    """
    def __init__(self, data ):
        self.data = data
        self.G = [[1, 1, 1, 0, 0, 0, 0],[1, 0, 0, 1, 1, 0, 0],[0, 1, 0, 1, 0, 1, 0],[1, 1, 0, 1, 0, 0, 1]]

    def cod_source(self, data):
        self.data = cs.Huffman_Encoding(data)

    def cod_canal(self, G, bits, n):
        self.data = cc.cod_canal(G, bits, n)

    def bruitage(self, encode):
        self.data = tr.transmis(encode)



A = Serveur("AAAAAAABCCCCCCDDEEEEE")
print("texte d origine\n", A.data)
A.cod_source(A.data)
print("texte apres huffman\n", A.data)
A.cod_canal(A.G, A.data, 4)
print("texte apres codage canal\n", A.data)
A.bruitage(A.data)
print("texte apres bruitage\n", A.data)

