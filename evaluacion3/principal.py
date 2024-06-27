#ejeuta aqui profe y en el otro documento estan las funciones
import funciones as fn
registro_libros = []

while True:
    try:
        print("BIENVENIDO A LA LIBRERIA")
        print("1.regitrar libros")
        print("2.listar todos los libros")
        print("3.regitrar venta")
        print("4.imprimir reporte de ventas")
        print("5.generar txt")
        print("6.salir de programa")

        opcion = int(input("seleccione opcion: "))

        if opcion == 1:
            fn.registrar_libros(registro_libros)

        elif opcion == 2:
            fn.listar_todos_los_libros(registro_libros)

        elif opcion == 3:
            fn.registrar_venta(registro_libros)

        elif opcion == 4:
            fn.imprimir_reporte_de_ventas(registro_libros)

        elif opcion == 5:
            fn.generar_txt(registro_libros)
        
        elif opcion == 6:
            print("saliendo....")
            break
    except:
        print("ingrese una opcion valida")