"""
HERENCIA: Paciente y Profesional heredan de Persona.
POLIMORFISMO: cada uno redefine mostrar_datos().
ENCAPSULAMIENTO: atributos privados (__) con getters.
"""

from abc import ABC, abstractmethod

from modelos import DIAS, HorarioAtencion


class Persona(ABC):
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    def get_dni(self):
        return self.__dni

    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @abstractmethod
    def mostrar_datos(self):
        pass


class Paciente(Persona):
    def __init__(self, nombre, apellido, dni, obra_social):
        super().__init__(nombre, apellido, dni)
        self.__obra_social = obra_social   # ASOCIACIÓN con ObraSocial

    def get_obra_social(self):
        return self.__obra_social

    def mostrar_datos(self):
        return (f"Paciente: {self.get_nombre_completo()} - DNI {self.get_dni()} - "
                f"{self.__obra_social.get_nombre()}")


class Profesional(Persona):
    def __init__(self, nombre, apellido, dni, especialidad):
        super().__init__(nombre, apellido, dni)
        self.__especialidad = especialidad
        self.__obras_sociales = []   # ASOCIACIÓN con ObraSocial
        self.__horarios = []         # COMPOSICIÓN con HorarioAtencion

    def get_especialidad(self):
        return self.__especialidad

    def agregar_obra_social(self, obra_social):
        self.__obras_sociales.append(obra_social)

    def agregar_horario(self, dia, hora_inicio, hora_fin, con_turno):
        # COMPOSICIÓN: el horario se crea acá adentro
        self.__horarios.append(HorarioAtencion(dia, hora_inicio, hora_fin, con_turno))

    def acepta_obra_social(self, obra_social):
        return obra_social in self.__obras_sociales

    def horario_del_dia(self, fecha):
        dia = DIAS[fecha.weekday()]
        for horario in self.__horarios:
            if horario.get_dia() == dia:
                return horario
        return None

    def mostrar_datos(self):
        horarios = ", ".join(h.mostrar() for h in self.__horarios)
        obras = ", ".join(o.get_nombre() for o in self.__obras_sociales)
        return (f"Profesional: {self.get_nombre_completo()} - {self.__especialidad}\n"
                f"   Atiende: {horarios}\n"
                f"   Obras sociales: {obras}")
