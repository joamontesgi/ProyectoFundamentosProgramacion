from io import open
def estu_prof():
    pregunta = int(input("Por favor digite 1 sí es estudiante, o 2 sí es profesor: "))
    while pregunta < 1 or pregunta > 2:
        pregunta = int(input("El valor que está dando no es válido, digite 1 sí es estudiante, o 2 sí es profesor: "))
    return pregunta

def pregunta_reg(uno_dos):
    if uno_dos == 2:
        regis_log = int(input("Digite 1 sí ya está resgitrado, o digíte 2 sí aún no está registrado: "))
        while regis_log < 1 or regis_log > 2:
            regis_log = int(input("El valor que está dando no es válido, digite 1 sí ya está resgitrado, o digíte 2 sí aún no está registrado: "))
        return regis_log

def registro(respu_uno_dos):
    if respu_uno_dos == 2:
        print("INGRESE LOS SIGUIENTES DATOS PARA SU REGISTRO EN EL SISTEMA")
        nombre=input("Por favor ingrese su nombre: ")
        apellido=input("Por favor ingrese su apellido: ")
        correo = input("Por favor ingrese su correo: ")
        usuario = input("Por favor ingrese un usuario: ")
        contraseña = input("Por favor ingrese una contraseña: ")
        conf_contraseña = input("Vuelva a ingresar la contraseña: ")
        while contraseña != conf_contraseña:
            print("Las contraseñas no coinciden, por favor vuelva a ingresarlas")
            contraseña = input("Por favor ingrese una contraseña: ")
            conf_contraseña = input("Vuelva a ingresar la contraseña: ")
        print("Su registro ha sido correcto, ahora debe de hacer un log in para el ingreso al sistema")
        dicc_regis={"usuario": usuario, "contraseña": contraseña}
        return dicc_regis, True

def login(respu_uno_dos, dicc_P, si_reg):
    if respu_uno_dos == 1:
        print("No se ha registrado aún, por favor registrese")
    elif si_reg == True:
        usuario = input("Por favor ingrese su usuario: ")
        contraseña = input("Por favor ingrese su contraseña: ")
        while (usuario != dicc_P["usuario"] or contraseña != dicc_P["contraseña"]):
            if usuario != dicc_P["usuario"] and contraseña != dicc_P["contraseña"]:
                print("Su usuario y contraseña son incorrectas")
                usuario = input("Por favor vuelva a ingresar su usuario: ")
                contraseña = input("Por favor vuelava a ingresar su contraseña: ")
            elif usuario != dicc_P["usuario"]:
                print("Su usuario es incorrrecto")
                usuario = input("Por favor vuelva e ingrese su usuario: ")
            elif contraseña != dicc_P["contraseña"]:
                print("Su contraseña es incorrecta")
                contraseña = input("Por favor vuelva e ingrese su contraseña: ")
        else:
            return True
 

def ingreso_plat(usuario_regis, matriz):
    print("USTED HA INGRESADO A LA PLATAFORMA CORRECTAMENTE")
    cant_estu=int(input("Por favor ingrese la cantidad de estudiantes que desea registrar y calificar: "))
    for i in range(cant_estu):
        matriz.append([0]*3)
    for i in range(cant_estu):
        for j in range(3):
            matriz[i][j]=input(f"Ingrese el número de ID del estudiante {i+1} y la nota 1 y 2: ")
    for i in matriz:
        print(i)
    
    
    
matriz=[]
uno_dos = estu_prof()
respu_uno_dos = pregunta_reg(uno_dos)
dicc_P, si_reg = registro(respu_uno_dos)
usuario_regis = login(respu_uno_dos, dicc_P, si_reg)
ingreso_plat(usuario_regis, matriz)




         