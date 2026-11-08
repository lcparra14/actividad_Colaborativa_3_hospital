from controllers.facturacion_controller import facturacionController
from controllers.servicioController import servicioController
from controllers.persona_Controller import personaController
from models.excepciones import CodigoFacturaInvalido, FechaNacimientoInvalida, IdentificacionNoPuedeEstarVacia, ServicioObligatorioAlFacturar


def mostrar_menu_principal():
    print("\n==================================================")
    print("    MENÚ PRINCIPAL - SISTEMA DE GESTIÓN HOSPITALARIA")
    print("==================================================")
    print("**********************************************")
    print("1. Gestion de usuarios")
    print("2. Gestion de servicios")
    print("3. Gestion de facturacion")
    print("4. Reportes")
    print("5. Casos excepcionales")
    print("0. Salir")


def menu_usuarios(persona_controller):
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Pacientes")
        print("2. Personal de salud")
        print("3. Personal administrativo")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 3: ").strip()

        match opcion:
            case "1":
                menu_pacientes(persona_controller)
            case "2":
                menu_personal_salud(persona_controller)
            case "3":
                menu_personal_administrativo(persona_controller)
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")


def menu_pacientes(persona_controller):
    
    while True:
        print("\n--- PACIENTES ---")
        print("1. Registrar paciente")
        print("2. Eliminar paciente")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 2: ").strip()

        match opcion:
            
            case "1":
                # Registrar paciente
                print("\n--- Ingrese los datos del paciente ---")
                try:
                    nombre = input("Nombre: ")
                    identificacion = input("Identificación: ")
                     # if not identificacion.strip():
                        #     raise identificacionNoPuedeEstarVacia(identificacion)
                    correo = input("Correo electrónico: ")
                    telefono = input("Número de teléfono: ")
                    direccion = input("Dirección de residencia: ")
                    nivelDeAcceso = "paciente"  # Nivel de acceso fijo para pacientes
                    fechaNacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
                    # if not fechaNacimiento.strip():
                    #     raise FechaNacimientoInvalida(fechaNacimiento)
                    contactoEmergencia = input("Contacto de emergencia: ")
                    nombreEps = input("Nombre de la EPS: ")
                
                    persona_controller.agregar_paciente(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, fechaNacimiento, contactoEmergencia, nombreEps)
                    print("Paciente registrado exitosamente.")
                except FechaNacimientoInvalida as e:
                    print(f"Error: {e}")  
                except IdentificacionNoPuedeEstarVacia as e:
                    print(f"Error: {e}")                  
                
                                    
            case "2":
                # Eliminar paciente
                print("\n--- Eliminar paciente ---")
                pacientesDisponibles = [p for p in persona_controller.get_personas()if type(p).__name__ == "paciente"]
                if not pacientesDisponibles:
                    print("No hay pacientes registrados.")
                else:
                    print("\n--- Pacientes disponibles ---")
                    for p, paciente in enumerate(pacientesDisponibles):
                        print(f"{p}. {paciente.get_nombre()} - ID: {paciente.get_identificacion()}")    
                    try:
                        opcion = int(input("\nSeleccione el número del paciente a eliminar: "))
                        pacienteSeleccionado = pacientesDisponibles[opcion]
                    except ValueError as e:
                        print(f"Error:{e}") ("Seleccion de paciente inválida.")
                    try:
                        persona_controller.eliminar_paciente(pacienteSeleccionado.get_identificacion())
                        print("Paciente eliminado exitosamente.")
                    except ValueError as e:
                        print(f"Error:{e}") ("No se encontró un paciente con esa identificación.")
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")
        input("\nPresione una tecla para continuar...")

