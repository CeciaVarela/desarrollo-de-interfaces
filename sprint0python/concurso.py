contI = 0;
contC = 0;

print("1.¿Cuál es la capital de España?")
print("a.Madrid")
print("b.Barcelona")
print("c.Bilbao")
respuesta = input('\nTeclea una opcion: ')
if (respuesta != 'a'):
     print('Respuesta incorrecta')
     contI = contI -5
else:
     print('Respuesta correcta')
     contC = contC + 10
   
   
print("\n2.¿En que comunidad autónoma encontramos el río Miño?")
print("a.Castilla y León")
print("b.Andalucía")
print("c.Galicia")
respuesta = input('\nTeclea una opcion: ')
if (respuesta != 'c'):
     print('Respuesta incorrecta')
     contI = contI - 5
else:
     print('Respuesta correcta')
     contC = contC + 10
     
     
print("\n3.¿Quién fue Picasso?")
print("a.Carpintero")
print("b.Pintor")
print("c.Albañil")
respuesta = input('\nTeclea una opcion: ')
if (respuesta != 'b'):
     print('Respuesta incorrecta')
     contI = contI - 5
else:
     print('Respuesta correcta')
     contC = contC + 10
     

print('\nPuntos respuestas correctas ' + str(contC))
print('\nPuntos respuestas incorrectas ' + str(contI))

     

     
     
     
     

