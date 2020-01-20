import sys

fila_depositos = {}
fila_aperturas = {}

def _menu():
    print('\n\n\nBienvenido a BanPlatzi')
    print('Selecciona una opción:')
    print('[1] Agregar cliente a la fila de depósitos')
    print('[2] Agregar cliente a la fila de aperturas')
    print('[3] Atender cliente')
    print('[4] Listar clientes en las filas')
    print('[5] Salir')

def _get_nombre_cliente():
    client_name = None

    while not client_name:
        client_name = input('¿Cuál es el nombre del cliente? ')

        if client_name == 'salir':
            client_name = None
            break

    if not client_name:
            sys.exit()

    return client_name

def _ya_tiene_turno(nombre_cliente):
    print('El cliente {} ya tiene un turno asignado.'.format(nombre_cliente))
    print('Por favor espera a que sea atendido.')

def agregar_cliente(tipo_turno, nombre_cliente):
    global fila_depositos
    global fila_aperturas
    n = False
    if len(fila_aperturas) > 0 and len(fila_depositos) > 0:  
        for val1 in fila_depositos.values():
            if val1 == nombre_cliente:
                n = True
            else:
                n = False
        for val2 in fila_aperturas.values():
            if val2 == nombre_cliente:
                n = True
            else:
                n = False

    if n == False:
        if tipo_turno == 1:
            l1 = len(fila_depositos) + 1
            t1 = 'D' + str(l1)
            fila_depositos[t1] = nombre_cliente
            print(('El cliente {} tiene el turno número ' + t1).format(nombre_cliente))
        elif tipo_turno == 2:
            l2 = len(fila_aperturas) + 1
            t2 = 'A' + str(l2)
            fila_aperturas[t2] = nombre_cliente
            print(('El cliente {} tiene el turno número ' + t2).format(nombre_cliente))
    else:
        _ya_tiene_turno(nombre_cliente)

def atender_cliente():
    global fila_aperturas
    global fila_depositos
    if len(fila_aperturas) == 0 and len(fila_depositos) == 0:
        print('No hay clientes para atender')
    elif len(fila_aperturas) != 0:
        first = next(iter(fila_aperturas))
        print('Atendiendo al turno ' + first)
        fila_aperturas.pop(first)
    else:
        first = next(iter(fila_depositos))
        print('Atendiendo al turno ' + first)
        fila_depositos.pop(first)

def listar_clientes():
    global fila_aperturas
    global fila_depositos

    print('Clientes para depósitos:')
    for key, value in fila_depositos.items():
        print(("Turno: {}  | Nombre: {}").format(key, value))

    print('Clientes para aperturas:')
    for key, value in fila_aperturas.items():
        print(("Turno: {}  | Nombre: {}").format(key, value))


if __name__ == '__main__':
    salir = False
    while not salir:
        _menu()
        command = int(input())

        if command == 1:
            nombre_cliente = _get_nombre_cliente()
            agregar_cliente(1, nombre_cliente)
        elif command == 2:
            nombre_cliente = _get_nombre_cliente()
            agregar_cliente(2, nombre_cliente)
        elif command == 3:
            atender_cliente()
        elif command == 4:
            listar_clientes()
        elif command == 5:
            salir = True
        else:
            print('Comando inválido')
