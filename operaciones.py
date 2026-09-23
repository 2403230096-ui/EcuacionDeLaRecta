import re  # se usa para separar los terminos de la cadena (mx y b)


class FuncionLineal:
    """
    Clase para los atributos de la funcion lineal
    y = mx + b

    """
    def __init__(self, m=None, b=None, limite=None):
        self.m = m            # pendiente de la funcion
        self.b = b            # ordenada al origen
        self.limite = limite  # hasta que valor de x se va a calcular


def calcular_y(valor_m, valor_x, valor_b):
    # aplica la formula y = mx + b
    valor_y = (valor_m * valor_x) + valor_b
    return valor_y


def parsear_funcion(cadena):
    """
    Recibe una cadena de texto con la funcion lineal, por ejemplo:
    "y = 2x + 3", "2x+3", "-x-5", "3-2x"
    y regresa los valores de m y b
    """
    cadena = cadena.replace(" ", "")  # quita espacios para facilitar la lectura

    if cadena.lower().startswith("y="):
        cadena = cadena[2:]  # quita el "y=" si el usuario lo escribio

    valor_m = 0
    valor_b = 0

    # separa la cadena en terminos, cada uno con su signo (ej: "+2x", "-3")
    terminos = re.findall(r'[+-]?[^+-]+', cadena)

    for termino in terminos:
        if "x" in termino:
            # es el termino de la x, se obtiene el coeficiente (m)
            coeficiente = termino.replace("x", "")
            if coeficiente in ("", "+"):
                coeficiente = "1"     # caso "x" o "+x" -> m = 1
            elif coeficiente == "-":
                coeficiente = "-1"    # caso "-x" -> m = -1
            valor_m = int(coeficiente)
        else:
            # es el termino independiente (b)
            valor_b = int(termino)

    return valor_m, valor_b