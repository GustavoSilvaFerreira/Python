
c11="604d75392535262d336453554a10400710151a2c233729363733011409142f5f41483c477f2d2c2e6a202024212c382f2d41044d0d232c0827685a213a253c69262a21252c392535693a207732303a2b3069253d2334693a2a6939222b3e3d2f463f702f652a3f27212f21643f203128212c752346537b".decode('hex')

caracter=")#UIPWJD803uienCEHF_-h4*$(j9ABGKLMNOQRSTXYZabcdfgklmopqrstvwxyz125679."

import itertools
#for i in itertools.permutations (caracter,3):
 #   arq.writelines(str(i)+'\n')
  #  print i

lista=[]
def permChave(c,m):
	for i in itertools.permutations(c,3):
		if len(m[64:67])==len(i):
			aux=""
			z=zip(m,i)
			print z
			for msg,chave in z:
				aux=aux+chr(ord(msg)^ord(chave))
				print str(i)
			z=""
			lista.append("Chave "+str(i)+" VALOR: "+aux+"\n")
	arq= open('chave2','w')
	arq.writelines(lista)
	arq.close()
				
permChave(caracter,c11)