#Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
#criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
#siguiente situación:
#a. cargue tres documentos de empleados (cada documento se representa solamente con
#un nombre).
#b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#c. cargue dos documentos del staff de TI.
#d. cargue un documento del gerente.
#e. imprima los dos primeros documentos de la cola.
#f. cargue dos documentos de empleados y uno de gerente.
#g. imprima todos los documentos de la cola de impresión.##

import queue

cola_prioridad = queue.PriorityQueue()

condicion = "s"
while condicion == "s":
    categoria = input("Ingrese a qué categoría pertenece el documento (empleado/TI/gerente): ")
    if categoria == "empleado":
        indice = 1
    elif categoria == "TI":
        indice = 2
    elif categoria == "gerente":
            indice = 3
    else:
        print("Ha ingresado incorrectamente el nombre de la categoría.")
            

    documento = input("Ingrese el nombre del documento: ")
    cola_prioridad.put((indice, documento))
    condicion = input("desea ingresar otro documento?")
    

print("Cola de impresión:")
while not cola_prioridad.empty():
    categoria, documento = cola_prioridad.get()
    print(f"Categoría: {'empleado' if categoria == 1 else 'TI' if categoria == 2 else 'gerente'}, Documento: {documento}")
    

