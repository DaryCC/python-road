class Nodo:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.Head=None

    def append(self,data):
        nuevo_nodo=Nodo(data)
        if not(self.Head):
            self.Head = nuevo_nodo 
            return
           
        ultimo_nodo=self.Head
        while ultimo_nodo.next:
            ultimo_nodo=ultimo_nodo.next
        ultimo_nodo.next=nuevo_nodo
    def imprime_lista(self):
        nodo_actual=self.Head
        while nodo_actual:
            print(nodo_actual.data)
            nodo_actual=nodo_actual.next

lista= Linked_list()

lista.append('Maria')
lista.append('Jose')
lista.append('Nadia')
lista.append('Emma')

lista.imprime_lista()
        
        




