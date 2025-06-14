# Trabajo-Practico-6-Grupo-4_Fern-ndezCalder-n_NespolaMangariello
Este repositorio contiene la implementación del **Punto 3** del Trabajo Práctico N.º 6 de la materia **Informática Médica (16.22)** de la carrera de Bioingeniería.

El objetivo principal de este trabajo es demostrar cómo utilizar el estándar **FHIR** mediante programación en **Python**, generando recursos clínicos estructurados e interoperables. Para ello, se utiliza la librería `fhir.resources` junto con `requests`, y se trabaja con el servidor público de **HAPI FHIR**.

---

## Contenidos del repositorio

### Archivos principales:

- `patient_creator.py`:  
  Contiene una función para crear un recurso `Patient`, con atributos como nombre, género, fecha de nacimiento, teléfono e identificador (DNI). Este recurso puede imprimirse en JSON o subirse al servidor HAPI.

- `upload_and_search.py`:  
  Incluye funciones para:
  - Subir el paciente creado al servidor HAPI FHIR (`POST`).
  - Buscar pacientes por número de documento (`identifier`) utilizando la API REST del servidor.

- `careteam_creator.py`:  
  Genera un recurso `CareTeam` asociado al paciente previamente creado. Este equipo de atención incluye un participante con rol clínico y simula un caso real de atención multidisciplinaria. El recurso se sube al servidor y puede visualizarse online.

- `README.md`:  
  Este archivo, con la descripción del trabajo y guía de uso.

---

## Actividades implementadas (TP6 - Punto 3)

### a. Crear un recurso Patient

Se creó un recurso `Patient` con los siguientes datos de ejemplo:

- Nombre: María Victoria Nespola  
- Género: femenino  
- Fecha de nacimiento: 04/10/2002  
- Teléfono: 11-5064-0223  
- Documento: 44452287  
- Sistema de identificación: [Renaper](https://www.argentina.gob.ar/interior/renaper)

### b. Buscar paciente por documento

Se desarrolló un método que permite buscar pacientes en el servidor HAPI FHIR utilizando el campo `identifier`. Esto permite validar que el paciente fue cargado correctamente.

### c. Crear recurso CareTeam

Se creó un recurso `CareTeam` con:

- Nombre del equipo: "Equipo de atención cardiovascular"  
- Estado: `active`  
- Referencia al paciente creado anteriormente  
- Participante: una médica cardióloga con rol clínico asignado

---
