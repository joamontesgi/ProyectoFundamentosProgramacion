from cProfile import label
from io import open
from matplotlib import colors
import matplotlib.pyplot as plt
def estu_prof():
    print("INICIO DEL SISTEMA")
    pregunta = int(input("Digite:\n1. Sí es estudiante\n2. Sí es profesor\n"))
    while pregunta < 1 or pregunta > 2:
        pregunta = int(input("### El valor que está ingresando no es válido. ###\nPor favor Digite:\n1. Sí es estudiante\n2. Sí es profesor\n"))
    return pregunta

def pregunta_reg(uno_dos):
    if uno_dos == 2:
        regis_log = int(input("Digite:\n1. Sí ya está resgitrado\n2. Sí aún no está registrado:\n"))
        while regis_log < 1 or regis_log > 2:
            regis_log = int(input("### El valor que está ingresando no es válido ###\n Por favor Digite:\n 1. Sí ya está resgitrado\n2. Sí aún no está registrado:\n"))
        return regis_log
    

def registro(respu_uno_dos):
    if respu_uno_dos == 2:
        regis_contra_profes = open("registro contrseña de profesores.txt", "a")
        regis_ususa_profes = open("registro ususario de profesores.txt", "a")
        print("\nINGRESE LOS SIGUIENTES DATOS PARA SU REGISTRO EN EL SISTEMA")
        nombre = input("Por favor ingrese su nombre: ")
        apellido = input("Por favor ingrese su apellido: ")
        correo = input("Por favor ingrese su correo: ")
        usuario = input("Por favor ingrese un usuario: ")
        contraseña = input("Por favor ingrese una contraseña: ")
        conf_contraseña = input("Vuelva a ingresar la contraseña: ")
        while contraseña != conf_contraseña:
            print("\nLas contraseñas no coinciden, por favor vuelva a ingresarlas\n")
            contraseña = input("Por favor ingrese una contraseña: ")
            conf_contraseña = input("Vuelva a ingresar la contraseña: ")
        print("\nSu registro ha sido correcto, ahora debe de hacer un login para el ingreso al sistema\n")
        regis_ususa_profes.write(usuario+"\n")
        regis_contra_profes.write(contraseña+"\n")
        regis_ususa_profes.close
        regis_contra_profes.close
        return True


def registro_hecho(respu_uno_dos, si_registro):
    if respu_uno_dos == 1 or si_registro == True:
        print("\nHAGA EL INICIO DE SESIÓN PARA EL INGRESO AL SISTEMA\n")
        usuario = input("Por favor ingrese su usuario: ")
        contraseña = input("Por favor digite su contraseña: ")
        archivo_contra = open("registro contrseña de profesores.txt", "r")
        archivo_usua = open("registro ususario de profesores.txt", "r")
        lineas2 = archivo_usua.readlines()
        lineas = archivo_contra.readlines()
        if contraseña+"\n" in lineas and usuario+"\n" in lineas2:
            print("\nSí está registrado\n")
            return True
        elif contraseña+"\n" not in lineas and usuario+"\n" not in lineas2:
            print("La contraseña y usuario son incorrectos")
            while contraseña+"\n" not in lineas or usuario+"\n" not in lineas2:
                contraseña = input("Vuelva a ingresar la contraseña: ")
                usuario = input("Vuelva a ingresar el usuario: ")
            print("\nSí está registrado\n")
            return True
        elif contraseña+"\n" not in lineas:
            while contraseña+"\n" not in lineas:
                contraseña = input(
                    "La contraseña es incorrecta o aún no se encuentra registrado, vuelva a ingresarla: ")
            print("\nSí está registrado\n")
            return True
        elif usuario+"\n" not in lineas2:
            while usuario+"\n" not in lineas2:
                usuario = input(
                    "El usuario es incorrecto o aún no se encuentra registrado, vuelva a ingresarlo: ")
            print("\nSí está registrado\n")
            return True

def ingreso_sistema(si_registro2):
    if si_registro2 == True:
        print('\n### INGRESANDO AL MENÚ ###\n')
        print("HOLA PROFESOR\n")
        opcion = int(input('Ingrese:\n1. Registrar estudiantes e ingresar calificación (nota 1 y 2).\n2. Mostrar la lista de estudiantes.\n3. Generar reporte (Graficas).\n4. Salir del sistema.\n'))
        while opcion < 1 or opcion > 4:
            print("Ingresó un valor no valido, por favor intente de nuevo.\n")
            opcion = int(input(
                'Ingrese:\n1. Registrar estudiantes e ingresar calificación (nota 1 y 2).\n2. Mostrar la lista de estudiantes.\n3. Generar reporte (Graficas).\n4. Salir del sistema.\n'))
    return opcion

