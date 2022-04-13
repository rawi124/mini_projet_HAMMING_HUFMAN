import traitement as ttt

def codage_canal(G, v ):
    """
    fait la multiplication de v.G
    pour avoir le mot c = v.G
    """
    j = 0
    c = []
    k = len(G[0])
    n = len(v)
    while j < k :
        s = 0
        i = 0
        while i < n :
            s = s + (G[i][j] * v[i])
            i += 1
        c.append(s%2)
        j+= 1
    return c

G=[[1, 1, 1, 0, 0, 0, 0],[1, 0, 0, 1, 1, 0, 0],[0, 1, 0, 1, 0, 1, 0],[1, 1, 0, 1, 0, 0, 1]]
#print(codage_canal(G,[1, 0, 0, 1]))

def cod_canal(G, encode, n):
    """
    effectue l'encodage de l'ensemble du texte
    """
    decoupe = ttt.decoupage(encode, n)
    i = 0
    enco = []
    while i < len(decoupe):
        c = ttt.convert_en_liste(decoupe[i])
        enco.append(codage_canal(G, c))
        i += 1
    return enco

ch = cod_canal(G, "001001100010100011", 4)
#print(ch)

