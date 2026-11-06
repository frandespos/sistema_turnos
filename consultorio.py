"""
AGREGACIÓN: el Consultorio tiene Profesionales y Pacientes que se crean afuera
            y existen por su cuenta.
COMPOSICIÓN: los Turnos se crean solo acá adentro (en dar_turno).
"""

from turnos import TurnoProgramado, TurnoPorOrden


class Consultorio:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__profesionales = []   # AGREGACIÓN
        self.__pacientes = []       # AGREGACIÓN
        self.__turnos = []          # COMPOSICIÓN

    def get_nombre(self):
        return self.__nombre

    def agregar_profesional(self, profesional):
        self.__profesionales.append(profesional)

    def get_profesionales(self):
        return self.__profesionales

    def registrar_paciente(self, paciente):
        if self.buscar_paciente(paciente.get_dni()):
            raise ValueError("Ya existe un paciente con ese DNI.")
        self.__pacientes.append(paciente)

    def buscar_paciente(self, dni):
        for paciente in self.__pacientes:
            if paciente.get_dni() == dni:
                return paciente
        return None

    def turnos_del_dia(self, profesional, fecha):
        return [t for t in self.__turnos
                if t.get_profesional() == profesional
                and t.get_fecha() == fecha and t.esta_activo()]

    def dar_turno(self, paciente, profesional, fecha, hora=None):
        horario = profesional.horario_del_dia(fecha)
        if horario is None:
            raise ValueError("El profesional no atiende ese día.")

        if not profesional.acepta_obra_social(paciente.get_obra_social()):
            raise ValueError("El profesional no atiende esa obra social.")

        if horario.es_con_turno():
            if not horario.incluye_hora(hora):
                raise ValueError("La hora está fuera del horario de atención.")
            for t in self.turnos_del_dia(profesional, fecha):
                if t.get_hora() == hora:
                    raise ValueError("Ese horario ya está ocupado.")
            turno = TurnoProgramado(fecha, paciente, profesional, hora)
        else:
            numero = len(self.turnos_del_dia(profesional, fecha)) + 1
            turno = TurnoPorOrden(fecha, paciente, profesional, numero)

        self.__turnos.append(turno)
        return turno

    def cancelar_turno(self, id_turno):
        for turno in self.__turnos:
            if turno.get_id() == id_turno and turno.esta_activo():
                turno.cancelar()
                return turno
        raise ValueError("No existe un turno activo con ese número.")

    def turnos_de_la_fecha(self, fecha):
        return [t for t in self.__turnos if t.get_fecha() == fecha]
