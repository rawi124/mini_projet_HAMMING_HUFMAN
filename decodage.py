import traitement as ttt

def syndrome(H, C):
    """
    effectue le calcul du syndrome
    si le syndrome est egale a un mot qui ne contient que des zeros
    donc pas d erreur
    sinon un bruitage a eu lieu
    """
    i = 0
    synd = []
    n = len(H)
    k = len(C)
    while i < n :
        s = 0
        j = 0
        while j < k:
            s = s + (H[i][j] * C[j])
            j+=1
        synd.append(s%2)
        i+=1
    return synd

H = [[0, 0, 0, 1, 1, 1, 1],[0, 1, 1, 0, 0, 1, 1],[1, 0, 1, 0, 1, 0, 1]]
#syndrome(H, [0, 0, 1, 0, 0, 0, 1])

def detect(s):
    """
    si le syndrome est egale a un mot qui ne contient que des zeros
    donc pas d erreur
    sinon un bruitage a eu lieu
    cette fonction renvoie un booleen :
            True si erreur
            False sinon
    """
    for el in s :
        if el == 1 :
            return True
    return True

def transpose(L):
    """
    calcule la transposee de la matrice en parametre
    """
    M = []
    for i in range(len(L[0])):
        aux = []
        for j in range(len(L)):
            aux = aux + [L[j][i]]
        M = M + [aux]
    return M

def corrige(H, C):
    """
    corrige le message C si bruitage
    sinon renvoie C sans modification 
    """
    s = syndrome(H, C)
    if detect(s):
        t = transpose(H)
        i = 0
        n = len(t[0])
        while i < len(t):
            Bool = True 
            if t[i][0] == s[0] :
                j = 1
                while j < n :
                    if t[i][j] != s[j] :
                        Bool = False
                    j += 1
                if Bool == True :
                    print("erreur dans bit num", i)
                    C[i] = C[i] ^ 1
                    break 
            i += 1
    return C 
            

def corrige_ens(message, n, H):
    mess = ttt.decoupage(message, n)
    #print(mess)
    res = []
    i = 0
    while i < len(mess):
        print("je traite le messsage", i)
        print(mess[i])
        mess[i] = ttt.convert_en_liste(mess[i])
        print(corrige(H, mess[i]),"\n")
        res.append(corrige(H, mess[i]))
        i += 1
    return ttt.convert_en_str(res)
    
#ch = corrige_ens("000000100100111111010101110111000001110011001011", 7, H)

#print(ch)



    
