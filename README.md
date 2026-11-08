# Sistema de Gestión Hospitalaria

## Nombre de los integrantes
- Richard Tabares Botero
- Roger Avila Uribe
- Laura Camila Parra Beltran

## Descripción general del proyecto
Sistema de gestión hospitalaria que permite administrar pacientes, personal de salud, personal administrativo, servicios y facturación. El proyecto aplica los conceptos de herencia, sobrescritura de métodos, polimorfismo y composición entre clases.

## Estructura de los archivos
```text
actividad_3_final_hospital/
├── main.py                              # Punto de entrada y menú interactivo
├── README.md
├── CHEKLIST.md                          # Lista de verificación del taller
├── Documento_Decisiones_Diseno.md       # Documento de decisiones de diseño
├── .gitignore                           # Archivos y carpetas ignorados por Git
├── controllers/
│   ├── facturacion_controller.py        # Controlador: registra, busca, elimina y lista facturas
│   ├── persona_Controller.py            # Controlador: registra y elimina pacientes, personal de salud y administrativos
│   └── servicioController.py            # Controlador: registra, busca y elimina servicios (citas, exámenes y medicamentos)
└── models/
    ├── persona.py                       # Clase abstracta base: nombre, identificación, correo, teléfono, dirección y nivel de acceso
    ├── paciente.py                      # Hereda de persona: fecha de nacimiento, contacto de emergencia y EPS
    ├── personalSalud.py                 # Hereda de persona: registro profesional, dependencia, especialidad, horas semanales y turno
    ├── administrativo.py                # Hereda de persona: dependencia, cargo y turno
    ├── servicio.py                      # Clase abstracta base: tipo y valor del servicio
    ├── cita.py                          # Hereda de servicio: especialidad de la cita
    ├── examen.py                        # Hereda de servicio: nombre del examen
    ├── medicamento.py                   # Hereda de servicio: nombre, dosis y presentación
    ├── facturacion.py                   # Compuesta por paciente, servicio, personal de salud y administrativo; incluye fecha y total
    └── excepciones.py                   # Excepciones personalizadas para validaciones y facturación
```

## Instrucciones para ejecutar el proyecto
1. Tener instalado **Python 3.10 o superior**. No se requieren librerías externas.
2. Clonar o descargar el repositorio.
3. Ubicarse en la carpeta raíz del proyecto, donde está `main.py`:
   ```
   cd actividad_3_final_hospital
   ```
4. Ejecutar:
   ```
   python main.py
   ```
   (en algunos sistemas el comando es `python3 main.py`).

Al iniciar, el sistema muestra un menú:

==================================================
    SISTEMA DE GESTIÓN HOSPITALARIA - MENÚ PRINCIPAL
==================================================
**********************************************
1. Gestion de usuarios
    1. Pacientes
        1. Registrar paciente
        2. Eliminar paciente
        0. Volver
    2. Personal de salud
        1. Registrar personal salud
        2. Eliminar personal salud
        0. Volver
    3. Personal administrativo
        1. Registrar personal administrativo
        2. Eliminar personal administrativo
        0. Volver
    0. Volver
2. Gestion de servicios
    1. Registrar nuevo servicio
    2. Eliminar servicio
    0. Volver
3. Gestion de facturacion
    1. Registar factura
    2. Eliminar factura
    3. Buscar factura
    0. Volver
4. Reportes
    1. Reporte polimorfico de usuarios
    2. Reporte de servicios
    3. Reporte de facturas
    0. Volver
5. Casos excepcionales
    1. Fecha de nacimiento inválida
    2. Identificación vacía
    3. Servicio obligatorio al facturar
    4. Código de factura inválido
    0. Volver
0. Salir 
>>>Ingrese una opción del 1 a 5:

## Explicación breve de cómo se aplicaron la herencia, la sobre escritura y el polimorfismo

La herencia se aplicó a partir de dos jerarquías. La primera inicia en `persona`, una clase abstracta que reúne los datos comunes (nombre, identificación, correo, teléfono, dirección y nivel de acceso) y declara el método abstracto `mostrar_informacion()`. De ella heredan `paciente`, `personalSalud` y `administrativo`, que agregan atributos propios. La segunda inicia en `servicio`, también abstracta, de la que heredan `cita`, `examen` y `medicamento`. La sobrescritura se evidencia en `mostrar_informacion()`: cada clase hija define su propia versión, llama a `super().mostrar_informacion()` para reutilizar los datos de la clase base y luego imprime sus atributos específicos. El polimorfismo se observa en los reportes: `personaController` almacena objetos de los tres tipos de persona en una sola lista y `reporte_personas()` recorre la lista ejecutando `p.mostrar_informacion()`; del mismo modo, `servicioController` almacena citas, exámenes y medicamentos y `reporte_servicios()` los trata como objetos `servicio`. Así, una misma llamada ejecuta el comportamiento correspondiente al tipo real del objeto.

## Relación de composición entre factura y servicio

La composición se aplicó en `facturacion`, que no almacena solo códigos sino referencias a objetos completos: `paciente`, `servicio`, `personalSalud` y `administrativo`. El constructor recibe esas instancias y las guarda en `_paciente`, `_servicio`, `_personalSalud` y `_administrativo`; luego `mostrar_informacion()` utiliza sus métodos para obtener el nombre, el tipo de servicio, etc. En `main.py`, al registrar una factura se seleccionan objetos existentes de los controladores y se pasan a `facturacionController.agregar_factura()`, que construye la factura con ellos. Además, `facturacion.set_servicio()` lanza la excepción `ServicioObligatorioAlFacturar` cuando el servicio es `None`, lo que garantiza que no se facture sin un servicio. El servicio puede ser una cita, un examen o un medicamento, y la factura lo utiliza mediante su interfaz común. Por eso la relación es de composición: la factura integra y depende de un servicio, y también de los demás objetos, para existir y mostrar su información.
