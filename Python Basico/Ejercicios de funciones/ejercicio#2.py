
#1. Intente acceder a una variable definida dentro de una función desde afuera.

# Esto no es posible, ya que las variables definidas dentro de una función son locales a esa función y no pueden ser accedidas desde fuera de ella. si lo hacemos, vamos a tener un error de NameError indicando que la variable no está definida. Por lo que solo podemos obtenerla con el return.

print ("Ejercicio #1")

def mi_funcion():
    name = "Daniel"
    return name

print("Obteniendo desde fuera de la función:", mi_funcion())



#2. Intente acceder a una variable global desde una función y cambiar su valor.

print ("\n\nEjercicio #2")

name = "Daniel"

def mi_funcion():
    global name
    name = "Josue"

mi_funcion()
print(name)
