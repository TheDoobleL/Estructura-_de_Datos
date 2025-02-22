def conversor_unidades():

    while True:
        print("\nConversor de Unidades")
        print("1. Longitud (metros ↔ pies)")
        print("2. Peso (kilogramos ↔ libras)")
        print("3. Temperatura (Celsius ↔ Fahrenheit)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            valor = float(input("Capture la cantidad: "))
            print("1. Metros a Pies")
            print("2. Pies a Metros")
            sub_opcion = input("Seleccione la conversión (1-2): ")
            if sub_opcion == "1":
                print(f"{valor} metros = {valor * 3.28084} pies")
            elif sub_opcion == "2":
                print(f"{valor} pies = {valor / 3.28084} metros")
            else:
                print("Opción no válida.")

        elif opcion == "2":
            valor = float(input("Ingrese la cantidad: "))
            print("1. Kilogramos a Libras")
            print("2. Libras a Kilogramos")
            sub_opcion = input("Seleccione la conversión (1-2): ")
            if sub_opcion == "1":
                print(f"{valor} kg = {valor * 2.20462} lb")
            elif sub_opcion == "2":
                print(f"{valor} lb = {valor / 2.20462} kg")
            else:
                print("Opción no válida.")

        elif opcion == "3":
            valor = float(input("Capture la temperatura: "))
            print("1. Celsius a Fahrenheit")
            print("2. Fahrenheit a Celsius")
            sub_opcion = input("Seleccione la conversión (1-2): ")
            if sub_opcion == "1":
                print(f"{valor}°C = {(valor * 9/5) + 32}°F")
            elif sub_opcion == "2":
                print(f"{valor}°F = {(valor - 32) * 5/9}°C")
            else:
                print("Opción no válida.")

        elif opcion == "4":
            print("Finalizando programa")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

conversor_unidades()
