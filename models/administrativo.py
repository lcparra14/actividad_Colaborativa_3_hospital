from models.persona import persona

class administrativo (persona):

    def __init__(self, nombre, identificacion, correo, telefono, direccion, codigoAdministrativo, area, cargo, turno, nivelDeAcceso):
        super().__init__(nombre, identificacion, correo, telefono, direccion)
        self.setCodigoAdministrativo(codigoAdministrativo)
        self.setArea(area)
        self.setCargo(cargo)
        self.setTurno(turno)
        self.setNivelDeAcceso(nivelDeAcceso)

    def mostrar_informacion(self):
        print(f"---INFORMACION DEL COLABORADOR ADMINISTRATIVO---")
        super().mostrar_informacion()
        print(f"Codigo del administrativo: {self.getCodigoAdministrativo()}")
        print(f"Area: {self.getArea()}")
        print(f"Cargo: {self.getCargo()}")
        print(f"Turno: {self.getTurno()}")
        print(f"Nivel de acceso permitido: {self.getNivelDeAcceso()}")

    def realizar_actividad_principal(self):
        print(f"El colaborador administrativo {self.get_nombre()} se encuentra trabajando en el area de {self.getArea()} y tiene el cargo de {self.getCargo()}.")

    # SETTERS
    def setCodigoAdministrativo(self, codigoAdministrativo):
        # validaciones
        self._codigoAdministrativo = codigoAdministrativo

    def setArea(self, area):
        self._area = area 

    def setCargo(self, cargo):
        self._cargo = cargo

    def setTurno(self, turno):
        self._turno = turno

    def setNivelDeAcceso(self, nivelDeAcceso):
        self._nivelDeAcceso = nivelDeAcceso

    # GETTERS
    def getCodigoAdministrativo(self):
        return self._codigoAdministrativo

    def getArea(self):
        return self._area
    
    def getCargo(self):
        return self._cargo

    def getTurno(self):
        return self._turno
    
    def getNivelDeAcceso(self):
        return self._nivelDeAcceso
