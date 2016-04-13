# coding=UTF-8
# Zip: É uma função que recebe duas Strings e retorna uma tupla de tuplas de duas posições.

z=zip("ABC","123")
print z

for t in z:
    print "Primeira letra: "+t[0]
    print "Segunda letra: "+t[1]

# Pattern Matching
for (x,y) in z:
    print "Primeira: "+x+" Segunda: "+y+" Concatenado: "+x+y
    
