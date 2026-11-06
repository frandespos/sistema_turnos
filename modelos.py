"""
Clases de apoyo: ObraSocial y HorarioAtencion.
"""

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


class ObraSocial:
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre


class HorarioAtencion:
    """Día y horario en que atiende un profesional.
    Lo crea el Profesional y no existe sin él (COMPOSICIÓN)."""

    def __init__(self, dia, hora_inicio, hora_fin, con_turno):
        self.__dia = dia
        self.__hora_inicio = hora_inicio   # "HH:MM"
        self.__hora_fin = hora_fin
        self.__con_turno = con_turno       # True = con turno / False = orden de llegada

    def get_dia(self):
        return self.__dia

    def es_con_turno(self):
        return self.__con_turno

    def incluye_hora(self, hora):
        return self.__hora_inicio <= hora < self.__hora_fin

    def mostrar(self):
        modalidad = "con turno" if self.__con_turno else "orden de llegada"
        return f"{self.__dia} de {self.__hora_inicio} a {self.__hora_fin} ({modalidad})"
