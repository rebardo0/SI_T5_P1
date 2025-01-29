import keyboard

def imprime_tecla(tecla): 
    print(tecla.name)
    
    with open('texto.txt', 'a') as file:
        if tecla.name == 'space':
            file.write(' ')
        else:
            file.write(tecla.name)

keyboard.on_press(imprime_tecla)
keyboard.wait()