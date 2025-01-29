import math

def suma_complejos(x=[], y=[]):
    parte_real = x[0] + y[0]
    parte_imaginaria = x[1] + y[1]
    return (round(parte_real, 4), round(parte_imaginaria, 4))

def resta_complejos(x=[], y=[]):
    parte_real = x[0] - y[0]
    parte_imaginaria = x[1] - y[1]
    return (round(parte_real, 4), round(parte_imaginaria, 4))

def multiplicar_complejos(x=[], y=[]):
    parte_real = x[0] * y[0] - x[1] * y[1]
    parte_imaginaria = x[0] * y[1] + y[0] * x[1]
    return (round(parte_real, 4), round(parte_imaginaria, 4))

def dividir_complejos(x=[], y=[]):
    denominador = (y[0] ** 2) + (y[1] ** 2)
    parte_real = ((x[0] * y[0]) + (x[1] * y[1])) / denominador
    parte_imaginaria = ((y[0] * x[1]) - (x[0] * y[1])) / denominador
    return (round(parte_real, 4), round(parte_imaginaria, 4))

def modulo_complejo(x=[]):
    return round(math.sqrt((x[0] ** 2) + (x[1] ** 2)), 4)

def conjugado_complejo(x=[]):
    return (x[0], -x[1])

def convertir_formato(x=[], tipo=""):
    if tipo.lower() == "cartesiano":
        parte_real = x[0] * math.cos(x[1])
        parte_imaginaria = x[0] * math.sin(x[1])
        return (round(parte_real, 4), round(parte_imaginaria, 4))
    elif tipo.lower() == "polar":
        magnitud = modulo_complejo(x)
        angulo = calcular_fase(x)
        return (magnitud, angulo)
    raise Exception("Solo se pueden hacer conversiones a formato polar o cartesiano")

def calcular_fase(x=[]):
    return round(math.atan(x[1] / x[0]), 4)

def imprimir_pretty(real, imaginario):
    if imaginario < 0:
        return f"{real}{imaginario}i"
    return f"{real}+{imaginario}i"
