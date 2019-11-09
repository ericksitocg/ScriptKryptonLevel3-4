nombreCifrado = "krypton4"
#
L_original = "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper().split()
L_clave = "b o i h g k n q v t w y u r x z a j e m s l d f p c".upper().split()
d2 = {}

for i in range(len(L_original)):
	d2[L_original[i]] = L_clave[i]

desencriptado = ""

f = open(nombreCifrado,"r").read()
for letra in f:
	if letra.isalpha():
		desencriptado+=d2[letra]

print(desencriptado)