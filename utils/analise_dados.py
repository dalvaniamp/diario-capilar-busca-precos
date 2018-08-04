from unidecode import *

class AnaliseDeDados():
    @staticmethod
    def Levenshtein(s, t):
        #Algoritmo de distancia de Levenshtein iterativo com duas matrizes.
        #Fonte: http//en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
        s=AnaliseDeDados.__formataTextoParaComparacao(s)
        t=AnaliseDeDados.__formataTextoParaComparacao(t)
        if s == t: return 0
        elif len(s) == 0: return len(t)
        elif len(t) == 0: return len(s)
        v0 = [None] * (len(t) + 1)
        v1 = [None] * (len(t) + 1)
        for i in range(len(v0)):
            v0[i] = i
        for i in range(len(s)):
            v1[0] = i + 1
            for j in range(len(t)):
                cost = 0 if s[i] == t[j] else 1
                v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
            for j in range(len(v0)):
                v0[j] = v1[j]                
        return v1[len(t)]

    @staticmethod
    def Hamming(s, t):
        #Algoritmo de distancia de Hamming
        #Fonte: http://claresloggett.github.io/python_workshops/improved_hammingdist.html        
        s=AnaliseDeDados.__formataTextoParaComparacao(s)
        t=AnaliseDeDados.__formataTextoParaComparacao(t)        
        if s == t:
            return 0   
        distancia=0         
        L = min(len(s),len(t))
        for i in range(L):
            if s[i] != t[i]:
                distancia += 1
        return distancia

    def __formataTextoParaComparacao(texto):
        #TODO: remover textos desnecessarios (de, para, a...)
        return unidecode(texto.lower())

    
