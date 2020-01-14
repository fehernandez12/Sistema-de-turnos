import sys

fila_depositos = []
fila_aperturas = []

def _menu():
    print('Bienvenido a BanPlatzi')
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

    if nombre_cliente not in fila_depositos and nombre_cliente not in fila_aperturas:
        if tipo_turno == 1:
            fila_depositos.append(nombre_cliente)
            print('El cliente {} tiene el turno número '.format(nombre_cliente) + 'D' + str(fila_depositos.index(nombre_cliente) + 1))
        elif tipo_turno == 2:
            fila_aperturas.append(nombre_cliente)
            print('El cliente {} tiene el turno número '.format(nombre_cliente) + 'A' + str(fila_aperturas.index(nombre_cliente) + 1))
    else:
        _ya_tiene_turno(nombre_cliente)

def atender_cliente():
    global fila_aperturas
    global fila_depositos

    if len(fila_aperturas) != 0:
        indice_turno = fila_aperturas.index(fila_aperturas[0])
        print('Atendiendo al turno A' + str(indice_turno + 1))
        print(fila_aperturas[-1])
        fila_aperturas.pop(0)
    else:
        indice_turno = fila_depositos.index(fila_depositos[0])
        print('Atendiendo al turno D' + str(indice_turno + 1))
        print(fila_depositos[0])
        fila_depositos.pop(0)

def listar_clientes():
    global fila_aperturas
    global fila_depositos

    print('Clientes para depósitos:')
    for cliente in fila_depositos:
        print(cliente)

    print('Clientes para aperturas:')
    for cliente in fila_aperturas:
        print(cliente)

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