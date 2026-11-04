class Node:
  data: str
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

class DoubleEndedQueue:
  head: Node
  def __init__(self, head = None):
    self.head = head

  def print_structure(self):
    current_node = self.head
    if current_node is None:
      print("(vacío)")
    
    while (current_node is not None):
      print(current_node.data)
      current_node = current_node.next

  def push_left(self, new_node):
    new_node.next = self.head
    self.head = new_node

  def push_right(self, new_node):
    if self.head is None:
      self.head = new_node
      return

    current_node = self.head
    while (current_node.next is not None):
      current_node = current_node.next
      
    current_node.next = new_node

  def pop_left(self):
    if self.head is not None:
      self.head = self.head.next

  def pop_right(self):
    if self.head is None:
      return
      
    if self.head.next is None:
      self.head = None
      return
      
    current_node = self.head
    while (current_node.next.next is not None):
      current_node = current_node.next
      
    current_node.next = None


deque = DoubleEndedQueue(Node("Nodo Central"))

print("Inicio:")
deque.print_structure()
print("\n")

print("Push_left:")
deque.push_left(Node("Izquierda 1"))
deque.print_structure()
print("\n")

print("Push_right:")
deque.push_right(Node("Derecha 1"))
deque.print_structure()
print("\n")

print("Pop_right:")
deque.pop_right()
deque.print_structure()
print("\n")

print("Pop_left:")
deque.pop_left()
deque.print_structure()