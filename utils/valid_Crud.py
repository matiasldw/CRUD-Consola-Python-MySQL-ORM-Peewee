from Models.Clientes import Clientes
from utils.funciones import separador, pedidoDeDatos


def clientesList() -> bool:
    result = Clientes.select()

    if result:
        print(separador('Clientes', 73))
        print(f'Id\t{"Nombre".ljust(15)}{"Apellido".ljust(15)}{"Dirección".ljust(30)}Teléfono')
        print('-' * 73)

        for client in result:
            if client.direccion is None:
                client.direccion = ''
            if client.telefono is None:
                client.telefono = ''
            print(f'{client.id}\t'
                  f'{client.nombre.ljust(15)}'
                  f'{client.apellido.ljust(15)}'
                  f'{client.direccion.ljust(30)}'
                  f'{client.telefono}')
        print()
        return True
    else:
        return False


def crearCliente() -> None:
    new_Cliente = pedidoDeDatos()

    id_Cliente = Clientes.insert({
        Clientes.nombre: new_Cliente[0],
        Clientes.apellido: new_Cliente[1],
        Clientes.direccion: new_Cliente[2],
        Clientes.telefono: new_Cliente[3]
    }).execute()

    return id_Cliente


def actualizarCliente():
    id_Cliente = input('Elija Id del cliente a Actualizar: ')
    while not id_Cliente.isnumeric():
        id_Cliente = input('Reingrese Id del cliente a Actualizar: ')
    else:
        print()
        data_Client = pedidoDeDatos()

        cliente_Actualizar = Clientes.get_or_none(Clientes.id == id_Cliente)

        Clientes.update({Clientes.nombre: data_Client[0],
                         Clientes.apellido: data_Client[1],
                         Clientes.direccion: data_Client[2],
                         Clientes.telefono: data_Client[3]}).where(
                    Clientes.id == cliente_Actualizar.id).execute()

        return Clientes.get_or_none(Clientes.id == cliente_Actualizar.id)


def borrarCliente():
    id_Cliente = input('Elija Id del cliente a Borrar: ')
    while not id_Cliente.isnumeric():
        id_Cliente = input('Reingrese Id del cliente a Borrar: ')
    else:
        cliente_Borrado = Clientes.get_or_none(Clientes.id == id_Cliente)

        Clientes.delete_by_id(cliente_Borrado.id)

        return cliente_Borrado
