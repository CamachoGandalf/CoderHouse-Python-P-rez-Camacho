

def registro():
    
    #Toma el txt 'BaseDeDatos' y lee la info.
    BD = open('BaseDeDatos.txt', 'r')
    users = input('Cree su usuario nuevo: ')
    password = input('Cree su contraseña nueva: ')
    check_password = input('Confirme la contraseña: ')

    login_user = []

    login_password = []

    #La info dentro del txt 'BaseDeDatos' esta ingresada con una separación de ', '.
    #Hacemos split y lo guardamos dentro de una lista y luego lo transformamos en diccionario.
    for i in BD:
        x,y = i.split(", ")
        y = y.strip()
        login_user.append(x)
        login_password.append(y)
    info = dict(zip(login_user, login_password))
    
    #Hacemo un check entro los dos inputs para ver sus igualdades, luego por si el input es demasiado corto.
    #Por ultimo hace un check por si se encuentra el usuario en el txt 'Base de datos'.
    if password != check_password:
        print('Contraseñas no coinciden, reintente ingresar otra vez')
        registro()
    else:
        if len(password) <= 6:
            print('Contraseña muy corta, reintente ingresar otra vez')
            registro()
        elif users in login_user:
            print('Usuario ya existente, use otro usuario')
            registro()
        else:
            BD = open('BaseDeDatos.txt', 'a')
            BD.write(users+', '+password+'\n')
            print('Registrado con exito')
            Menu()


def acceso():

    #Toma el txt 'BaseDeDatos' y lee la info.
    BD = open('BaseDeDatos.txt', 'r')
    user = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')

    #Check de si hubo un ingreso de información.
    if not len(user or password) < 1:

        login_user = []

        login_password = []


        for i in BD:
            x,y = i.split(", ")
            y = y.strip()
            login_user.append(x)
            login_password.append(y)
        info = dict(zip(login_user, login_password))

        #Check de si en el diccionario 'info' existe el usuario y coincide con contraseña. 
        try:
            if info[user]:
                try:
                    if password == info[user]:
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

    login_user = []
    login_password = []

    for i in BD:
        x,y = i.split(", ")
        y = y.strip()
        login_user.append(x)
        login_password.append(y)
    info = dict(zip(login_user, login_password))

    print('Ingrese (1) para Iniciar sesión: ')
    print('Ingrese (2) para Registrar un Usuario: ')
    print('Ingrese (3) para mostrar los usuarios: ')
    print('Ingrese (4) para finalizar: ')

    option = input('Ingrese su opción: ')

    if option == ('1'):
        acceso()
    elif option == ('2'):
        registro()
    elif option == ('3'):
        print(info)
    elif option == ('4'):
        print('Aplicación finalizada')
    else:
        print('valor ingresado no coincide con ninguna opción, vuelva a intentarlo')
        Menu()



    
    
    




    




