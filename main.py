import random

helados = []  # Lista vacia para almacenar los helados

print("-------HELADOS LOS MEJORES--------")
print("1.INGRESE UN HELADO A LA LISTA")
print("2.VERIFICAR LISTA DE HELADOS")
print("3.EDITAR LISTA DE HELADOS")
print("4.ELIMINAR HELADO POR SU ID")
print("5.SALIR")


opcion = 0
while opcion !=5:
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print("\nIngrese un helado a la lista")
        helado = {
             "id": random.randint(1, 30),
             "nombre": input("Digita el nombre del helado: "),
             "descripcion": input("Ingresa la descripcion del helado: "),
             "precio": int(input("Ingrese el precio del helado: "))
        }

    # Agregar un helado
        helados.append(helado)
        print("\nHelado ingresdo con exito")
        print("Lista de helados: ", helado)
    
    # Ver lista de helados
    elif opcion == 2:
         print("\nLista de Helados:")
         if helados: 
            for heladoseleccionado in helados:
                print(f"ID: {heladoseleccionado['id']} - Nombre: {heladoseleccionado['nombre']} - Descripcion: {heladoseleccionado['descripcion']} - Precio: {heladoseleccionado['precio']}")
         else:
            print("No hay helados en la lista")
    
    # Modificar un helado
    elif opcion == 3:
        print("\nModificar un helado")
        heladocambio = int(input("Digita el id del helado que deseas modificar: "))
         
        #buscar el helado por el id
        for heladobuscado in helados:
            if heladobuscado["id"] == heladocambio:
                print("Helado encontrado: ", heladobuscado)

                #permitir editar valores
                heladobuscado["nombre"] = input("Ingrese el nuevo nombre: ")
                heladobuscado["descripcion"] = input("Ingrese una nueva descripcion: ")
                heladobuscado["precio"] = input("Ingrese un nuevo precio: ")
                print("Helado actualizado con exito: ")
                break
        else:
             print("NO se encontro un helado con ese id")   
              
        # Eliminar un helado
    elif opcion == 4:  
         print("\nEliminar helado de la vista: ")
         heladoid = int(input("Digita el id del helado que desea eliminar: "))
         
         for helado in helados:
             if helado["id"] == heladoid:
                 helados.remove(helado)
                 print("Helado eliminado con exito")
                 break
         else:
              print("No se encontro un helado con ese id")    
        
          # Salir
    elif opcion == 5:
        print("Saliendo del programa...")  
    else:
        print("Opción inválida, intente nuevamente.")