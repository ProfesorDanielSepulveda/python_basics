# Ejercicio tienda:
# Crear una tienda que ofrezca productos y emita boletas en base a los productos que se compran.
# La tienda debe estar en ejecución permanente y debe tener la opción de agregar nuevos productos a la tienda.


#Propuesta básica de solución
#CABECERA
print("*"*50)
print("Tienda".center(50,"*"))
print("*"*50)

l_prod = ["Leche", "Jabón", "Azúcar", "Escoba"]
l_prec = [1490, 1990, 990, 9990]


#LOOP PRINCIPAL
while True:
    prod_comprados = []
    total = 0
    ans = input("\nBienvenido a la tienda, que quieres hacer?\n1. Comprar\n2. Agregar nuevo producto\n3. Salir\n")

    #COMPROBACION ERROR RESPUESTA
    while not ans.isdigit():
        print("\nIngresaste una opción no válida.")
        ans = input("\nBienvenido a la tienda, que quieres hacer?\n1. Comprar\n2. Agregar nuevo producto\n3. Salir\n")

    #HACER COMPRA
    if int(ans) == 1:

        #VARIABLES DE CONTROL DE COMPRA


        #LOOP COMPRA
        while True:
            ans = input("\nQué quieres hacer?\n1. Comprar un producto.\n2. Emitir boleta.\n3. Volver al menú principal\n")

            #CONTROL DE ERRORES
            while not ans.isdigit():
                print("\nIngresaste una opción no válida.")
                ans = input("\nQué quieres hacer?\n1. Comprar un producto.\n2. Emitir boleta.\n3. Volver al menú principal\n")

            #LISTAR PRODUCTOS
            print("\n")
            if int(ans) == 1:
                indice = 0
                for producto in l_prod:
                    print(f"{indice+1}. {producto} - ${l_prec[indice]}")
                    indice += 1

                #ELEGIR UN PRODUCTO
                ans = input("\nQué producto quieres? (Ingresa su número)\n")

                #CONTROL DE ERRORES
                while not ans.isdigit():
                    print("\nIngresaste una opción no válida.")
                    ans = input("Qué producto quieres? (Ingresa su número)\n")

                #PRODUCTO INEXISTENTE
                if int(ans) > indice:
                    print("Ese producto no existe. Trata de nuevo")

                #AGREGAR PRODUCTO
                if int(ans) <= indice and int(ans) > 0:
                    prod_comprados.append(int(ans)-1)
                    total += l_prec[int(ans)-1]

            #EMITIR BOLETA
            elif int(ans) == 2:
                print("BOLETA TIENDA")
                print("DETALLE:\n")
                for prod in prod_comprados:
                    print(f"{l_prod[prod]} - ${l_prec[prod]}")
                print(f"Total a pagar: ${total}")
                break


            #VOLVER
            elif int(ans) == 3:
                break

            #CONTROL DE ERRORES:
            else:
                print("\nEsa opción no está en el menu. Intenta de nuevo")



    #AGREGAR NUEVO PRODUCTO
    elif int(ans) == 2:

        #LOOP AGREGAR PRODUCTO
        while True:
            nom = input("\nPor favor, ingresa el nombre del producto: (Si quieres cancelar, escribe 'x')\n")

            #CANCELAR AGREGAR PRODUCTO NUEVO
            if nom.lower() == "x":
                break

            print(f"\nEl nombre del producto es {nom}.")
            ans = input("Es correcto?(s/n)")

            #COMPROBACIÓN DE ERRORES
            while not ans.isalpha():
                ans = input("Es correcto?(s/n)")

            #PROCEDER A AGREGAR PECIO
            if ans.lower() == "s":
                pre = input("\nPor favor, ingresa el precio del producto:\n")

                #COMPROBACIÓN DE ERRORES
                while not pre.isdigit():
                    pre = input("Por favor, ingresa el precio del producto:\n")
                print(f"\nEl precio del producto es {pre}.")
                ans = input("Es correcto?(s/n)")
                while not ans.isalpha():
                    ans = input("Es correcto?(s/n)")

                #AGREGAR PRODUCTO NUEVO A LAS LISTAS
                if ans.lower() == "s":
                    l_prod.append(nom)
                    l_prec.append(int(pre))
                    break

                #COMPROBACIÓN DE ERRORES - REGRESO A INICIO
                else:
                    pass
            #COMPROBACIÓN DE ERRORES - REGRESO A INICIO
            elif ans.lower() == "n":
                continue

            #COMPROBACIÓN DE ERRORES - REGRESO A INICIO
            else:
                print("Por favor, ingesa una opción válida")

    #SALIR
    elif int(ans) == 3:
        print("\nIniciando proceso de cierre de caja.\nAdiós.")
        break

    #CONTROL DE OPCIONES
    else:
        print("\nEsa opción no está en el menu. Intenta de nuevo")
