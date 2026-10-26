from models.facturacion import facturacion

class facturacionController():

    def __init__(self):
        self.facturas = []

    def agregar_factura(self, codigoFactura, codigoPaciente, codigoServicio, codigoPersonalSalud, codigoAdministrativo, fechaFactura, total):
        factura = facturacion(codigoFactura, codigoPaciente, codigoServicio, codigoPersonalSalud, codigoAdministrativo, fechaFactura, total)
        self.facturas.append(factura)

    def get_facturas(self):
        return self.facturas.copy()