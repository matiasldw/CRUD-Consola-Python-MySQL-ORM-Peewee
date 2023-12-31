from utils import funciones, valid_Crud


def menu() -> int:
    print(funciones.separador('Menu'))
    print("1.- Listar Clientes")
    print("2.- Registrar Cliente")
    print("3.- Actualizar Cliente")
    print("4.- Eliminar Cliente")
    print("5.- Salir")
    print(funciones.separador())

    option = input('Seleccione una opción: ')

    return funciones.validador_option(option)


def action(valor: int):
    print()
    if valor == 1:
        try:
            if not valid_Crud.clientesList():
                print('No existe ningun cliente.')
        except Exception as ex:
            print(f'Ocurrió un error... ({ex})')

    elif valor == 2:
        try:
            if id_cliente := valid_Crud.crearCliente():
                print(f'\n{funciones.separador(f"Cliente Agregado. Id: {id_cliente}")}\n')
        except Exception as ex:
            print(f'Ocurrió un error... ({ex})')

    elif valor == 3:
        try:
            if not valid_Crud.clientesList():
                print('No existe ningun cliente.')
            else:
                if cliente := valid_Crud.actualizarCliente():
                    print(f'\n{funciones.separador(f"Cliente {cliente.id} Actualizado")}\n')
                else:
                    print(f'\n{funciones.separador("El id No existe.")}\n')
        except Exception as ex:
            print(f'Ocurrió un error... ({ex})')

    elif valor == 4:
        try:
            if not valid_Crud.clientesList():
                print('No existe ningun cliente.')
            else:
                if cliente := valid_Crud.borrarCliente():
                    print(f'\n{funciones.separador(f"Cliente {cliente.id} Borrado")}\n')
                else:
                    print(f'\n{funciones.separador("El id No existe.")}\n')
        except Exception as ex:
            print(f'Ocurrió un error... ({ex})')


if __name__ == '__main__':
    while True:
        election = menu()
        if election == 5:
            break
        action(election)
        # print()
