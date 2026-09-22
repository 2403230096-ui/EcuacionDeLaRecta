### Nombre:     Lopez Angulo Marco Adel
### Matricula:  2403230096
### Asignatura: Ciencia de Datos
### Fecha:      09/20/2026

m = int(input("Ingresa el valor de m: "))
b = int(input("Ingresa el valor de b: "))
x = int(input("Ingresa el valor limite: "))
if x <= 0:
    print("Error: el valor limite debe ser mayor a 0")
    exit()

for i in range(1, x+1):
    calcular_y = (m * i) + b
    print(f"x: {i} | y: {calcular_y}")
