### Nombre:     Lopez Angulo Marco Adel
### Matricula:  2403230096
### Asignatura: Ciencia de Datos
### Fecha:      09/20/2026

## Validar Opciones /

from operaciones import FuncionLineal
from operaciones import calcular_y
from operaciones import parsear_funcion

print("------ Menu Principal ------")

def mostrar_menu():
    print("\n Option 1: Guardar Funcion")
    print("\n Option 2: Guardar Valor Limite")
    print("\n Option 3: Mostrar Resultados")
    print("\n Option 4: Salir del Programa")

def main():
    funcion = FuncionLineal()  # objeto donde se guardan m, b y el limite

    while True:
        mostrar_menu()
        Opcion = input("\nSelecciona una de las opciones: "
        "")

        if Opcion == "1":
            # pide la funcion como texto y la convierte en m y b
            cadena_funcion = input("\nIngresa la funcion (ejemplo: y = 2x + 3): ")
            funcion.m, funcion.b = parsear_funcion(cadena_funcion)

        elif Opcion == "2":
            # hasta que valor de x se van a calcular los resultados
            funcion.limite = int(input("\nIngresa el valor limite: "))

        elif Opcion == "3":
            # verifica que ya se hayan guardado todos los datos
            if (funcion.m is None or
                funcion.b is None or
                funcion.limite is None):

                print("\nHacen falta datos dentro de la funcion")
            else:
                if funcion.limite <= 0:
                    print("\nError: el valor limite debe ser mayor a 0")
                    continue

                print("------------------------------------------------------------------------------------------------")

                # calcula y muestra el valor de y para cada x, de 1 hasta el limite
                for i in range(1, funcion.limite + 1):
                    valor_y = calcular_y(funcion.m, i, funcion.b)
                    print(f"x: {i} | y: {valor_y}")

                print("------------------------------------------------------------------------------------------------")

        elif Opcion == "4":
            # termina el programa
            print("------------------------------------------------------------------------------------------------")
            print("\nGracias por usar el programa.")
            print(":)")
            break

if __name__ == "__main__":
    main()