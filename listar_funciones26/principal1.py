import funciones1 as fn


estudiantes = []

while True:
    print("1) Agregar estudiante")
    print("2) Mostrar todos los estudiantes")
    print("3) Buscar estudiante por nombre")
    print("4) Exportar Regitro a Archivo de texto")
    print("5) Salir")
    
    opcion = int(input("ingrese opcion: "))

    if opcion == 1:
        fn.agregar_estudiantes(estudiantes)

    elif opcion == 2:
        fn.mostrar_todos_los_estudiantes(estudiantes)
        
    elif opcion == 3:
        fn.buscar_estudiante_por_nombre(estudiantes)

    elif opcion == 4:
        fn.exportar_registro_a_archivo_texto(estudiantes)

    elif opcion == 5:
        print("saliendo...")
        break