def menu_personal_salud(persona_controller):
    
    while True:
        print("\n--- PERSONAL DE SALUD ---")
        print("1. Registrar personal salud")
        print("2. Eliminar personal salud")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 2: ").strip()

        match opcion:
            case "1":
                # Registrar personal de salud
                print("\n--- Ingrese los datos del personal de salud ---")
                try: 
                    nombre = input("Nombre: ")
                    identificacion = input("Identificación: ")
                    # if not identificacion.strip():
                    #     raise IdentificacionNoPuedeEstarVacia(identificacion)
                    correo = input("Correo electrónico: ")
                    telefono = input("Número de teléfono: ")
                    direccion = input("Dirección de residencia: ")
                    nivelDeAcceso = "salud"  # Nivel de acceso fijo para personal de salud
                    registroProfesional = input("Registro profesional: ")
                    dependencia = input("Dependencia: ")
                    especialidad = input("Especialidad: ")
                    numeroDeHorasSemanales = input("Número de horas semanales: ")
                    turno = input("Turno de trabajo: ")
                
                    persona_controller.agregar_personalSalud(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, registroProfesional, dependencia, especialidad, numeroDeHorasSemanales, turno)
                    print("Personal de salud registrado exitosamente.")
                except IdentificacionNoPuedeEstarVacia as e:
                    print(f"Error: {e}")
                
                
            case "2":
                # Eliminar personal de salud
                print("\n--- Eliminar personal de salud ---")
                personalSaludDisponibles = [p for p in persona_controller.get_personas() if type(p).__name__ == "personalSalud"]
                if not personalSaludDisponibles:
                    print("No hay personal de salud registrado.")
                else:
                    print("\n--- Personal de salud disponible ---")
                    for p, personalSalud in enumerate(personalSaludDisponibles):
                        print(f"{p}. {personalSalud.get_nombre()} - ID: {personalSalud.get_identificacion()}")
                    try:
                        opcion = int(input("\nSeleccione el número del personal de salud a eliminar: "))
                        personalSaludSeleccionado = personalSaludDisponibles[opcion]
                    except (ValueError, IndexError) as e:
                        print(f"Error:{e}") ("Seleccion de personal de salud inválida.")
                    try:
                        persona_controller.eliminar_personalSalud(personalSaludSeleccionado.get_identificacion())
                        print("Personal de salud eliminado exitosamente.")
                    except ValueError as e:
                        print(f"Error:{e}") ("No se encontró un personal de salud con esa identificación.")        
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")
        input("\nPresione una tecla para continuar...")

def menu_personal_administrativo(persona_controller):
        
    while True:
        print("\n--- PERSONAL ADMINISTRATIVO ---")
        print("1. Registrar personal administrativo")
        print("2. Eliminar personal administrativo")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 2: ").strip()

        match opcion:
            case "1":
                # Registrar personal administrativo
                print("\n--- Ingrese los datos del personal administrativo ---")
                try:
                    nombre = input("Nombre: ")
                    identificacion = input("Identificación: ")
                    # if not identificacion.strip():
                    #     raise IdentificacionNoPuedeEstarVacia(identificacion)
                    correo = input("Correo electrónico: ")
                    telefono = input("Número de teléfono: ")
                    direccion = input("Dirección de residencia: ")
                    nivelDeAcceso = "admin"  # Nivel de acceso fijo para personal administrativo
                    dependencia = input("Dependencia: ")
                    cargo = input("Cargo: ")
                    turno = input("Turno de trabajo: ") 
                
                    persona_controller.agregar_adminitrativo(nombre, identificacion, correo, telefono, direccion, nivelDeAcceso, dependencia, cargo, turno)
                    print("Personal administrativo registrado exitosamente.")
                except IdentificacionNoPuedeEstarVacia as e:
                    print(f"Error: {e}")
                
            case "2":
                # Eliminar personal administrativo
                print("\n--- Eliminar personal administrativo ---")
                personalAdministrativoDisponibles = [p for p in persona_controller.get_personas() if type(p).__name__ == "administrativo"]
                if not personalAdministrativoDisponibles:
                    print("No hay personal administrativo registrado.")
                else:
                    print("\n--- Personal administrativo disponible ---")
                    for p, personalAdministrativo in enumerate(personalAdministrativoDisponibles):
                        print(f"{p}. {personalAdministrativo.get_nombre()} - ID: {personalAdministrativo.get_identificacion()}")
                    try:
                        opcion = int(input("\nSeleccione el número del personal administrativo a eliminar: "))
                        personalAdministrativoSeleccionado = personalAdministrativoDisponibles[opcion]
                    except (ValueError, IndexError) as e:
                        print(f"Error:{e}") ("Seleccion de personal administrativo inválida.")
                    try:
                        persona_controller.eliminar_administrativo(personalAdministrativoSeleccionado.get_identificacion())
                        print("Personal administrativo eliminado exitosamente.")
                    except ValueError as e:
                        print(f"Error:{e}") ("No se encontró un personal administrativo con esa identificación.")
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")
        input("\nPresione una tecla para continuar...")


