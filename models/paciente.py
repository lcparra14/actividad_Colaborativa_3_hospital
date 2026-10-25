from models.persona import persona

class paciente (persona):

    def __init__(self, nombre, identificacion, correo, telefono, direccion, codigoPaciente, fechaNacimiento, contactoEmergencia, nombreEps, nivelDeAcceso):
        super().__init__(nombre, identificacion, correo, telefono, direccion)
        self.setCodigoPaciente(codigoPaciente)
        self.setFechaNacimiento(fechaNacimiento)
        self.setContactoEmergencia(contactoEmergencia)
        self.setNombreEps(nombreEps)
        self.setNivelDeAcceso(nivelDeAcceso)

    def mostrar_informacion(self):
        print(f"---INFORMACION PACIENTE---")
        super().mostrar_informacion()
        print(f"Codigo del paciente: {self.getCodigoPaciente()}")
        print(f"Fecha de nacimiento: {self.getFechaNacimiento()}")
        print(f"Contacto de emergencia: {self.getContactoEmergencia()}")
        print(f"Eps a la que pertenece: {self.getNombreEps()}")
        print(f"Nivel de acceso permitido: {self.getNivelDeAcceso()}")

    def realizar_actividad_principal(self):
        print(f"El paciente {self.get_nombre()} se encuentra afiliado a {self.getNombreEps()} y tiene un nivel de acceso {self.getNivelDeAcceso()}.")

    # SETTERS
    def setCodigoPaciente(self, codigoPaciente):
        # validaciones
        self._codigoPaciente = codigoPaciente

    def setFechaNacimiento(self, fechaNacimiento):
        self._fechaNacimiento = fechaNacimiento 

    def setContactoEmergencia(self, contactoEmergencia):
        self._contactoEmergencia = contactoEmergencia

    def setNombreEps(self, nombreEps):
        self._nombreEps = nombreEps

    def setNivelDeAcceso(self, nivelDeAcceso):
        self._nivelDeAcceso = nivelDeAcceso

    # GETTERS
    def getCodigoPaciente(self):
        return self._codigoPaciente

    def getFechaNacimiento(self):
        return self._fechaNacimiento

    def getContactoEmergencia(self):
        return self._contactoEmergencia

    def getNombreEps(self):
        return self._nombreEps
    
    def getNivelDeAcceso(self):
        return self._nivelDeAcceso
