print('****  BIENVENIDO A PLATAFORMA IMC, DONDE PODREMOS CALCULAR TU INDICE DE MASA CORPORAL ****')

nombre = input('¿Cuál es su nombre?')   #Solicitamos el nombre del usuario
if(len(nombre) > 0 and nombre.isalpha): #Condición en caso de que el nombre quede vacio o no sea de tipo string
    print('Gracias ', nombre)
else:
    print('El campo no debe estar vacío y debe ser cadena de texto')
    nombre = input('¿Cuál es su nombre?')

aPaterno = input('¿Cuál es su apellido paterno?')
if(len(aPaterno) > 0 and aPaterno.isalpha):
    print('Bien ', aPaterno)
else:
    print('El campo no debe estar vacío y debe ser cadena de texto')
    aPaterno = input('¿Cuál es su apellido paterno?')

aMaterno = input('¿Cuál es su apellido materno?')
if(aMaterno.isalpha):
    print('Gracias ')

edad = int(input('¿Cuál es su edad?'))
if(edad.is_integer() and edad):
    print('Gracias')
else:
    print('Debe ingresar un número entero')
    edad = int(input('¿Cuál es su edad?'))

peso = float(input('¿Cuál es su peso actual en kg?'))
if(peso):
    print('Gracias')

estatura = float(input('¿Cuál es su estatura actual en mts?'))
if(estatura):
    print('Gracias')

print('**** Hemos recopilado la información necesaria, procedemos a realizar el calculo ***')
imc=peso/(estatura**2)

if(imc > 0 and imc <= 18.9):
    resultado = 'Peso bajo'
elif(imc > 18.9 and imc <= 24.99):
    resultado = 'Peso normal'
elif(imc > 25 and imc <= 29.99):
    resultado = 'Sobrepeso'
elif(imc > 30 and imc <= 34.99):
    resultado = 'Obesidad leve'
elif(imc > 35 and imc <= 39.99):
    resultado = 'Obesidad media'
elif(imc > 40):
    resultado = 'Obesidad mórbida'

print(nombre + aPaterno + aMaterno + 'el resultado de su anális es el siguiente: ')
print('Su edad: ' + str(edad) + 'años')
print('Su peso: ' + str(peso) + 'Kg')
print('Su estatura: ' + str(estatura) + 'm')
print('El índice de masa corporsal obtenido: ' + str(imc))
print('El resultado de su imc nos indica que usted esta con ' + resultado)

