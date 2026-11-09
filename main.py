"""
Sistema de Turnos Médicos
Parcial domiciliario - Algoritmos y Estructuras de Datos III

Ejecutar:  python3 main.py
Usuario: admin   Contraseña: 1234
"""

from datetime import datetime
from getpass import getpass

from consultorio import Consultorio
from modelos import ObraSocial
from personas import Paciente, Profesional

USUARIO = "admin"
CONTRASENA = "1234"

PAMI = ObraSocial("PAMI")
IOMA = ObraSocial("IOMA")
AGREMIACION = ObraSocial("Agremiación Médica")
PARTICULAR = ObraSocial("Particular")
OBRAS_SOCIALES = [PAMI, IOMA, AGREMIACION, PARTICULAR]


def cargar_datos():
    consultorio = Consultorio("Consultorio Médico El Toboso")

    clinica = Profesional("Valeria", "Segurado", "20111111", "Médico clínico")
    clinica.agregar_obra_social(PAMI)
    clinica.agregar_obra_social(AGREMIACION)
    clinica.agregar_obra_social(PARTICULAR)
    clinica.agregar_horario("martes", "09:00", "15:00", con_turno=True)
    clinica.agregar_horario("jueves", "09:00", "15:00", con_turno=True)

    pediatra = Profesional("Karina", "Estilarte", "20222222", "Pediatría")
    pediatra.agregar_obra_social(AGREMIACION)
    pediatra.agregar_obra_social(PARTICULAR)
    pediatra.agregar_horario("martes", "09:00", "14:00", con_turno=False)
    pediatra.agregar_horario("jueves", "09:00", "14:00", con_turno=False)

    cardiologo = Profesional("Pablo", "Guenaga", "20333333", "Cardiología")
    cardiologo.agregar_obra_social(PAMI)
    cardiologo.agregar_obra_social(AGREMIACION)
    cardiologo.agregar_obra_social(PARTICULAR)
    cardiologo.agregar_horario("lunes", "09:00", "12:00", con_turno=False)

    fono = Profesional("Claudia", "Arcaro", "20444444", "Fonoaudiología")
    fono.agregar_obra_social(IOMA)
    fono.agregar_obra_social(PARTICULAR)
    fono.agregar_horario("lunes", "09:00", "12:00", con_turno=True)
    fono.agregar_horario("viernes", "09:00", "12:00", con_turno=True)

    for profesional in [clinica, pediatra, cardiologo, fono]:
        consultorio.agregar_profesional(profesional)

    consultorio.registrar_paciente(Paciente("Juan", "Pérez", "30111222", PAMI))
    consultorio.registrar_paciente(Paciente("Ana", "Gómez", "40222333", IOMA))
    consultorio.registrar_paciente(Paciente("Lucía", "Martínez", "45333444", AGREMIACION))
    return consultorio


# ---------- Funciones auxiliares ----------

def elegir(opciones, titulo):
    """Muestra una lista numerada. Acepta el número o el nombre.
    Vuelve a preguntar si la opción es inválida. Enter vacío = cancelar."""
    print(titulo)
    for i, texto in enumerate(opciones, start=1):
        print(f"  {i}. {texto}")
    while True:
        eleccion = input("Opción (número o nombre, Enter para cancelar): ").strip()
        if eleccion == "":
            return None
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
            return int(eleccion) - 1
        for i, texto in enumerate(opciones):
            if eleccion.lower() in texto.lower():
                return i
        print("Opción inválida, probá de nuevo.")


def pedir_fecha():
    try:
        return datetime.strptime(input("Fecha (dd/mm/aaaa): "), "%d/%m/%Y").date()
    except ValueError:
        print("Fecha inválida.")
        return None


def pedir_hora():
    """Acepta 9:30 o 09:30 y la devuelve siempre como HH:MM."""
    try:
        return datetime.strptime(input("Hora (HH:MM): ").strip(), "%H:%M").strftime("%H:%M")
    except ValueError:
        print("Hora inválida.")
        return None


# ---------- Opciones del menú ----------

def registrar_paciente(consultorio):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    i = elegir([o.get_nombre() for o in OBRAS_SOCIALES], "Obra social:")
    if i is None:
        return
    try:
        paciente = Paciente(nombre, apellido, dni, OBRAS_SOCIALES[i])
        consultorio.registrar_paciente(paciente)
        print("Registrado ->", paciente.mostrar_datos())
    except ValueError as error:
        print("Error:", error)


def dar_turno(consultorio):
    paciente = consultorio.buscar_paciente(input("DNI del paciente: "))
    if paciente is None:
        print("No existe ese paciente.")
        return
    profesionales = consultorio.get_profesionales()
    i = elegir([f"{p.get_nombre_completo()} ({p.get_especialidad()})" for p in profesionales],
               "Profesional:")
    if i is None:
        return
    profesional = profesionales[i]
    print(profesional.mostrar_datos())
    fecha = pedir_fecha()
    if fecha is None:
        return
    hora = None
    horario = profesional.horario_del_dia(fecha)
    if horario and horario.es_con_turno():
        hora = pedir_hora()
        if hora is None:
            return
    try:
        turno = consultorio.dar_turno(paciente, profesional, fecha, hora)
        print("Turno asignado ->", turno.mostrar())
    except ValueError as error:
        print("No se pudo dar el turno:", error)


def cancelar_turno(consultorio):
    numero = input("Número de turno a cancelar: ")
    if not numero.isdigit():
        print("Número inválido.")
        return
    try:
        turno = consultorio.cancelar_turno(int(numero))
        print("Cancelado ->", turno.mostrar())
    except ValueError as error:
        print("Error:", error)


def ver_turnos(consultorio):
    fecha = pedir_fecha()
    if fecha is None:
        return
    turnos = consultorio.turnos_de_la_fecha(fecha)
    if not turnos:
        print("No hay turnos ese día.")
    for turno in turnos:
        print(turno.mostrar())   # POLIMORFISMO: cada tipo de turno se muestra distinto


def ver_profesionales(consultorio):
    for profesional in consultorio.get_profesionales():
        print(profesional.mostrar_datos())   # POLIMORFISMO


# ---------- Programa principal ----------

def login():
    print("===== SISTEMA DE TURNOS MÉDICOS =====")
    for _ in range(3):
        usuario = input("Usuario: ")
        contrasena = getpass("Contraseña: ")
        if usuario == USUARIO and contrasena == CONTRASENA:
            return True
        print("Datos incorrectos.")
    return False


def main():
    if not login():
        print("Acceso bloqueado.")
        return
    consultorio = cargar_datos()
    opciones = [
        ("Registrar paciente", registrar_paciente),
        ("Dar turno", dar_turno),
        ("Cancelar turno", cancelar_turno),
        ("Ver turnos del día", ver_turnos),
        ("Ver profesionales", ver_profesionales),
    ]
    while True:
        print(f"\n===== {consultorio.get_nombre()} =====")
        for i, (texto, _) in enumerate(opciones, start=1):
            print(f"  {i}. {texto}")
        print("  0. Salir")
        opcion = input("Opción: ")
        if opcion == "0":
            print("Hasta luego.")
            break
        if opcion.isdigit() and 1 <= int(opcion) <= len(opciones):
            print()
            opciones[int(opcion) - 1][1](consultorio)
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()