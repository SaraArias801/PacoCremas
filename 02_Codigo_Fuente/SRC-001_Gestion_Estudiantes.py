# SRC-001 - Gestión de Estudiantes
# Proyecto: PacoCremas
# Versión: 1.1
# Estado: En modificación por CR-001
# Fecha: 16/09/2026
# Responsable: Equipo PacoCremas
# Responsable del cambio: MInerva2026410


# SRC-001 - Gestión de Estudiantes
# Proyecto: PacoCremas
# Versión: 1.1
# Estado: En modificación por CR-001
# Fecha: 09/09/2026
# Responsable: Equipo PacoCremas


class Estudiante:
    def __init__(self, identificacion, nombre_completo, correo_electronico, telefono):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.telefono = telefono

    def mostrar_informacion(self):
        return {
            "identificacion": self.identificacion,
            "nombre_completo": self.nombre_completo,
            "correo_electronico": self.correo_electronico,
            "telefono": self.telefono
        }


def registrar_estudiante(identificacion, nombre_completo, correo_electronico, telefono):
    estudiante = Estudiante(
        identificacion,
        nombre_completo,
        correo_electronico,
        telefono
    )

    return estudiante