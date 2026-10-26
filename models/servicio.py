#Clase: Servicio
class servicio:
    def __init__(self, codigoServicio, nombreServicio):
        self.set_codigoServicio(codigoServicio)
        self.set_nombreServicio(nombreServicio)

    def mostrar_informacion(self):
        print(f"Código del servicio: {self.get_codigoServicio()}")
        print(f"Nombre del servicio: {self.get_nombreServicio()}")

    # Getters and Setters
    def set_codigoServicio(self, codigoServicio):
        self._codigoServicio = codigoServicio

    def get_codigoServicio(self):
        return self._codigoServicio

    def set_nombreServicio(self, nombreServicio):
        self._nombreServicio = nombreServicio

    def get_nombreServicio(self):
        return self._nombreServicio 