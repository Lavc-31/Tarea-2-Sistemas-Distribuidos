import time
import json
import random
from datetime import datetime
from kafka import KafkaProducer

def serializer(message):
	return json.dumps(message).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10, 1), value_serializer = serializer)

flag = True
print("Bienvenido al menu de los Maestros Sopaipilleros!\n")
while flag:
    print("Que desea hacer?(ingrese el numero):\n")
    print("1.- Registrar Nuevo miembro\n")
    print("2.- Registrar Venta\n")
    print("3.- Reportar Agente extraño\n")
    print("4.- Salir del menu\n")

    opcion = int(input())
    print("-----------\n")
    if(opcion == 1):
        print("Ingrese los datos del nuevo miembro:\n")

        print("Ingrese el Nombre:\n")
        nombre = input()

        print("Ingrese el Apellido:\n")
        apellido = input()

        print("Ingrese el Rut:\n")
        rut = input()

        print("Ingrese el Email:\n")
        email = input()

        print("Patente del Carrito:\n")
        patente = input()

        print("Registro Premium (1 si es Premium o 0 si no lo es):\n")
        premium = int(input())

        miembro = {"nombre": nombre, "apellido":apellido, "rut":rut, "email":email, "patente":patente, "premium":premium}

        if(premium == 1):
            producer.send('nuevosMiembros', miembro, partition=0)
        else:
            producer.send('nuevosMiembros', miembro, partition=1)

    elif(opcion == 2):
        print("Ingrese los datos de la venta:\n")

        print("Ingrese el Cliente:\n")
        cliente = input()

        print("Ingrese la Cantidad de sopaipillas:\n")
        cantidad = int(input())

        print("Ingrese la Hora:\n")
        hora = input()

        print("Ingrese el Stock:\n")
        stock_s = int(input())

        print("Ingrese la Ubicacion del carrito:\n")
        ubicacion = input()

        venta = {"cliente" : cliente, "cantidad" : cantidad, "hora" : hora, "stock_s" :stock_s, "ubicacion" :ubicacion}
        producer.send('ventas', venta)

    elif(opcion == 3):
        print("Ingrese la ubicacion del carrito profugo:\n")
        profugo = input()

        profugo_dict = {"profugo" : profugo}
        producer.send('coordenadas', profugo)

    elif(opcion == 4):
        flag = False
    else:
        print("Ingreso de opcion invalido, vuelva a ingresar la opcion\n")
