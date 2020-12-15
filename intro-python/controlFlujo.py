
# Evaluaciones
# a==b
# a > b
# a < b
# a != b
# a <= b
# a >= b

if 2 > 5:
    print('2 es mayor a 5')
elif 2 == 5:
    print('2 es menor que 5') 
else:
    print('ninguna instrucción es válida')

# Diferentes formas de escribir un if
#If de una sola línea
if 2 < 5: print('if de una sola línea')
# if  en una sola línea con un else
print('La devolución es True') if 5 > 2 else print('Cuando la devolción es False')

#simples pruebas
hola_como_estamos = 'bien bro'
y_tu = 'igual bien bro'

if hola_como_estamos == 'mal bro' and y_tu == 'igual bien bro': 
    print('Andamos Embaladísimos')
else: 
    print('¿Qué estamos haciendo mal?')