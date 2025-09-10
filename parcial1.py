import csv
import os

archivo_clientes = 'clientes.csv'
archivo_pedidos = 'pedidos.csv'
archivo_ventas = 'ventas.csv'

def inicializar_archivos():
    if not os.path.exists(archivo_clientes):
        with open(archivo_clientes, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id_cliente','nombre','apellido','telefono','activo'])
            writer.writerow(['1','juan','perez','3123456789','1'])
            writer.writerow(['2','maria','gomez','3112233445','1'])
            writer.writerow(['3','carlos','ramirez','3205566778','0'])
    if not os.path.exists(archivo_pedidos):
        with open(archivo_pedidos, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id_pedido','id_cliente','producto','precio','cantidad','activo'])
            writer.writerow(['1','1','laptop','2500.00','1','1'])
            writer.writerow(['2','2','mouse','20.50','2','1'])
            writer.writerow(['3','1','teclado','45.00','1','1'])
            writer.writerow(['4','3','monitor','150.00','1','0'])
    if not os.path.exists(archivo_ventas):
        with open(archivo_ventas, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id_pedido','id_cliente','cantidad','activo'])
            writer.writerow(['1','1','1','1'])
            writer.writerow(['2','2','2','1'])
            writer.writerow(['3','1','1','1'])
            writer.writerow(['4','3','1','0'])

def registrar_cliente():
    with open(archivo_clientes, 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file))
    id_cliente = len(reader)
    nombre = input('nombre: ')
    apellido = input('apellido: ')
    telefono = input('telefono: ')
    with open(archivo_clientes, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_cliente,nombre,apellido,telefono,1])

def listar_clientes():
    with open(archivo_clientes, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if line[4] == '1':
                print(line)

def eliminar_cliente():
    id_cliente = input('id cliente a eliminar: ')
    filas = []
    with open(archivo_clientes, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == id_cliente:
                line[4] = '0'
            filas.append(line)
    with open(archivo_clientes, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filas)

def registrar_pedido():
    with open(archivo_pedidos, 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file))
    id_pedido = len(reader)
    id_cliente = input('id cliente: ')
    producto = input('producto: ')
    precio = input('precio: ')
    cantidad = input('cantidad: ')
    with open(archivo_pedidos, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_pedido,id_cliente,producto,precio,cantidad,1])

def listar_pedidos_cliente():
    id_cliente = input('id cliente: ')
    with open(archivo_pedidos, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if line[1] == id_cliente and line[5] == '1':
                print(line)

def guardar_venta():
    with open(archivo_ventas, 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file))
    id_pedido = len(reader)
    id_cliente = input('id cliente: ')
    cantidad = input('cantidad: ')
    with open(archivo_ventas, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_pedido,id_cliente,cantidad,1])

def listar_ventas():
    with open(archivo_ventas, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if line[3] == '1':
                print(line)

def listar_ventas_cliente():
    nombre_cliente = input('nombre cliente: ')
    total = 0
    with open(archivo_clientes, 'r', encoding='utf-8') as file:
        clientes = list(csv.reader(file))
    id_cliente = None
    for line in clientes:
        if line[1] == nombre_cliente and line[4] == '1':
            id_cliente = line[0]
            break
    if id_cliente:
        with open(archivo_pedidos, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                if line[1] == id_cliente and line[5] == '1':
                    parcial = float(line[3]) * int(line[4])
                    print(line[2], line[3], line[4], parcial)
                    total += parcial
        print('total:', total)
    else:
        print('cliente no encontrado')

def menu():
    inicializar_archivos()
    while True:
        print('1. registrar cliente')
        print('2. listar clientes')
        print('3. eliminar cliente')
        print('4. registrar pedido')
        print('5. listar pedidos cliente')
        print('6. guardar venta')
        print('7. listar ventas cliente')
        print('8. listar ventas')
        print('9. salir')
        opcion = input('opcion: ')
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            listar_clientes()
        elif opcion == '3':
            eliminar_cliente()
        elif opcion == '4':
            registrar_pedido()
        elif opcion == '5':
            listar_pedidos_cliente()
        elif opcion == '6':
            guardar_venta()
        elif opcion == '7':
            listar_ventas_cliente()
        elif opcion == '8':
            listar_ventas()
        elif opcion == '9':
            break
        else:
            print('opcion invalida')

menu()