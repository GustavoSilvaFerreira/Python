# coding=UTF-8
def ola():
    print 'Ola'
    
def somar(x,y):
    return x+y
    
def dicionario():
    # Um dicionario é uma lista com índices não necessariamente inteiros. Não é possivel ter uma lista como índice.
    
    #Dicionário vazio
    d ={}
    d["casa"] = 9
    d[5] = "Gustavo"
    d[9.8] = '1'
    d[8] = [1,2,3,4]
    print d
    
def contar(palavra):
    # Esse dicionário possuirá como índice as letras da palavra
    dic={}
    for letra in palavra:
        if letra in dic:
            dic[letra]=dic[letra]+1
        else:
            dic[letra]=1
            
    print dic
    
contar("ababababab")
dicionario()
    