def menu_servicios(servicio_controller):
    while True:
        print("\n--- SERVICIOS ---")
        print("1. Registrar nuevo servicio")
        print("2. Eliminar servicio")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 2: ").strip()

        match opcion:
            case "1":
                # Registrar servicio
                print("\nCategoría del servicio:")
                print("1. Cita")
                print("2. Examen")
                print("3. Medicamento")
                categoria = input(">>>Ingrese una categoría del 1 a 3: ").strip()
                if categoria not in ["1", "2", "3"]:
                    print("Categoría inválida. Intente de nuevo.")
                    continue

                # Datos comunes

                # Datos propios de cada categoría
                match categoria:
                    case "1":
                        if servicio_controller.buscar_servicio("Cita") is not None:
                            print("Ya existe un servicio de tipo Cita.")
                            break
                        valor_servicio = int(input("Valor del servicio (sin puntos ni comas): "))
                        especialidad = input("Especialidad de la cita: ")
                        #fecha = input("Fecha y hora de la cita (YYYY-MM-DD HH:MM): ")
                        try:
                            servicio_controller.agregar_servicioCita("Cita", valor_servicio, especialidad)
                            print("Servicio de tipo Cita registrado exitosamente.")
                        except Exception as e:
                            print(f"Error al registrar el servicio de tipo Cita: {e}")
                    case "2":
                        if servicio_controller.buscar_servicio("Examen") is not None:
                            print("Ya existe un servicio de tipo Examen.")
                            break
                        valor_servicio = int(input("Valor del servicio (sin puntos ni comas): "))
                        nombre_examen = input("Nombre del examen: ")
                        #fecha = input("Fecha y hora del examen (YYYY-MM-DD HH:MM): ")
                        try:
                            servicio_controller.agregar_servicioExamen("Examen", valor_servicio, nombre_examen)
                            print("Servicio de tipo Examen registrado exitosamente.")
                        except Exception as e:
                            print(f"Error al registrar el servicio de tipo Examen: {e}")
                    case "3":
                        if servicio_controller.buscar_servicio("Medicamento") is not None:
                            print("Ya existe un servicio de tipo Medicamento.")
                            break
                        valor_servicio = int(input("Valor del servicio (sin puntos ni comas): "))
                        nombre_medicamento = input("Nombre del medicamento: ")
                        dosis = input("Dosis: ")
                        presentacion = input("Presentación: ")
                        try:
                            servicio_controller.agregar_servicioMedicamento("Medicamento", valor_servicio, nombre_medicamento, dosis, presentacion)
                            print("Servicio de tipo Medicamento registrado exitosamente.")
                        except Exception as e:
                            print(f"Error al registrar el servicio de tipo Medicamento: {e}")
            case "2":
                # Eliminar servicio
                servicios = servicio_controller.get_servicios()
                if not servicios:
                    print("No hay servicios registrados.")
                    continue

                print("\n--- Servicios registrados ---")
                for i, s in enumerate(servicios):
                    print(f"[{i}] ", end="")
                    s.mostrar_informacion()

                try:
                    numero = int(input("\nIngrese el número del servicio a eliminar: "))
                    servicioSeleccionado = servicios[numero] 
                except ValueError:
                    print("Número inválido.")
                    continue

                try:
                    servicio_controller.eliminar_servicio(servicios[numero].get_tipoServicio())
                    print("Servicio eliminado exitosamente")
                except ValueError:
                    print("No se encontró el servicio")
                
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")
        input("\nPresione una tecla para continuar...")

def elegir_de_lista(elementos, mensaje):
    """Pide un número y devuelve el elemento de la lista, o None si el número es inválido."""
    try:
        numero = int(input(mensaje))
    except ValueError:
        return None
    if numero < 1 or numero > len(elementos):
        return None
    return elementos[numero - 1]


