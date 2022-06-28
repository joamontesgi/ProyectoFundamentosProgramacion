from io import open
def estu_prof():
    print("INICIO DEL SISTEMA")
    pregunta = int(
        input("Por favor digite 1 sí es estudiante, o 2 sí es profesor: "))
    while pregunta < 1 or pregunta > 2:
        pregunta = int(input(
            "El valor que está dando no es válido, digite 1 sí es estudiante, o 2 sí es profesor: "))
    return pregunta

def pregunta_reg(uno_dos):
    if uno_dos == 2:
        regis_log = int(
            input("Digite 1 sí ya está resgitrado, o digíte 2 sí aún no está registrado: "))
        while regis_log < 1 or regis_log > 2:
            regis_log = int(input(
                "El valor que está dando no es válido, digite 1 sí ya está resgitrado, o digíte 2 sí aún no está registrado: "))
        return regis_log
    

def registro(respu_uno_dos):
    if respu_uno_dos == 2:
        regis_contra_profes = open("registro contrseña de profesores.txt", "a")
        regis_ususa_profes = open("registro ususario de profesores.txt", "a")
        print("INGRESE LOS SIGUIENTES DATOS PARA SU REGISTRO EN EL SISTEMA")
        nombre = input("Por favor ingrese su nombre: ")
        apellido = input("Por favor ingrese su apellido: ")
        correo = input("Por favor ingrese su correo: ")
        usuario = input("Por favor ingrese un usuario: ")
        contraseña = input("Por favor ingrese una contraseña: ")
        conf_contraseña = input("Vuelva a ingresar la contraseña: ")
        while contraseña != conf_contraseña:
            print("Las contraseñas no coinciden, por favor vuelva a ingresarlas")
            contraseña = input("Por favor ingrese una contraseña: ")
            conf_contraseña = input("Vuelva a ingresar la contraseña: ")
        print("Su registro ha sido correcto, ahora debe de hacer un log in para el ingreso al sistema")
        regis_ususa_profes.write(usuario+"\n")
        regis_contra_profes.write(contraseña+"\n")
        regis_ususa_profes.close
        regis_contra_profes.close
        return True


def registro_hecho(respu_uno_dos, si_registro):
    if respu_uno_dos == 1 or si_registro == True:
        print("HAGA EL INICIO DE SESIÓN PARA EL INGRESO AL SISTEMA")
        usuario = input("Por favor ingrese su usuario: ")
        contraseña = input("Por favor digite su contraseña: ")
        archivo_contra = open("registro contrseña de profesores.txt", "r")
        archivo_usua = open("registro ususario de profesores.txt", "r")
        lineas2 = archivo_usua.readlines()
        lineas = archivo_contra.readlines()
        if contraseña+"\n" in lineas and usuario+"\n" in lineas2:
            print("Sí está registrado")
            return True
        elif contraseña+"\n" not in lineas and usuario+"\n" not in lineas2:
            print("La contraseña y usuario son incorrectos")
            while contraseña+"\n" not in lineas or usuario+"\n" not in lineas2:
                contraseña = input("Vuelva a ingresar la contraseña: ")
                usuario = input("Vuelva a ingresar el usuario: ")
            print("Sí está registrado")
            return True
        elif contraseña+"\n" not in lineas:
            while contraseña+"\n" not in lineas:
                contraseña = input(
                    "La contraseña es incorrecta o aún no se encuentra registrado, vuelva a ingresarla: ")
            print("Sí está registrado")
            return True
        elif usuario+"\n" not in lineas2:
            while usuario+"\n" not in lineas2:
                usuario = input(
                    "El usuario es incorrecto o aún no se encuentra registrado, vuelva a ingresarlo: ")
            print("Sí está registrado")
            return True

