class persona:
    def __init__(self, nombre, identificacion, correo, telefono, direccion):
        self.set_nombre(nombre)
        self.set_identificacion(identificacion)
        self.set_correo(correo)
        self.set_telefono(telefono)
        self.set_direccion(direccion)

    def mostrar_informacion(self):
        print(f"Nombre de la persona: {self.get_nombre()}")
        print(f"Identificacion: {self.get_identificacion()}")
        print(f"Correo Electronico: {self.get_correo()}")
        print(f"Numero Telefonico: {self.get_telefono()}")
        print(f"Direccion de residencia: {self.get_direccion()}")

    # Getters and Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_identificacion(self, identificacion):
        self._identificacion = identificacion

    def get_identificacion(self):
        return self._identificacion 

    def set_correo(self, correo):
        self._correo = correo

    def get_correo(self):
        return self._correo

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_telefono(self):
        return self._telefono

    def set_direccion(self, direccion):
        self._direccion = direccion

    def get_direccion(self):
        return self._direccion 
    