def menu_facturacion(facturacion_controller, persona_controller, servicio_controller):
    while True:
        print("\n--- FACTURACIÓN ---")
        print("1. Registrar factura")
        print("2. Eliminar factura")
        print("3. Buscar factura")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 3: ").strip()

        match opcion:
            case "1":
                # Registrar factura
                codigo = input("Código de la factura: ").strip()
                if not codigo:
                    print("El código de la factura no puede estar vacío.")
                    continue
                if facturacion_controller.buscar_factura(codigo) is not None:
                    print("Ya existe una factura con ese código.")
                    continue

                # Paciente
                pacientes = [p for p in persona_controller.get_personas() if type(p).__name__ == "paciente"]
                if not pacientes:
                    print("No hay pacientes registrados.")
                    continue
                print("\n--- Pacientes disponibles ---")
                for i, p in enumerate(pacientes, start=1):
                    print(f"{i}. {p.get_nombre()} - ID: {p.get_identificacion()}")
                paciente_elegido = elegir_de_lista(pacientes, "Seleccione el número del paciente: ")
                if paciente_elegido is None:
                    print("Selección inválida.")
                    continue

                # Servicio
                servicios = servicio_controller.get_servicios()
                if not servicios:
                    print("No hay servicios registrados. No se puede facturar sin un servicio.")
                    continue
                print("\n--- Servicios disponibles ---")
                for i, s in enumerate(servicios, start=1):
                    print(f"{i}. {s.get_tipoServicio()} - Valor: {s.get_valorServicio()}")
                servicio_elegido = elegir_de_lista(servicios, "Seleccione el número del servicio: ")
                if servicio_elegido is None:
                    print("Selección inválida.")
                    continue

                # Personal de salud
                personal_salud = [p for p in persona_controller.get_personas() if type(p).__name__ == "personalSalud"]
                if not personal_salud:
                    print("No hay personal de salud registrado.")
                    continue
                print("\n--- Personal de salud disponible ---")
                for i, p in enumerate(personal_salud, start=1):
                    print(f"{i}. {p.get_nombre()} - ID: {p.get_identificacion()}")
                salud_elegido = elegir_de_lista(personal_salud, "Seleccione el número del personal de salud: ")
                if salud_elegido is None:
                    print("Selección inválida.")
                    continue

                # Personal administrativo
                personal_admin = [p for p in persona_controller.get_personas() if type(p).__name__ == "administrativo"]
                if not personal_admin:
                    print("No hay personal administrativo registrado.")
                    continue
                print("\n--- Personal administrativo disponible ---")
                for i, p in enumerate(personal_admin, start=1):
                    print(f"{i}. {p.get_nombre()} - ID: {p.get_identificacion()}")
                admin_elegido = elegir_de_lista(personal_admin, "Seleccione el número del personal administrativo: ")
                if admin_elegido is None:
                    print("Selección inválida.")
                    continue

                # Datos de la factura
                fecha = input("Fecha de la factura (YYYY-MM-DD): ").strip()
                total = servicio_elegido.get_valorServicio()  # el total es el valor del servicio
                print(f"Total a facturar: {total}")

                try:
                    facturacion_controller.agregar_factura(codigo, paciente_elegido, servicio_elegido, salud_elegido, admin_elegido, fecha, total)
                    print("Factura registrada exitosamente.")
                except (ServicioObligatorioAlFacturar, CodigoFacturaInvalido) as e:
                    print(f"Error: {e}")
            case "2":
                # Eliminar factura
                facturas = facturacion_controller.get_facturas()
                if not facturas:
                    print("No hay facturas registradas.")
                    continue

                print("\n--- Facturas registradas ---")
                for i, f in enumerate(facturas, start=1):
                    print(f"\nFactura #{i}")
                    f.mostrar_informacion()

                factura_elegida = elegir_de_lista(facturas, "\nIngrese el número de la factura a eliminar: ")
                if factura_elegida is None:
                    print("Número inválido.")
                    continue

                if facturacion_controller.eliminar_factura(factura_elegida.get_codigoFactura()):
                    print("Factura eliminada exitosamente.")
                else:
                    print("No se encontró la factura.")
            case "3":
                # Buscar factura
                codigo = input("Ingrese el código de la factura a buscar: ").strip()
                factura = facturacion_controller.buscar_factura(codigo)
                if factura is None:
                    print("No se encontró una factura con ese código.")
                else:
                    print("\n--- Factura encontrada ---")
                    factura.mostrar_informacion()
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")
        input("\nPresione una tecla para continuar...")

