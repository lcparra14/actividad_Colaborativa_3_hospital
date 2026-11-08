from models.paciente import paciente
from models.servicio import servicio
from models.personalSalud import personalSalud
from models.administrativo import administrativo
from models.excepciones import ServicioObligatorioAlFacturar, CodigoFacturaInvalido

#Clase: Facturacion
class facturacion:
    def __init__(self, codigoFactura, paciente, servicio, personalSalud, administrativo, fechaFactura, total):
        self.set_codigoFactura(codigoFactura)
        self.set_paciente(paciente)
        self.set_servicio(servicio)
        self.set_personalSalud(personalSalud)
        self.set_administrativo(administrativo)
        self.set_fechaFactura(fechaFactura)
        self.set_total(total)

    def mostrar_informacion(self):
        print(f"Codigo de la factura: {self.get_codigoFactura()}")
        print(f"Paciente: {self.get_paciente().get_nombre()}")
        print(f"Servicio: {self.get_servicio().get_tipoServicio()}")
        print(f"Personal de salud: {self.get_personalSalud().get_nombre()}")
        print(f"Administrativo: {self.get_administrativo().get_nombre()}")
        print(f"Fecha de la factura: {self.get_fechaFactura()}")
        print(f"Total: {self.get_total()}")

    # Getters and Setters
    def set_codigoFactura(self, codigoFactura):
        if codigoFactura.strip() == "":
            raise CodigoFacturaInvalido(codigoFactura)
        self._codigoFactura = codigoFactura

    def get_codigoFactura(self):
        return self._codigoFactura

    def set_paciente(self, paciente):
        self._paciente = paciente

    def get_paciente(self):
        return self._paciente

    def set_servicio(self, servicio):
        if servicio is None:
            raise ServicioObligatorioAlFacturar(servicio)
        self._servicio = servicio

    def get_servicio(self):
        return self._servicio

    def set_personalSalud(self, personalSalud):
        self._personalSalud = personalSalud

    def get_personalSalud(self):
        return self._personalSalud

    def set_administrativo(self, administrativo):
        self._administrativo = administrativo

    def get_administrativo(self):
        return self._administrativo

    def set_fechaFactura(self, fechaFactura):
        self._fechaFactura = fechaFactura

    def get_fechaFactura(self):
        return self._fechaFactura

    def set_total(self, total):
        self._total = total

    def get_total(self):
        return self._total