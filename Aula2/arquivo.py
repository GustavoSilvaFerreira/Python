# coding=UTF-8
arq= open('dados','r')

linhas=arq.readlines()
aux=[]
# strip corta os elementos por um parâmetro passado entre ()
for reg in linhas:
    aux.append(reg.strip('\n').split(','))
    
soma=0
for [x, y] in aux:
    soma+=float(y)
    
# round serve para determinar quantidade de casas
media=round(soma/len(aux),2)
print media


    



    
