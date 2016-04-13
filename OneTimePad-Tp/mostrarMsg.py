# coding=UTF-8

c1="664b75273f766a1d3f3c1f4656104107060e0b2d642831663c2549514809770b03681a6871".decode('hex')
c2="6746232c22773f3735694c5856106c1b0c483a2a292068363e2e0d430140370a574c30042c2724326a2d2c33".decode('hex')
c3="7d4b306902040b64393a185113405617050c0d6e2f2031663a244e4611442b434c4a".decode('hex')
c4="7d4b306902040b64312a4a5f5d494e551a110f2d20366820303817143a5d294f505079040c2e283a2334692b282d6a1e3b440f544c24".decode('hex')
c5="7d4b3c3a703e396431694b585c42575504001d3025222d677e".decode('hex')
c6="7d4b3069333e3a2c353b4c554b440e1a0709176325313c273c210d430746345903423c4a3a663e3e3e2e6939332b392b365c1f4d4425310825215921302569".decode('hex')
c7="7c503c27377718171169595c5c5e465500164e27252b2f232d255847461a71".decode('hex')
c8="6a512c3924382d363139505950104b141a0d0b30642c3b662a3948504840300a405630452b2369273f2425232569213a26080c50432d3a583421473d2676696874".decode('hex')
c9="684d3a3d383238642321574247104e101a160f24216b66687f6b0c".decode('hex')
c10="6e463b2c22363e2134695a491d1e0d".decode('hex')
c11="604d75392535262d336453554a10400710151a2c233729363733011409142f5f41483c477f2d2c2e6a202024212c382f2d41044d0d232c0827685a213a253c69262a21252c392535693a207732303a2b3069253d2334693a2a6939222b3e3d2f463f702f652a3f27212f21643f203128212c752346537b".decode('hex')

def otp(m,k):
	if len(m)==len(k):
		aux=""
		z=zip(m,k)
		for msg,chave in z:
			aux=aux+chr(ord(msg)^ord(chave))
		return aux

print "Quantidade de caracteres:"
print "1) "+str(len(c1))
print "2) "+str(len(c2))
print "3) "+str(len(c3))
print "4) "+str(len(c4))
print "5) "+str(len(c5))
print "6) "+str(len(c6))
print "7) "+str(len(c7))
print "8) "+str(len(c8))
print "9) "+str(len(c9))
print "10) "+str(len(c10))
print "11) "+str(len(c11))+"\n"

msg8= "Cryptographic hashes is used to create public key fingeprints!!!!"
chave = otp(c8,msg8)
#Chave: )#UIPWJDPI8030#uienCDEHF_J-4h4_*#$U$_FIWJFIJFIJ__(j9-J_(FH)IUWHIU

# PRINT DE TODAS AS MSGS
print "Chave: "+ chave+"\n"
print "1) "+otp(c1[:37],chave[:37])
print "2) "+otp(c2[:44],chave[:44])
print "3) "+otp(c3[:34],chave[:34])
print "4) "+otp(c4[:54],chave[:54])
print "5) "+otp(c5[:25],chave[:25])
print "6) "+otp(c6[:63],chave[:63])
print "7) "+otp(c7[:31],chave[:31])
print "8) "+otp(c8[:65],chave[:65])
print "9) "+otp(c9[:27],chave[:27])
print "10) "+otp(c10[:15],chave[:15])
print "11) "+otp(c11[:len(chave)],chave)
