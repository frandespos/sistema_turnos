# Sistema de Turnos Médicos

Sistema por consola para registrar pacientes y dar, cancelar y consultar turnos médicos de un consultorio, desarrollado en Python aplicando Programación Orientada a Objetos.

## Cómo ejecutarlo

Requiere Python 3 y Git. No usa librerías externas.

### En Linux o Mac

Clonar el repositorio:

```bash
git clone https://github.com/frandespos/sistema_turnos.git
```

Entrar a la carpeta:

```bash
cd sistema_turnos
```

Ejecutar el programa:

```bash
python3 main.py
```

En Windows, el último paso es `python main.py`.

### Sin Git

Descargar desde el botón verde **Code → Download ZIP**, descomprimir, abrir una terminal dentro de la carpeta y ejecutar `python3 main.py` (Linux o Mac) o `python main.py` (Windows).

## Datos de acceso

- **Usuario:** admin
- **Contraseña:** 1234

Al iniciar, el sistema ya tiene cargados 4 profesionales (clínica médica, pediatría, cardiología y fonoaudiología) y 3 pacientes (DNI 30111222, 40222333 y 45333444) para poder probarlo.

## Estructura

```
sistema_turnos/
├── main.py           Login, menú principal y datos iniciales
├── consultorio.py    Consultorio
├── personas.py       Persona, Paciente, Profesional
├── turnos.py         Turno, TurnoProgramado, TurnoPorOrden
└── modelos.py        ObraSocial, HorarioAtencion
```

## Conceptos de POO aplicados

- **Encapsulamiento:** todos los atributos son privados y se acceden con métodos.
- **Herencia:** Paciente y Profesional heredan de Persona; TurnoProgramado y TurnoPorOrden heredan de Turno.
- **Polimorfismo:** cada subclase redefine `mostrar_datos()` o `mostrar()`.
- **Asociación:** Turno vincula un Paciente con un Profesional.
- **Agregación:** Consultorio contiene profesionales y pacientes creados afuera.
- **Composición:** Consultorio crea sus turnos y Profesional crea sus horarios de atención; no existen sin ellos.
