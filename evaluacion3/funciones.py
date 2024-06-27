stock_libros = 5
registro_libros = []
titulos = ["alicia","pinocho","caperucita"]
genero = ["ficcion","cuento","ciencia"]
autores = ["pepe","pedro","jorge"]
def registrar_libros(regitro_libros):
    titulo = input("ingrese un libro(alicia/pinocho/caperucita):").lower()
    
    print("pepe/pedro,jorge")
    autor = input("ingrese el autor del libro: ").lower()
    
    print("ficcion/cuento/ciencia")
    genero = input("ingrese el genero del libro: ").lower()

    print("precios: alicia:1200/ pinocho:3000/caperucita:2000/")
    precio = int(input("ingrese precio del libro: "))
       
    registro_libros.append({
        "titulo" : titulo,
        "autor" : autor,
        "genero" : genero,
        "precio" : precio
    })
    print(registro_libros)

def listar_todos_los_libros(registro_libros):
    print("CATALOGO DE LIBROS")
    print("########################")
    for listar in titulos:
        print(listar)
    print("#########################")
        # if listado_libros["titulo"] and listado_libros["autor"] and listado_libros ["genero"] and listado_libros ["precio"] == listado_libros:   
        #     print(listado_libros)
def registrar_venta(registro_libros):
    print("catalogos disponibles: ",stock_libros)
    print("nuestros titulos: ",titulos)
def imprimir_reporte_de_ventas(registro_libros):
    print()

def generar_txt(regitro_libros):
    generar_2 = registro_libros
    archivoTexto = "archivo.txt"
    
    with open(archivoTexto, "w") as archivo:
        archivoTexto = f"archivo{registro_libros}.txt"
        for generar in  generar_2:
            archivo.write(f"titulo{generar["titulo"]}")
            archivo.write(f"autor{generar["autor"]}")
            archivo.write(f"genero{generar["genero"]}")
            archivo.write(f"titulo{generar["precio"]}")
