#stack
class Nodo:
    def __init__(self,dato):
        self.next=None
        self.dato=dato
    
class Stack:
    def __init__(self):
        self.head=None
    
    def push(self,data):
        new_node= Nodo(data)
        if self.head=None: