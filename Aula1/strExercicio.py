palavra = raw_input('Digite uma palavra: ')
#Mostre esta palavra em ordem reversa
acc=''
for e in palavra:
	acc = e+acc
print acc