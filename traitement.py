def convert_en_liste(enc):
    """
    convertit une chaine de caractere binaire en liste de binaire
    """
    i = 0
    l_bin = []
    while i < len(enc):
        l_bin.append(int(enc[i]))
        i += 1
    return l_bin

def convert_en_str(enc):
    """
    convertit une chaine de caractere binaire en liste de binaire
    """
    ch_bin = ""
    for el in enc :
        for c in el :
            ch_bin += str(c)
    return ch_bin

def decoupage(encode, n):
    """
    effectue la segmentation en segment de longeur n
    """
    i = 0
    dec = []
    while i < len(encode) :
        j = i+n
        c = encode[i:j]
        dec.append(c)
        i = j
    if len(c) < n :
        l = n - len(c)
        i = 0
        while i < l :
            c = c + '0'
            i += 1
    dec[len(dec)-1]  = c
    return dec
