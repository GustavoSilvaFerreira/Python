# coding=UTF-8
# Para Casa
# Faça uma função toDict(a,b) que receba duas Strings a, b e retorne um dicionário contendo o seguinte
# toDict("SOL","LUA") = {'S':'L','O':'U','L':'A'}

def toDict(a,b):
    dic={}
    z=zip(a,b)
    for (x,y) in z:
        dic[x]=y
    print dic
    
toDict("ACE","BDF")
