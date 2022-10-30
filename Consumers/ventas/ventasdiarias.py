
def calculo_ventas():
    f = open('ventas.txt', 'r')

    ubicaciones = {}
    clientes_ubicacion{}

    for line in f:
        linea = line.split(",")
        cliente = linea[0]
        cantidad = linea[1]
        ubicacion = linea[2]
        if(ubicacion not in ubicaciones):
            ubicaciones[ubicacion] = 0

        if(ubicacion not in clientes_ubicacion):
            clientes_ubicacion[ubicacion]=[]

        if(cliente not in clientes_ubicacion[ubicacion]):
            clientes_ubicacion[ubicacion].append(cliente)
        ubicaciones[ubicacion] += int(cantidad)

    for i in ubicaciones:
        c = len(clientes_ubicacion[i].values())
        print(i+" | Ventas Totales: "+i.values()+" | Clientes Totales: "+c+" | Promedio ventas: "+(i.values()/c)+"\n")
    f.close()