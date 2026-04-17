my_string = "python-variable-funcion-computadora-monitor"


def order_words(string):
    lista = string.split("-")
    lista.sort()
    resultado = "-".join(lista)
    return resultado

print(order_words(my_string))