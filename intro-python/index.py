#Acá va un comentario, se ignora el numeral a la derecha
if 2> 3:
    print('2 es mayor a 3')

#if 6> 3:
 #   print('6 es mayor a 3')


x = 5
y = 'Cerdos'

print (x, y)


#poner nombres de acuerdo a los valores que se guardan
correo ='Cerdo@feliz.com'

print (correo)

nombre_usuario = 'Juan Pablo '

#print (nombre_usuario)

# se puede asignar valores a variables de esta manera

a,b,c = 'Pata', 'Pete', 'Piti'

#print (a,b,c)

#También se le puede agregar un mismo valor a varias varibles de la siguiente manera:
valor1 = valor2 = valor3 = 'Chanchito feliz'

#print (valor1, valor2, valor3)

# Python nos permite hacer concatenación con el signo '+'

inicio = 'Hola '
final = 'mundo'

#print (inicio + final)

#----------------Tipos de datos en python--------------------
#Strings
palabra = 'hola mundo' # String
oracion = "Se puede hacer en comillas simples y en comillas dobles" #String
#Números
Entero = 20 #Integer
Decimal = 30.50 # float or double
Complejo = 1j 

#print (palabra, oracion, Entero, Decimal, Complejo)

#---------------Introducción a las listas, son varios datos agrupados dentro de una lista

lista = ['Hola como estamos', 'Como  estas princhecha', 'Mmmmm']
lista2 = lista.copy()
lista.append('ya no te quiero') # agregar un valor a la lista
#lista.clear() #borra los elementos dentro de la lista

#print (lista, lista2.count(3)) #el método count nos sirve para mostrar la cantidad  de veces que se repite el número que especificamos

#print (len(lista), len(lista2)) # el método len nos sirve para mostrar la cantidad de elementos que hay en la lista

largoLista = len(lista)
largoLista2 = len(lista2)

#print (largoLista, largoLista2)

#------------Podemos acceder a los arreglos en particular
#print(lista[1])

#-----------Eliminar elementos de una lista
#lista.pop() # El método pop nos sirve para elimiar el último elemento de nuestra lista
#lista.remove('Hola como estamos')  # El método remove elimina el valor que le especificamos
#print(lista)

#----------Reverse y sort
lista.reverse() #El método reverse nos cambia el orden de nuestra lista de último a primero
lista.sort() #El método sort ordena las listas, pero no se va a poder utilizar cuando los arreglos tienen valores con el mismo tipo de dato
#print(lista)

#----------Tuplas,  a diferencia de las listas, una vez creada ya no nos dejará cambiarlas
tupla = ('hola mundo', 'somos', 'tupla')
# en las tuplas podemos utilizar menos métodos que en las listas, pero se pueden seguir utilizando algunos como 'count()' 
print(tupla.index('hola mundo'))# el método index nos muestra en qué posición de la tupla está el valor especificado

#para poder modificar una tupla, en primer lugar tenemos que convertirla a una lista
listaDeTupla = list(tupla)
#print(listaDeTupla.append('JEJEJE si me agregaste wueeeey'))
#print (listaDeTupla) 

#------------Range
rango = range(6)
#print (rango)

#-----------Diccionarios 
diccionario = {
    "nombre": "Robert",
    "raza": "Persa",
    "edad": 12
}

print(diccionario)
print(diccionario['nombre'])#Acceder a un valor determinado del diccionario
print(diccionario.get('raza'))

diccionario['nombre'] = 'Fluffy' # modigficar un atributo en un diccionario

print(diccionario.get('nombre'))

#------------Profundizamos en los diccionarios
diccionario['color'] = 'negro' #Agregar un nuevo valor a nuestro diccionario

#print(diccionario)

#diccionario.pop('color') # Eliminar un valor en nuestro diccionario

#print(diccionario)

#diccionario.popitem() #Elimina el último valor de nuetro diccionario

del diccionario['color'] #Es lo mismo que eliminar con el método pop

#print(diccionario)

copiaGatito = diccionario.copy() # copia el diccionario en otra variable

copiaGatito2 = dict(diccionario) # es otra manera de copia el diccionario

#print(copiaGatito)

diccionario.clear() # Elimina todos los valores para los diccionarios

#------------ Diccionario anidados y constructor dict
gatitos = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
    "Mamba":{
        "nombre": "Black Mamba",
        "edad" : 12
    }
}

#También podemos realizar el diccionario con variables y para luego asignarlas

fluffy = {
    "nombre": "gato",
    "edad": 4
}

mamba = {
    "nombre": "mamba",
    "edad": 6
}

gatitos2 = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

#print (gatitos2)

#Otra manera de crear diccionarios, podemos utilizar un constructor llamado 'dict'
perritos = dict(nombre="Rocko", edad=6)
#print(perritos)

#------------------Booleanos
#verdadero = True
#falso = False

#print (verdadero, falso)


#----------------------------------------Control de flujo---------------------------------