def menu_reportes(persona_controller, servicio_controller, facturacion_controller):
    while True:
        print("\n--- REPORTES ---")
        print("1. Reporte polimórfico de usuarios")
        print("2. Reporte de servicios")
        print("3. Reporte de facturas")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 3: ").strip()

        match opcion:
            case "1":
                # Reporte polimórfico de usuarios
                reporte_personas(persona_controller)
                pass
            case "2":
                # Reporte de servicios
                reporte_servicios(servicio_controller)
            case "3":
                # Reportes de facturas
                reporte_facturas(facturacion_controller)
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")
                
        input("\nPresione una tecla para continuar...")


def probar_fecha_nacimiento_invalida(persona_controller):
    print("\nIntentando registrar un paciente con fecha de nacimiento vacía...")
    try:
        persona_controller.agregar_paciente(
            "Paciente de prueba",
            "900000001",
            "prueba.fecha@email.com",
            "3000000001",
            "Calle de prueba",
            "paciente",
            "",
            "Contacto de prueba",
            "EPS de prueba"
        )
    except FechaNacimientoInvalida as e:
        print(f"Excepción capturada: {e}")


def probar_identificacion_vacia(persona_controller):
    print("\nIntentando registrar un paciente con identificación vacía...")
    try:
        persona_controller.agregar_paciente(
            "Paciente de prueba",
            "",
            "prueba.identificacion@email.com",
            "3000000002",
            "Calle de prueba",
            "paciente",
            "1990-01-01",
            "Contacto de prueba",
            "EPS de prueba"
        )
    except IdentificacionNoPuedeEstarVacia as e:
        print(f"Excepción capturada: {e}")


def probar_servicio_obligatorio(facturacion_controller):
    print("\nIntentando registrar una factura sin servicio...")
    try:
        facturacion_controller.agregar_factura(
            "F-ERROR",
            None,
            None,
            None,
            None,
            "2026-01-01",
            0
        )
    except ServicioObligatorioAlFacturar as e:
        print(f"Excepción capturada: {e}")


def probar_codigo_factura_invalido(facturacion_controller):
    print("\nIntentando registrar una factura con código vacío...")
    try:
        facturacion_controller.agregar_factura(
            "",
            None,
            None,
            None,
            None,
            "2026-01-01",
            0
        )
    except CodigoFacturaInvalido as e:
        print(f"Excepción capturada: {e}")


def menu_casos_excepcionales(persona_controller, facturacion_controller):
    while True:
        print("\n--- CASOS EXCEPCIONALES ---")
        print("1. Fecha de nacimiento inválida")
        print("2. Identificación vacía")
        print("3. Servicio obligatorio al facturar")
        print("4. Código de factura inválido")
        print("0. Volver")
        opcion = input(">>>Ingrese una opción del 1 a 4: ").strip()

        match opcion:
            case "1":
                probar_fecha_nacimiento_invalida(persona_controller)
            case "2":
                probar_identificacion_vacia(persona_controller)
            case "3":
                probar_servicio_obligatorio(facturacion_controller)
            case "4":
                probar_codigo_factura_invalido(facturacion_controller)
            case "0":
                return
            case _:
                print("Opción inválida. Intente de nuevo.")
        input("\nPresione una tecla para continuar...")


