estudiantes = []



def agregar_estudiantes(estudiantes):
    nombre = input("ingrese nombre y apellido: ").lower()
    edad = int(input("ingrese edad del estudiante: "))
    rut = int(input("ingrese rut del estudiante: "))
    estudiantes.append({
        "nombre/apellido" : nombre,
        "edad" : edad,
        "rut" : rut
    })
    
    
    
def mostrar_todos_los_estudiantes(estudiantes):
    for estudiante in estudiantes:
        print(estudiante)
def buscar_estudiante_por_nombre(estudiantes):
    nombre = input("ingrese nombre y apellido del estudiante: ").lower()
    nombre_estudiante = estudiantes
    for estudiante in estudiantes:
        if estudiante["nombre/apellido"] and estudiante["edad"] and estudiante["rut"] == nombre_estudiante:
            nombre_estudiante.append(estudiante)
        print(nombre_estudiante)
            
            

def exportar_registro_a_archivo_texto(estudiantes):
    imprimir_estudiantes = estudiantes
    
    nombreArchivo = "registro_estudiantes.txt"
    with open(nombreArchivo, "w") as archivo:
        nombreArchivo = f"registro_estudiantes{estudiantes}.txt"
    
        for estudiante in imprimir_estudiantes:
            archivo.write(f"nombre:{estudiante["nombre/apellido"]}\n")
            archivo.write(f"edad:{estudiante["edad"]}\n")
            archivo.write(f"RUT:{estudiante["rut"]}\n")