def reg_not_estu(opcion):
    if opcion == 1:
        lista_est = open('nombres_estudiante.txt', 'w')
        datos_est = open("datos_estudiante.txt", "w")
        lista_cedula = open("cedulas_estudiante.txt", "w")
        cantidad = int(input('Ingrese la cantidad de estudiantes: '))
        lista_calculo = open("notas_calculo.txt",'w')
        lista_fp=open('notas_fp.txt','w')
        for i in range(cantidad):
            name = input(f'Ingrese el nombre del estudiante {i+1}: ')
            cedula = input(f'Ingrese la cedula el estudiante {i+1}: ')
            nota1 = float(input(f'Ingrese la nota del estudiante {name} en la asignatura CALCULO INTEGRAL: '))
            nota2 = float(input(f'Ingrese la nota del estudiante {name} en la asignatura FUNDAMENTOS DE PROGRAMACIÓN: '))
            diccionario = {'cedula': cedula,'calculo': nota1, 'fundamentos': nota2}
            datos_est.write(str(diccionario)+'\n')
            lista_est.write((name)+'\n')
            lista_cedula.write((cedula)+"\n")
            lista_calculo.write(str(nota1)+'\n')
            lista_fp.write(str(nota2)+'\n')
        print("\nEL REGISTRO DE NOTAS HA SIDO CORRECTO\n")
        datos_est.close()
        lista_est.close()
        lista_cedula.close()
        lista_calculo.close()
        lista_fp.close()
        return lista_calculo, lista_fp

def lista_estu(opcion):
    if opcion == 2:
        lista_est = open('nombres_estudiante.txt', 'r')
        listado = lista_est.readlines()
        print("\nLISTADO DE ESTUDIANTES:\n")
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
        nombre = input('\nIngrese su nombre: ')
        cedula = input('Ingrese su cedula: ')
        listado_est = open('cedulas_estudiante.txt', 'r')
        datos_est = open('datos_estudiante.txt', 'r')
        lista_cedulas = listado_est.readlines()
        lista_notas = datos_est.readlines()
        if cedula+"\n" not in lista_cedulas:
            for i in range(3):
                cedula = input('\nSu cedula no se encuentra registrada o es incorrecta. Ingresela de nuevo: ')
                if cedula+"\n" in lista_cedulas:
                    posicion = lista_cedulas.index(cedula+"\n")
                    print(nombre, "estas son sus notas")
                    print(lista_notas[posicion])
                    break
            print("Usted no se encuentra registrado en el listado de estudiantes")
            return False
        elif cedula+"\n" in lista_cedulas:
            posicion = lista_cedulas.index(cedula+"\n")
            print(nombre, "estas son sus notas:\n")
            print(lista_notas[posicion])
        pregunta=int(input('Ingrese:\n1. Si desea ver el reporte de los estudiantes(Grafico)\n2. Si desea salir del sistema.\n'))
        while pregunta<1 or pregunta>2:
            print('ERROR, Intente nuevamentene.\n')
            pregunta=int(input('Ingrese:\n1. Si desea ver el reporte de los estudiantes(Grafico)\n2. Si desea salir del sistema.\n'))
        if pregunta == 1:
            notasC=[]
            notasFP=[]
            documentos=[]
            nota_cal=open("notas_calculo.txt",'r')
            nota_fp=open('notas_fp.txt','r')
            documento=open('cedulas_estudiante.txt', 'r')
            for i in nota_cal:
                i.strip()
                x=float(i)
                notasC.append(x)
            for i in nota_fp:
                i.strip()
                z=float(i)
                notasFP.append(z)
            for i in documento:
                y=i.strip()
                documentos.append(y)
            fig, ax = plt.subplots()
            ax.bar(documentos, notasC)
            plt.title("GRAFICA DE NOTAS DE CALCULO INTEGRAL")
            plt.show()
            fig, ax = plt.subplots()
            ax.bar(documentos, notasFP)
            plt.title("GRAFICA DE NOTAS DE FUNDAMENTOS DE PROGRAMACION")
            plt.show()  
        return False
