class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Inserta un nodo al final de la lista."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def insert_at_beginning(self, data):
        """Inserta un nodo al principio de la lista."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_position(self, position):
        """Elimina un nodo en una posición específica."""
        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        k = 0
        while current and k < position - 1:
            current = current.next
            k += 1

        if current and current.next:
            current.next = current.next.next
        else:
            print("Posición inválida.")

    def delete_by_value(self, value):
        """Elimina el primer nodo que contenga un valor específico."""
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        """Imprime los datos de todos los nodos en la lista."""
        current = self.head
        while current:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print("Lista después de insertar al final:")
    linked_list.print_list()

    linked_list.insert_at_beginning(5)
    print("\nLista después de insertar al principio:")
    linked_list.print_list()


    linked_list.delete_at_position(1)
    print("\nLista después de eliminar en posición 1:")
    linked_list.print_list()


    linked_list.delete_by_value(20)
    print("\nLista después de eliminar valor 20:")
    linked_list.print_list()

