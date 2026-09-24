# DIS-001 - Diseño del Sistema PacoCremas

## Información del elemento de configuración

- Código del CI: DIS-001
- Nombre: Diseño del Sistema
- Proyecto: PacoCremas
- Versión: 1.1
- Estado: Completado por CR-001
- Fecha: 23/09/2026
- Responsable: Equipo PacoCremas
- Responsable del cambio: BrandonBBlandon

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---------|-------|------------------------|-------------|
| 1.0 | 09/09/2026 | Diseño inicial del sistema | Equipo PacoCremas |
| 1.1 | 16/09/2026 | Se agrega el atributo teléfono a la entidad Estudiante según CR-001 | BrandonBBlandon |
| 1.2 | 23/09/2026 | Se agrega el atributo teléfono secundario | BrandonBBlandon |

## 1. Descripción general

PacoCremas se organiza en tres componentes principales:

1. Gestión de estudiantes.
2. Gestión de cursos.
3. Gestión de matrículas.

## 2. Entidades principales

### Estudiante

La entidad Estudiante contiene inicialmente los siguientes atributos:

- identificacion
- nombreCompleto
- correoElectronico
- telefono
- telefono secundario

### Curso

La entidad Curso contiene:

- codigoCurso
- nombreCurso
- numeroCreditos

### Matricula

La entidad Matricula contiene:

- identificacionEstudiante
- codigoCurso
- fechaMatricula

## 3. Relación entre requisitos y diseño

| Requisito | Elemento de diseño asociado |
|-----------|-----------------------------|
| RF-01 Registrar estudiante | Entidad Estudiante (incluye atributo telefono) |
| RF-02 Consultar estudiante | Entidad Estudiante |
| RF-03 Registrar curso | Entidad Curso |
| RF-04 Matricular estudiante | Entidad Matricula |

## 4. Flujo general

### Registro de estudiante

1. El usuario ingresa la información del estudiante.
2. El sistema valida los datos obligatorios.
3. El sistema crea un objeto Estudiante.
4. El sistema almacena la información.

### Registro de curso

1. El usuario ingresa los datos del curso.
2. El sistema valida la información.
3. El sistema almacena el curso.

### Matrícula

1. El usuario selecciona un estudiante.
2. El usuario selecciona un curso.
3. El sistema verifica que ambos existan.
4. El sistema registra la matrícula.

## 5. Trazabilidad de diseño

Este diseño se deriva de los requisitos definidos en el elemento de configuración REQ-001 versión 1.1.

La versión 1.1 de DIS-001 se actualiza como consecuencia de la solicitud de cambio CR-001 - Agregar teléfono al estudiante.
Cualquier modificación que afecte la estructura de estudiantes, cursos o matrículas deberá evaluarse para determinar su impacto sobre este elemento de configuración.