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





uno_dos = estu_prof()
respu_uno_dos = pregunta_reg(uno_dos)
