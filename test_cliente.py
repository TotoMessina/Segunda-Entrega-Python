from modelado_clientes.cliente import Cliente

cliente1 = Cliente(nombre="Juan Perez", email="juan.perez@example.com", telefono="1234567890", direccion="123 Calle Falsa")
print(cliente1)

cliente1.actualizar_email("nuevo.email@example.com")
print(cliente1)