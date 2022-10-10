def isnum(j):
	try:
		int(j)
		
	except:
		return False
		return True


def length(j):
	i = 0
	if not (isnum(j)):
		for i in range(len(j)):
			i = i + 1
	elif(isnum(j)):
		return(j)
	return(i)


print(length("Hoy es lunes"))
