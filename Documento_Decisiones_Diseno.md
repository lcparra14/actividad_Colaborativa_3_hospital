# Documento de Decisiones de Diseño

## Sistema de Gestión Hospitalaria

### Actividad N.° 3 Final — Sistema Hospitalario

**Integrantes:**
- Richard Tabares Botero
- Roger Avila Uribe
- Laura Camila Parra Beltran

**Curso:** Programación 1  
**Docente:** Natalia Castellanos
**Universidad:** Universidad de Manizales  
**Facultad / Programa:** Ingeniería en Seguridad de la Información - Ingeniería de Sistemas
**Fecha:** 01 de noviembre de 2026

## 1. Introducción

Un hospital debe administrar pacientes, personal, servicios y facturas. Cuando esa información se maneja de forma manual aumentan los errores, las duplicaciones y el riesgo de facturar servicios incorrectos. Este proyecto centraliza esas operaciones en una aplicación de consola en Python y aplica abstracción, herencia, sobrescritura, polimorfismo y composición.

Permite gestionar usuarios y servicios, crear y buscar facturas, y generar reportes; la información se conserva en listas administradas por controladores.

## 2. Descripción general de la solución

La solución se organizó en tres partes. `models` contiene las clases del dominio; `controllers` almacena y manipula los objetos; y `main.py` implementa el menú, la lectura de datos y los resultados. Así, los modelos no dependen de la consola.

El diseño se apoya en dos jerarquías. De `persona` heredan `paciente`, `personalSalud` y `administrativo`; de `servicio` heredan `cita`, `examen` y `medicamento`. `facturacion` integra objetos de ambas jerarquías mediante composición. Los controladores mantienen listas de objetos y ofrecen operaciones para agregarlos, buscarlos y eliminarlos. `models/excepciones.py` concentra las validaciones del negocio.

## 3. Desarrollo de las decisiones de diseño

### 3.1 Clases principales y responsabilidades

`persona` es la base abstracta de los usuarios y concentra nombre, identificación, correo, teléfono, dirección y nivel de acceso. `paciente` agrega fecha de nacimiento, contacto de emergencia y EPS. `personalSalud` añade registro profesional, dependencia, especialidad, horas semanales y turno. `administrativo` agrega dependencia, cargo y turno.

En la otra jerarquía, `servicio` define el tipo y el valor de una prestación. `cita` agrega la especialidad; `examen`, el nombre del examen; y `medicamento`, nombre, dosis y presentación. `facturacion` relaciona un paciente, un servicio, un miembro del personal de salud y uno del personal administrativo, además de código, fecha y total. Los controladores conservan estas instancias y ejecutan las operaciones del menú.

### 3.2 Clases abstractas

`persona` y `servicio` son abstractas porque representan conceptos generales que no deben instanciarse solos. No tiene sentido crear una persona sin conocer su rol, ni un servicio sin conocer su categoría. Ambas declaran `mostrar_informacion()` como abstracto, lo que obliga a cada subclase a implementar su presentación. `persona` valida la identificación y `servicio` concentra tipo y valor.

### 3.3 Herencia y relación “es un”

La herencia representa una relación “es un”: un paciente es una persona, al igual que un colaborador de salud o administrativo. Por eso las subclases llaman a `super().__init__()` para inicializar los datos comunes y luego agregan los propios. De igual forma, una cita, un examen y un medicamento son servicios porque comparten tipo y valor, aunque se diferencian en su información específica.

Las personas comparten los datos personales, el nivel de acceso, getters, setters y `mostrar_informacion()`. Cada subclase añade atributos y define `realizar_actividad_principal()` según su rol. En los servicios, los datos comunes son `tipoServicio` y `valorServicio`.

### 3.4 Sobrescritura y polimorfismo

El método sobrescrito es `mostrar_informacion()`. En `paciente`, `personalSalud` y `administrativo` se redefine para imprimir primero los datos comunes mediante `super().mostrar_informacion()` y después los específicos. Lo mismo ocurre en `cita`, `examen` y `medicamento`, que reutilizan el método de `servicio` y amplían su salida.

El polimorfismo se evidencia en los reportes. `personaController` guarda los tres tipos de persona en una misma lista y `reporte_personas()` ejecuta `p.mostrar_informacion()` sin comprobar el tipo concreto. Del mismo modo, `servicioController` almacena citas, exámenes y medicamentos, y `reporte_servicios()` los trata como objetos `servicio`. La misma llamada produce una salida distinta según la clase real del objeto.

### 3.5 Composición en facturación

