# SRC-001 - Gestión de Estudiantes
# Proyecto: PacoCremas
# Versión: 1.2
# Estado: En modificación por CR-001
# Fecha: 23/09/2026
# Responsable: Equipo PacoCremas
# Responsable del cambio: BrandonBBlandon


class Estudiante:
    def __init__(self, identificacion, nombre_completo, correo_electronico, telefono, telefono_secundario):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.telefono_secundario = telefono_secundario

    def mostrar_informacion(self):
        return {
            "identificacion": self.identificacion,
            "nombre_completo": self.nombre_completo,
            "correo_electronico": self.correo_electronico,
            "telefono": self.telefono,
            "telefono_secundario": self.telefono_secundario
        }


def registrar_estudiante(identificacion, nombre_completo, correo_electronico, telefono, telefono_secundario):
    estudiante = Estudiante(
        identificacion,
        nombre_completo,
        correo_electronico,
        telefono,
        telefono_secundario
    )

    return estudiante