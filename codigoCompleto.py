
def crearListasPorFrecuencia(s):
    print("--Creando listas de frecuencia--")
    L_letras = []
    L_frecuencias = []
    for letra in s.upper():
        if letra.isalpha():
            if letra not in L_letras:
                L_letras.append(letra)
                L_frecuencias.append(1)
            else:
                L_frecuencias[L_letras.index(letra)]+=1
    return L_letras,L_frecuencias

def ordenarLFrecuencias(L_letras,L_frecuencias):
	"""
    arreglo_letras = np.array(L_letras)
    arreglo_frecuencia = np.array(L_frecuencias)
    
    arreglo_letras = arreglo_letras[arreglo_frecuencia.argsort()[::-1]]
    return arreglo_letras
    """
	L_ord = []
	c = 0
	while(c!= len(L_frecuencias)):
		max_ind = L_frecuencias.index(max(L_frecuencias))
		max_letra = L_letras[max_ind]
		print("%s : %d coincidencias "%(max_letra,max(L_frecuencias)))
		L_ord.append(max_letra)
		L_frecuencias[max_ind] = -1
		c+=1
	return L_ord
	

    
L_letras_frecuentes_english = ["E","T","A","O","I","N","S","H","R","D","L","U","C","M","W","F","G","Y","P","B","V","K","J","X","Q","Z"]

def genDiccCifrado(letrasOrdenadas,LetrasGuiaLenguaje):
    d = {}
    for i in range(len(letrasOrdenadas)):
        #print("%s : %s"%(letrasOrdenadas[i],LetrasGuiaLenguaje[i]))
        d[letrasOrdenadas[i]] = LetrasGuiaLenguaje[i]
        #d[LetrasGuiaLenguaje[i]]=letrasOrdenadas[i]
    return d
def claveLevel3_4Krypton(nombreArchivo1,nombreArchivo2,nombreArchivo3,ArchivopasswordCifrado):
    frase1 = open(nombreArchivo1,"r").read()
    frase2 = open(nombreArchivo2,"r").read()
    frase3 = open(nombreArchivo3,"r").read()
    frase = frase1 + " " + frase2 + " " + frase3

    passwordCifrado = open(ArchivopasswordCifrado,"r").read()
    L_letras, L_frecuencias = crearListasPorFrecuencia(frase)
    #print(L_letras,"\n",L_frecuencias)
    L_ordenada = ordenarLFrecuencias(L_letras,L_frecuencias)
    #print(L_ordenada)
    L_frecuencias.sort()
    #print(L_frecuencias[::-1])
    d_crifrado = genDiccCifrado(L_ordenada,L_letras_frecuentes_english)
    #print(d_crifrado)
    password = ""
    for letra in passwordCifrado:
        if letra!=" ":
            password+=d_crifrado[letra]
        else:
            password+=" "
    return password
####
frase1 = "found1"#input("Ingrese el nombre del archivo 1: ")
frase2 = "found2" #input("Ingrese el nombre del archivo 2: ")
frase3 = "found3" #input("Ingrese el nombre del archivo 3: ")

nombreCifrado = "krypton4"
#
L_original = "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper().split()
L_clave = "b o i h g k n q v t w y u r x z a j e m s l d f p c".upper().split()
d2 = {}

for i in range(len(L_original)):
	d2[L_original[i]] = L_clave[i]

#
#L_letras, L_frecuencias = crearListasPorFrecuencia(frase)
#L_ordenada = ordenarLFrecuencias(L_letras,L_frecuencias)
#d_crifrado = genDiccCifrado(L_ordenada,L_letras_frecuentes_english)
claveLevel3_4Krypton(frase1,frase2,frase3,nombreCifrado)
