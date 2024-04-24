

def registro():

    BD = open('BaseDeDatos.txt', 'r')
    Usuario = input('Cree su usuario nuevo: ')
    Contraseña = input('Cree su contraseña nueva: ')
    CheckContraseña = input('Confirme la contraseña: ')

    Lusuario = []

    Lcontraseña = []


    for i in BD:
        x,y = i.split(", ")
        y = y.strip()
        Lusuario.append(x)
        Lcontraseña.append(y)
    info = dict(zip(Lusuario, Lcontraseña))
    

    if Contraseña != CheckContraseña:
        print('Contraseñas no coinciden, reintente ingresar otra vez')
        registro()
    else:
        if len(Contraseña) <= 6:
            print('Contraseña muy corta, reintente ingresar otra vez')
            registro()
        elif Usuario in Lusuario:
            print('Usuario ya existente, use otro usuario')
            registro()
        else:
            BD = open('BaseDeDatos.txt', 'a')
            BD.write(Usuario+', '+Contraseña+'\n')
            print('Registrado con exito')
            Menu()


def acceso():

    BD = open('BaseDeDatos.txt', 'r')
    Usuario = input('Ingrese su usuario: ')
    Contraseña = input('Ingrese su contraseña: ')

    if not len(Usuario or Contraseña) < 1:

        Lusuario = []

        Lcontraseña = []


        for i in BD:
            x,y = i.split(", ")
            y = y.strip()
            Lusuario.append(x)
            Lcontraseña.append(y)
        info = dict(zip(Lusuario, Lcontraseña))


        try:
            if info[Usuario]:
                try:
                    if Contraseña == info[Usuario]:
                        print('ingreso con exito')
                    else:
                        print('Usuario o Contraseña incorrectos')
                except:
                    print('Usuario o Contraseña incorrectos')
            else:
                print('Usuario no existe')
        except:
            print('Error en el sistema')
                    

def Menu():

    BD = open('BaseDeDatos.txt', 'r')

    Lusuario = []
    Lcontraseña = []

    for i in BD:
        x,y = i.split(", ")
        y = y.strip()
        Lusuario.append(x)
        Lcontraseña.append(y)
    info = dict(zip(Lusuario, Lcontraseña))

    print('Ingrese (1) para Iniciar sesión: ')
    print('Ingrese (2) para Registrar un Usuario: ')
    print('Ingrese (3) para mostrar los usuarios: ')
    print('Ingrese (4) para finalizar: ')

    Loop = input('Ingrese su opción: ')

    if Loop == ('1'):
        acceso()
    elif Loop == ('2'):
        registro()
    elif Loop == ('3'):
        print(info)
    elif Loop == ('4'):
        print('Aplicación finalizada')
    else:
        print('valor ingresado no coincide con ninguna opción, vuelva a intentarlo')
        Menu()
    
    
        
Menu()


    
    
    




    




