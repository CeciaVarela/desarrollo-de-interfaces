def caracter(a):
    if(len(a) > 1):
        return False
    if(len(a) == 1):
        return True
        
def vocal(a):
	vocales = "aeiouáéíóúü"
	if not(caracter(a)):
		for i in range(len(vocales)):
			for j in range(len(a)):
				if (vocales[i] == a):
					return True
				else:
					return False
	elif (caracter(a)):
		print("Es un caracter")
		

vocal("o")