def cargar_datos_prueba(persona_controller, servicio_controller, facturacion_controller):
    # precargamos datos de prueba para pacientes
    paciente_juan = persona_controller.agregar_paciente("Juan Torres", "123456789", "juan.torres@email.com", "3001234567", "Calle 123 #45-67", "paciente", "1990-05-15", "Juan Pérez - 3009876543", "EPS Sura")
    paciente_raul = persona_controller.agregar_paciente("Raúl Sanchez", "123456780", "raul.sanchez@email.com", "3001234432", "Calle 123 #45-67", "paciente", "2000-07-11", "Juan Pérez - 3009876543", "EPS Sanitas")

    # precargamos datos de prueba para personal de salud
    salud_carlos = persona_controller.agregar_personalSalud("Dr. Carlos Pérez", "987654321", "carlos.perez@email.com", "3009876543", "Calle 456 #78-90", "salud", "12345", "Hospital General", "Cardiología", "40", "Matutino")
    salud_ana = persona_controller.agregar_personalSalud("Dra. Ana Gómez", "987654322", "ana.gomez@email.com", "3009876544", "Calle 789 #12-34", "salud", "12346", "Hospital General", "Pediatría", "40", "Vespertino")

    # precargamos datos de prueba para personal administrativo
    admin_laura = persona_controller.agregar_adminitrativo("Laura Martínez", "456789123", "laura.martinez@email.com", "3009876545", "Calle 101 #23-45", "administrativo", "Recursos Humanos", "Gerente", "Matutino")
    admin_pedro = persona_controller.agregar_adminitrativo("Pedro Ramírez", "456789124", "pedro.ramirez@email.com", "3009876546", "Calle 102 #24-46", "administrativo", "Contabilidad", "Auxiliar", "Vespertino")

    # precargamos datos de prueba para servicios
    cita_cardio = servicio_controller.agregar_servicioCita("Consulta de cardiología", 120000, "Cardiología")
    cita_pediatria = servicio_controller.agregar_servicioCita("Consulta de pediatría", 90000, "Pediatría")
    examen_hemograma = servicio_controller.agregar_servicioExamen("Hemograma completo", 45000, "Hemograma")
    medicamento_ibuprofeno = servicio_controller.agregar_servicioMedicamento("Ibuprofeno 400mg", 8000, "Ibuprofeno", 400, "Tableta")

    # precargamos datos de prueba para facturas
    facturacion_controller.agregar_factura("F001", paciente_juan, cita_cardio, salud_carlos, admin_laura, "2026-11-05", cita_cardio.get_valorServicio())
    facturacion_controller.agregar_factura("F002", paciente_raul, examen_hemograma, salud_ana, admin_pedro, "2026-11-06", examen_hemograma.get_valorServicio())
    facturacion_controller.agregar_factura("F003", paciente_juan, medicamento_ibuprofeno, salud_carlos, admin_laura, "2026-11-07", medicamento_ibuprofeno.get_valorServicio())


def main():
    facturacion_controller = facturacionController()
    servicio_controller = servicioController()
    persona_controller = personaController()

    cargar_datos_prueba(persona_controller, servicio_controller, facturacion_controller)

    while True:
        mostrar_menu_principal()
        opcion = input(">>>Ingrese una opción del 1 a 5: ").strip()

        match opcion:
            case "1":
                menu_usuarios(persona_controller)
            case "2":
                menu_servicios(servicio_controller)
            case "3":
                menu_facturacion(facturacion_controller, persona_controller, servicio_controller)
            case "4":
                menu_reportes(persona_controller, servicio_controller, facturacion_controller)
            case "5":
                menu_casos_excepcionales(persona_controller, facturacion_controller)
            case "0":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida. Intente de nuevo.")
    
# Reportes generales            
def reporte_personas(persona_controller):
    personas = persona_controller.get_personas()
    if not personas:
        print("No hay usuarios registrados.")
        return

    print("\n--- REPORTE POLIMÓRFICO DE USUARIOS ---")
    for p in personas:
        p.mostrar_informacion()
        print("----------------------------------------")

def reporte_servicios(servicio_controller):
    servicios = servicio_controller.get_servicios()
    if not servicios:
        print("No hay servicios registrados.")
        return

    print("\n--- REPORTE DE SERVICIOS ---")
    for s in servicios:
        s.mostrar_informacion()
        print("----------------------------------------")

def reporte_facturas(facturacion_controller):
    facturas = facturacion_controller.get_facturas()
    if not facturas:
        print("No hay facturas registradas.")
        return

    print("\n--- REPORTE DE FACTURAS ---")
    for f in facturas:
        f.mostrar_informacion()
        print("----------------------------------------")

if __name__ == "__main__":
    main()
    