def graficas(opcion):
    if opcion==3:
        notasC=[]
        notasFP=[]
<<<<<<< HEAD
        documentos=[]
=======
        nada=[]
>>>>>>> c38aed607ca69273a38058205bd20de439b93c73
        ganaron_cal=0
        ganaron_fp=0
        nota_cal=open("notas_calculo.txt",'r')
        nota_fp=open('notas_fp.txt','r')
        documento=open('cedulas_estudiante.txt', 'r')
        for i in nota_cal:
            i.strip()
            x=float(i)
            notasC.append(x)
            if x>=3:
                ganaron_cal+=1
        for i in nota_fp:
            i.strip()
            z=float(i)
            notasFP.append(z)
            if z>=3:
                ganaron_fp+=1
        for i in documento:
            y=i.strip()
<<<<<<< HEAD
            documentos.append(y)
=======
            nada.append(y)
>>>>>>> c38aed607ca69273a38058205bd20de439b93c73
        tam_cal=len(notasC)
        tam_fp=len(notasFP)
        perdieron_cal=tam_cal-ganaron_cal
        perdieron_fp=tam_fp-ganaron_fp
        fig, ax = plt.subplots()
<<<<<<< HEAD
        ax.bar(documentos, notasC)
        plt.title("GRAFICA DE NOTAS DE CALCULO INTEGRAL")
        plt.show()
        fig, ax = plt.subplots()
        ax.bar(documentos, notasFP)
        plt.title("GRAFICA DE NOTAS DE FUNDAMENTOS DE PROGRAMACION")
        plt.show()
        fig, ax = plt.subplots()
        ax.plot(documentos, notasC, marker = '*')
        ax.plot(documentos, notasFP, marker = '^')
        plt.title("EL AZUL ES CÁLCULO, EL NARANJA ES FUNDAMENTOS")
        plt.show()
        etiquetas=["Ganaron cálculo","Perdieron cálculo"]
        porcentajes=[ganaron_cal, perdieron_cal]
=======
        ax.bar(nada, notasC)
        plt.title("GRAFICA DE NOTAS DE CALCULO INTEGRAL")
        plt.show()
        fig, ax = plt.subplots()
        ax.bar(nada, notasFP)
        plt.title("GRAFICA DE NOTAS DE FUNDAMENTOS DE PROGRAMACION")
        plt.show()
        fig, ax = plt.subplots()
        ax.plot(nada, notasC, marker = '*')
        ax.plot(nada, notasFP, marker = '^')
        plt.title("EL AZUL ES CÁLCULO, EL NARANJA ES FUNDAMENTOS")
        plt.show()
        etiquetas=["Ganaron cálculo","Perdieron cálculo"]
        x=ganaron_cal*100/tam_cal
        porcentajes=[x, perdieron_cal]
>>>>>>> c38aed607ca69273a38058205bd20de439b93c73
        plt.pie(porcentajes, labels=etiquetas)
        plt.title("PROCENTAJES DE CÁLCULO INTEGRAL")
        plt.show()
        etiquetas2=["Ganaron FP","Perdieron FP"]       
<<<<<<< HEAD
        porcentajes2=[ganaron_fp, perdieron_fp]
=======
        Z=ganaron_fp*100/tam_fp
        porcentajes2=[z, perdieron_fp]
>>>>>>> c38aed607ca69273a38058205bd20de439b93c73
        plt.pie(porcentajes2, labels=etiquetas2)
        plt.title("PORCENTAJES DE FUNDAMENTOS DE PROGRAMACIÓN")
        plt.show()
uno_dos = estu_prof()
if opc_estudiante(uno_dos)==False:
    print('\n### FIN DEL SISTEMA ###')
else:
    respu_uno_dos = pregunta_reg(uno_dos)
    si_registro = registro(respu_uno_dos)
    si_registro2 = registro_hecho(respu_uno_dos, si_registro)
    opcion = ingreso_sistema(si_registro2)
    reg_not_estu(opcion)
    lista_estu(opcion)
    graficas(opcion)
    salir(opcion)
    while salir(opcion) == True:
        opcion = ingreso_sistema(si_registro2)
        reg_not_estu(opcion)
        lista_estu(opcion)
        graficas(opcion)
        salir(opcion)
    print('### FIN DEL SISTEMA ###')
