#Diccionarios y Conjuntos

#Ejemplo de diccionario

diccionario={
    #Llave |:| Valor
    'A':'Letra A',
    'B':'Letra B',
    'C':'Letra C',
    'D':'Letra D'
}
print('Este es el diccionario de las letras: ')
print(diccionario)

#Para recuperar un valor, se proporciona entre [] el valor de la llave.
print('Aqui se mostrara el valor de la llave A:')
print(diccionario['A'])
#Y esto imprimira 'Letra A'. Si se trata de imprimir un valor que no existe se genera un error.
#Pero se puede tratar de recuperar sin que se "rompa" el programa con get()
#Y con , se pone el mensaje que quieras dar por si no existe.
print('Aqui se muestra con .get que no existe una llave o valor dentro del diccionario')
print(diccionario.get('Z','No existe ese valor'))

#Para recuperar las llaves de un diccionario con un ciclo for, seria:
print('Aqui se muestran las llaves de el diccionario: ')
for x in diccionario:
    print(x) 
#Es lo mismo que poner:
print('Aqui se muestran las llaves de el diccionario con .keys() ')
for x in diccionario.keys():
    print(x)

#para recuperar los valores:
print('Aqui se muestran los valores de un diccionario con .values()')
for x in diccionario.values():
    print(x)

#Para recuperar llaves y valores es con 'items'
print('Aqui se muestran los valores de un diccionario con .items()')
for x,y in diccionario.items():
    print(x,y)

#Si quieres agregar un elemento al diccionario se pone la llave y su valor:
diccionario['E']='Letra E'
print('Aqui se muestra que se agrega un nuevo elemento')
print(diccionario)

#Si sobreescribes en una llave, se mantiene la llave pero actualizas su valor
diccionario['E']='Nueva Letra E'
print('Aqui se muestra que se actualizo la ultima llave agregada')
print(diccionario)

#Si quieres eliminar un elemento se usa .pop
diccionario.pop('E')
print('Aqui se muestra que se elimino un elemento con .pop(llave)')
print(diccionario)

#Ahora lo mostrare con un ejercicio donde el usuario tenga que agregar la informacion.
#Primero creamos un diccionario vacio, en este caso hare uno para estudiantes.

estudiantes={}

print('Omite la matricula para salir\n')

#Se crea un ciclo para registrar alumnos hasta que el usuario lo decida.
while True:
    datos = []
    matricula = input('Ingresa la matricula del alumno: ')
    #Si aqui no ingresa la matricula, se sale del ciclo.
    if (matricula == ''):
        break
    #Se valida si ya existe la matricula
    if (estudiantes.get(matricula,'')!=''):
        print('Error, la matricula ya ha sido registrada, intente otra.')
        #El continue nos hara regresar a donde comienza el ciclo.
        continue
    #Se preguntan el resto de datos.
    apellidos = input('Ingresa tus apellidos: ')
    nombre = input('Ingresa el nombre: ')

    #se guardan los datos en las listas.
    datos.append(matricula)
    datos.append(apellidos)
    datos.append(nombre)
    
    #Se guardan los datos en el diccionario.
    estudiantes[matricula]=datos

print('-'*20)
print('Haz salido')

#Para recuperar la informacion de manera organizada se usa un ciclo for con una variable para la llave y el valor

for x,y in estudiantes.items():
    print('Matricula: ',x)
    print('Apellidos: ',y)
    print('Nombre: ',x[1])
    print('-'*25)