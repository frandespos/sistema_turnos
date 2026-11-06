"""
HERENCIA: TurnoProgramado y TurnoPorOrden heredan de Turno.
POLIMORFISMO: cada uno redefine mostrar().
ASOCIACIÓN: el turno conoce a un Paciente y a un Profesional.
"""

from abc import ABC, abstractmethod


class Turno(ABC):
    contador = 0   # para numerar los turnos

    def __init__(self, fecha, paciente, profesional):
        Turno.contador += 1
        self.__id = Turno.contador
        self.__fecha = fecha
        self.__paciente = paciente
        self.__profesional = profesional
        self.__activo = True

    def get_id(self):
        return self.__id

    def get_fecha(self):
        return self.__fecha

    def get_paciente(self):
        return self.__paciente

    def get_profesional(self):
        return self.__profesional

    def esta_activo(self):
        return self.__activo

    def cancelar(self):
        self.__activo = False

    def datos_base(self):
        estado = "ACTIVO" if self.__activo else "CANCELADO"
        return (f"#{self.__id} {self.__fecha.strftime('%d/%m/%Y')} - "
                f"{self.__profesional.get_nombre_completo()} "
                f"({self.__profesional.get_especialidad()}) - "
                f"{self.__paciente.get_nombre_completo()} - {estado}")

    @abstractmethod
    def mostrar(self):
        pass


class TurnoProgramado(Turno):
    def __init__(self, fecha, paciente, profesional, hora):
        super().__init__(fecha, paciente, profesional)
        self.__hora = hora

    def get_hora(self):
        return self.__hora

    def mostrar(self):
        return f"[{self.__hora} hs] {self.datos_base()}"


class TurnoPorOrden(Turno):
    def __init__(self, fecha, paciente, profesional, numero):
        super().__init__(fecha, paciente, profesional)
        self.__numero = numero

    def mostrar(self):
        return f"[Orden N° {self.__numero}] {self.datos_base()}"
