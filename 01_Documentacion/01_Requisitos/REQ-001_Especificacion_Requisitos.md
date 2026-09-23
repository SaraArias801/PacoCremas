# REQ-001 - Especificación de Requisitos de PacoCremas

## Información del elemento de configuración

- Código del CI: REQ-001
- Nombre: Especificación de Requisitos
- Proyecto: PacoCremas
- Versión: 1.1
- Estado: - En modificación por CR-001
- Fecha: 16/09/2026
- Responsable: Equipo PacoCremas
- Responsable del cambio: MInerva2026410


## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 09/09/2026 | Creación inicial de la especificación de requisitos | Equipo PacoCremas |
| 1.1 | 16/09/2026 | Se agrega el número de teléfono al estudiante según CR-001 | MInerva2026410 |
| 1.2 | 16/09/2026 | Se agrega el número de teléfono secundario al estudiante según CR-001 | BrandonBBlandon |

## 1. Propósito

PacoCremas es un sistema académico básico destinado a gestionar estudiantes, cursos y matrículas de una institución educativa.

## 2. Alcance

El sistema permitirá registrar y consultar estudiantes, registrar cursos y asociar estudiantes a los cursos disponibles.

## 3. Requisitos funcionales

### RF-01 - Registrar estudiante

El sistema deberá permitir registrar un estudiante con los siguientes datos:

- Número de identificación
- Nombre completo
- Correo electrónico
- Número de teléfono

Criterio de aceptación:

El sistema debe almacenar correctamente la información del estudiante cuando todos los datos obligatorios hayan sido suministrados.

### RF-02 - Consultar estudiante

El sistema deberá permitir consultar la información de un estudiante utilizando su número de identificación.

Criterio de aceptación:

Cuando exista el estudiante, el sistema deberá mostrar sus datos registrados.

### RF-03 - Registrar curso

El sistema deberá permitir registrar un curso indicando:

- Código del curso
- Nombre del curso
- Número de créditos

Criterio de aceptación:

El curso deberá quedar disponible para procesos posteriores de matrícula.

### RF-04 - Matricular estudiante

El sistema deberá permitir asociar un estudiante previamente registrado a un curso existente.

Criterio de aceptación:

La matrícula deberá quedar registrada cuando tanto el estudiante como el curso existan.

## 4. Requisitos no funcionales

### RNF-01 - Usabilidad

La interfaz deberá permitir que las operaciones principales puedan realizarse de manera sencilla por usuarios administrativos.

### RNF-02 - Disponibilidad

El sistema deberá mantener disponible la información almacenada durante su operación normal.

## 5. Observaciones de configuración

Este documento constituye un Elemento de Configuración de Software identificado como REQ-001.

Cualquier modificación posterior a la aprobación de la línea base deberá estar asociada a una solicitud de cambio formal.