class Node:
  data: str
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class BinaryTree:
  root: Node
  def __init__(self, root):
    self.root = root

  def print_structure(self):
    print("Raiz:")
    if self.root is not None:
      print(self.root.data)
      
      print("  Hijos de la raíz:")
      if self.root.left is not None:
        print("  Izquierda: " + self.root.left.data)
      if self.root.right is not None:
        print("  Derecha: " + self.root.right.data)



hoja_izq = Node("Soy la hoja izquierda")
hoja_der = Node("Soy la hoja derecha")

raiz = Node("Soy la raíz", hoja_izq, hoja_der)

arbol = BinaryTree(raiz)

arbol.print_structure()