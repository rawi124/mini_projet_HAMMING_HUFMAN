import decodage as dec

class Client :
    """
    pour reception, decodage et decryptage
    """
    def __init__(self, data ):
        self.data = data
        self.H = [[1, 1, 1, 0, 0, 0, 0],[1, 0, 0, 1, 1, 0, 0],[0, 1, 0, 1, 0, 1, 0],[1, 1, 0, 1, 0, 0, 1]]
        self.n = len(self.H[0])
        
    def corrige_message(self, data, H):
        self.data = dec.corrige_ens(data, self.n, H)


A = Client("000000000000000000000100011110110101011010101101000101101110101011010101011010000000")
A.corrige_message(A.data, A.H)
        
