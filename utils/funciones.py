def separador(texto: str = None, largo: int = 30) -> str:
    largo = largo
    linea = '='

    if texto is not None:
        texto_f = texto.center(len(texto)+2)
        return f'{texto_f :{linea}^{largo}}'
    return linea*largo


def validador_option(valor: str) -> int:
    while not valor.isnumeric():
        valor = input('Reingrese la opción, debe ser un numero: ')
    else:
        valor = int(valor)
        while valor < 1 or valor > 5:
            valor = input('Reingrese una opción dentro del rango: ')
            while not valor.isnumeric():
                valor = input('Reingrese la opción, debe ser un numero: ')
            else:
                valor = int(valor)
    return int(valor)


def pedidoDeDatos() -> tuple:
    nombre = input('Ingrese Nombre: ')
    while nombre == '':
        nombre = input('El nombre no puede ser nulo. Reingrese Nombre: ')

    apellido = input('Ingrese Apellido: ')
    while apellido == '':
        apellido = input('El nombre no puede ser nulo. Reingrese Apellido: ')

    direccion = input('Ingrese Dirección: ')
    if direccion == '':
        direccion = None

    telefono = input('Ingrese Teléfono: ')
    while True:
        if telefono == '':
            telefono = None
            break
        elif not telefono.isnumeric():
            telefono = input('Reingrese el telefono: ')
        else:
            break

    cliente = (nombre, apellido, direccion, telefono)

    return cliente
