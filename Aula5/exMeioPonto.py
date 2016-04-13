# Faca um programa em Python para gerar 100 bits do exemplo 2


def gerar(ini,qtd):
    x=[]
    for o in ini:
        x.append(int(o))
    i=0
    while i<qtd:
        x.append(x[i+1]^x[i+2]^x[i])
        i=i+1
    return x
        
chave="1011"
print str(gerar(chave,100))

# feito pelo Garcia
def lfsr(x0,x1,x2,x3):
    x4=0
    while True:
        x4=x1^x2^x0
        yield x4
        x0=x1
        x1=x2
        x2=x3
        x3=x4
        
#1011 eh o Seed (chave do algoritmo)
g = lfsr(1,0,1,1)
aux=""
for i in range(100):
    aux = aux + str(g.next())
print aux