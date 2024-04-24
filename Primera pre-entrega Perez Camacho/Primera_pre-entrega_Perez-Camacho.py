

def registro():

    BD = open('BaseDeDatos.txt', 'r')
    Users = input('Cree su usuario nuevo: ')
    Password = input('Cree su contraseña nueva: ')
    Check_Password = input('Confirme la contraseña: ')

    Login_User = []

    Login_Password = []


    for i in BD:
        x,y = i.split(", ")
        y = y.strip()
        Login_User.append(x)
        Login_Password.append(y)
    info = dict(zip(Login_User, Login_Password))
    

    if Password != Check_Password:
        print('Contraseñas no coinciden, reintente ingresar otra vez')
        registro()
    else:
        if len(Password) <= 6:
            print('Contraseña muy corta, reintente ingresar otra vez')
            registro()
        elif Users in Login_User:
            print('Usuario ya existente, use otro usuario')
            registro()
        else:
            BD = open('BaseDeDatos.txt', 'a')
            BD.write(Users+', '+Password+'\n')
            print('Registrado con exito')
            Menu()


def acceso():

    BD = open('BaseDeDatos.txt', 'r')
    User = input('Ingrese su usuario: ')
    Password = input('Ingrese su contraseña: ')

    if not len(User or Password) < 1:

        Login_User = []

        Login_Password = []


        for i in BD:
            x,y = i.split(", ")
            y = y.strip()
            Login_User.append(x)
            Login_Password.append(y)
        info = dict(zip(Login_User, Login_Password))


        try:
            if info[User]:
                try:
                    if Password == info[User]:
                        print('ingreso con exito')
                    else:
                        print('Usuario o Contraseña incorrectos')
                except:
                    print('Usuario o Contraseña incorrectos')
            else:
                print('Usuario no existe')
        except:
            print('Usuario no existe')
                    

def Menu():

    BD = open('BaseDeDatos.txt', 'r')

    Login_User = []
    Login_Password = []

    for i in BD:
        x,y = i.split(", ")
        y = y.strip()
        Login_User.append(x)
        Login_Password.append(y)
    info = dict(zip(Login_User, Login_Password))

    print('Ingrese (1) para Iniciar sesión: ')
    print('Ingrese (2) para Registrar un Usuario: ')
    print('Ingrese (3) para mostrar los usuarios: ')
    print('Ingrese (4) para finalizar: ')

    Option = input('Ingrese su opción: ')

    if Option == ('1'):
        acceso()
    elif Option == ('2'):
        registro()
    elif Option == ('3'):
        print(info)
    elif Option == ('4'):
        print('Aplicación finalizada')
    else:
        print('valor ingresado no coincide con ninguna opción, vuelva a intentarlo')
        Menu()
    
    
        
Menu()


    
    
    




    