def ingreso_sistema(si_registro2):
    if si_registro2 == True:
        print("Hola profesor: ")
        opcion = int(input('Ingrese:\n1. Registrar estudiantes e ingresar calificación (nota 1 y 2).\n2. Mostrar la lista de estudiantes.\n3. Generar reporte (Graficas).\n4. Salir del sistema.\n'))
        while opcion < 1 or opcion > 4:
            print("Ingresó un valor no valido, por favor intente de nuevo.")
            opcion = int(input(
                'Ingrese:\n1. Registrar estudiantes e ingresar calificación (nota 1 y 2).\n2. Mostrar la lista de estudiantes.\n3. Generar reporte (Graficas).\n4. Salir del sistema.\n'))
    return opcion

def reg_not_estu(opcion):
    if opcion == 1:
        lista_est = open('nombres_estudiante.txt', 'w')
        datos_est = open("datos_estudiante.txt", "w")
        lista_cedula = open("cedulas_estudiante.txt", "w")
        cantidad = int(input('Ingrese la cantidad de estudiantes: '))
        for i in range(cantidad):
            name = input(f'Ingrese el nombre del estudiante {i+1}: ')
            cedula = input(f'Ingrese la cedula el estudiante {i+1}: ')
            nota1 = float(input(
                f'Ingrese la nota del estudiante {name} en la asignatura CALCULO INTEGRAL: '))
            nota2 = float(input(
                f'Ingrese la nota del estudiante {name} en la asignatura FUNDAMENTOS DE PROGRAMACIÓN: '))
            diccionario = {'cedula': cedula,
                           'calculo': nota1, 'fundamentos': nota2}
            datos_est.write(str(diccionario)+'\n')
            lista_est.write((name)+'\n')
            lista_cedula.write((cedula)+"\n")
        print("EL REGISTRO DE NOTAS HA SIDO CORRECTO")
        datos_est.close()
        lista_est.close()
        lista_cedula.close()

def lista_estu(opcion):
    if opcion == 2:
        lista_est = open('nombres_estudiante.txt', 'r')
        listado = lista_est.readlines()
        print("LISTADO DE ESTUDIANTES:")
        for i in listado:
            print(i.strip())
        lista_est.close()

def salir(opcion):
    valor = True
    if opcion == 4:
        valor = False
    return valor
def opc_estudiante(uno_dos):
    if uno_dos == 1:
        nombre = input('Ingrese su nombre: ')
        cedula = input('Ingrese su cedula: ')
        listado_est = open('cedulas_estudiante.txt', 'r')
        datos_est = open('datos_estudiante.txt', 'r')
        lista_cedulas = listado_est.readlines()
        lista_notas = datos_est.readlines()
        if cedula+"\n" not in lista_cedulas:
            for i in range(3):
                cedula = input('Su cedula no se encuentra registrada, o es incorrecta. Ingresela de nuevo: ')
                if cedula+"\n" in lista_cedulas:
                    posicion = lista_cedulas.index(cedula+"\n")
                    print(nombre, "Estas son sus notas")
                    print(lista_notas[posicion])
                    break
            print("Usted no se encuentra registrado en el listado de estudiantes")
        elif cedula+"\n" in lista_cedulas:
            posicion = lista_cedulas.index(cedula+"\n")
            print(nombre, "Estas son sus notas")
            print(lista_notas[posicion])
    opcion=False
    return opcion

uno_dos = estu_prof()
variable=opc_estudiante(uno_dos)
respu_uno_dos = pregunta_reg(uno_dos)
if variable == False:
    print('Fin del sistema')
else:
    si_registro = registro(respu_uno_dos)
    si_registro2 = registro_hecho(respu_uno_dos, si_registro)
    opcion = ingreso_sistema(si_registro2)
    reg_not_estu(opcion)
    lista_estu(opcion)
    salir(opcion)
    while salir(opcion) == True:
        opcion = ingreso_sistema(si_registro2)
        reg_not_estu(opcion)
        lista_estu(opcion)
        salir(opcion)