`facturacion` no guarda códigos sueltos, sino referencias a objetos completos. Su constructor recibe un paciente, un servicio, un miembro del personal de salud y uno del personal administrativo, y los conserva en `_paciente`, `_servicio`, `_personalSalud` y `_administrativo`. Luego, `mostrar_informacion()` usa sus métodos para obtener nombre, tipo de servicio y datos del personal. En `main.py` se seleccionan objetos existentes y se pasan a `facturacionController.agregar_factura()`, que construye la factura con ellos.

La factura integra y depende de esas partes para existir. Además, `set_servicio()` lanza `ServicioObligatorioAlFacturar` si el servicio es `None`, lo que impide facturar sin una prestación. El servicio puede ser cita, examen o medicamento, y la factura lo usa mediante su interfaz común.

### 3.6 Excepciones personalizadas

`FechaNacimientoInvalida` se lanza en `paciente.setFechaNacimiento()` cuando la fecha está vacía. `IdentificacionNoPuedeEstarVacia` se lanza en `persona.set_identificacion()` cuando la identificación no contiene caracteres. `ServicioObligatorioAlFacturar` se lanza en `facturacion.set_servicio()` al intentar facturar sin servicio. `CodigoFacturaInvalido` se lanza en `facturacion.set_codigoFactura()` cuando el código está vacío. `main.py` captura estas excepciones para mostrar mensajes claros y evitar cierres abruptos.

### 3.7 Decisiones modificadas durante el desarrollo

Inicialmente, `servicio` era una clase concreta y las citas y exámenes incluían fechas. Luego se convirtió en una clase abstracta y se crearon `cita`, `examen` y `medicamento`, eliminando datos innecesarios. También se modificó `facturacion`: antes guardaba códigos de paciente, servicio y personal; después pasó a guardar objetos completos, lo que permitió implementar la composición.

La excepción `CitasElMismoDia` fue reemplazada por `IdentificacionNoPuedeEstarVacia`, y más adelante se agregó `CodigoFacturaInvalido`. Estos cambios respondieron a la necesidad de validar datos realmente usados y de mantener coherencia entre modelos, controladores y menú.

### 3.8 Verificación

La verificación se realizó ejecutando manualmente `main.py` y recorriendo cada opción del menú. El sistema precarga datos de prueba con `cargar_datos_prueba()`: pacientes, personal de salud, personal administrativo, servicios y facturas. Con ellos se comprobó el registro y eliminación de usuarios, la creación y búsqueda de facturas, los reportes y las validaciones. También se revisó que cada reporte correspondiera al tipo real de los objetos.

## 4. Conclusiones

El desarrollo mostró cómo la abstracción, la herencia y la composición resuelven un problema concreto. Las clases abstractas `persona` y `servicio` evitaron duplicar lógica y obligaron a definir comportamientos claros en las subclases. El polimorfismo facilitó los reportes sobre listas heterogéneas, y la composición permitió que una factura integrara información de varias entidades. Las dificultades estuvieron en integrar modelos, controladores y menús, y en cambiar de códigos a objetos y reorganizar los servicios. El aprendizaje principal fue diseñar primero las relaciones entre clases y validar cada decisión con el código.

## 5. Referencias del proyecto

| Archivo | Contenido citado |
|---|---|
| `models/persona.py` | Clase abstracta y validación de la identificación. |
| `models/paciente.py` | Herencia, validación de fecha y actividad principal. |
| `models/personalSalud.py` | Herencia, atributos clínicos y actividad principal. |
| `models/administrativo.py` | Herencia, datos laborales y actividad principal. |
| `models/servicio.py` | Clase abstracta y atributos comunes. |
| `models/cita.py` | Especialidad y sobrescritura de `mostrar_informacion()`. |
| `models/examen.py` | Nombre del examen y sobrescritura. |
| `models/medicamento.py` | Datos del medicamento y sobrescritura. |
| `models/facturacion.py` | Composición y validaciones de facturación. |
| `models/excepciones.py` | Excepciones del dominio hospitalario. |
| `controllers/persona_Controller.py` | Lista heterogénea y registro/eliminación. |
| `controllers/servicioController.py` | Registro, búsqueda y eliminación de servicios. |
| `controllers/facturacion_controller.py` | Registro, búsqueda y eliminación de facturas. |
| `main.py` | Menú, precarga, reportes y excepciones. |
| `README.md` | Explicación de herencia, polimorfismo y composición. |

## 6. Declaración de uso de inteligencia artificial

Para la elaboración de este documento técnico nos apoyamos en herramientas de inteligencia artificial como apoyo para estudiar y comprender los conceptos de programación orientada a objetos y para la redacción y revisión del texto. Las decisiones de diseño, la implementación del sistema y la verificación de la información presentada fueron realizadas y validadas por los integrantes del equipo.