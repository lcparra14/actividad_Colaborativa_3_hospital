#Clase: Facturacion
class facturacion:
    def __init__(self, codigoFactura, codigoPaciente, codigoServicio, codigoPersonalSalud, codigoAdministrativo, fechaFactura, total):
        self.set_codigoFactura(codigoFactura)
        self.set_codigoPaciente(codigoPaciente)
        self.set_codigoServicio(codigoServicio)
        self.set_codigoPersonalSalud(codigoPersonalSalud)
        self.set_codigoAdministrativo(codigoAdministrativo)
        self.set_fechaFactura(fechaFactura)
        self.set_total(total)

    def mostrar_informacion(self):
        print(f"Codigo de la factura: {self.get_codigoFactura()}")
        print(f"Codigo del paciente: {self.get_codigoPaciente()}")
        print(f"Codigo del servicio: {self.get_codigoServicio()}")
        print(f"Codigo del personal de salud: {self.get_codigoPersonalSalud()}")
        print(f"Codigo del administrativo: {self.get_codigoAdministrativo()}")
        print(f"Fecha de la factura: {self.get_fechaFactura()}")
        print(f"Total: {self.get_total()}")

    # Getters and Setters
    def set_codigoFactura(self, codigoFactura):
        self._codigoFactura = codigoFactura

    def get_codigoFactura(self):
        return self._codigoFactura

    def set_codigoPaciente(self, codigoPaciente):
        self._codigoPaciente = codigoPaciente

    def get_codigoPaciente(self):
        return self._codigoPaciente

    def set_codigoServicio(self, codigoServicio):
        self._codigoServicio = codigoServicio

    def get_codigoServicio(self):
        return self._codigoServicio

    def set_codigoPersonalSalud(self, codigoPersonalSalud):
        self._codigoPersonalSalud = codigoPersonalSalud

    def get_codigoPersonalSalud(self):
        return self._codigoPersonalSalud

    def set_codigoAdministrativo(self, codigoAdministrativo):
        self._codigoAdministrativo = codigoAdministrativo

    def get_codigoAdministrativo(self):
        return self._codigoAdministrativo

    def set_fechaFactura(self, fechaFactura):
        self._fechaFactura = fechaFactura

    def get_fechaFactura(self):
        return self._fechaFactura

    def set_total(self, total):
        self._total = total

    def get_total(self):
        return self._total