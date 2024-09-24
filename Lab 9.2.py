import random

#Problema 1 implementacion de las clase chained_hash

#Clase nodo
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

#Clase de lista enlasada doble
class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addlast(self, key, value):
        new_node = Node(key, value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find(self,key):
        actual = self.head
        while actual:
            if actual.key == key:
                return actual.value
            actual = actual.next
        return None

    def remove(self,key):
        actual = self.head
        while actual:
            if actual.key == key:
                if actual.prev:
                    actual.prev.next = actual.next
                if actual.next:
                    actual.next.prev = actual.prev
                if actual == self.head:
                    self.head = actual.next
                if actual == self.tail:
                    self.tail = actual.prev
                return True
            actual = actual.next
        return False

#clase hash
class Chained_Hash:
    def __init__(self, size, method="division", A=0.6180339887):
        self.size = size
        self.table = [DoubleList() for _ in range(size)]
        self.method = method
        self.A = A

    def hash_function(self, key):
        if self.method == "division":
            return key % self.size
        elif self.method == "multiplicacion":
            return int(self.size * ((key * self.A) % 1))

    def insert(self, key, value):
        indice = self.hash_function(key)
        self.table[indice].addlast(key,value)

    def search(self, key):
        indice = self.hash_function(key)
        return self.table[indice].find(key)

    def delete(self, key):
        indice = self.hash_function(key)
        return self.table[indice].remove(key)

#Problema 2 prueba de la implementación

#se crean las 2 tablas a probar
hash_table_division = Chained_Hash(10, 'division')
hash_table_multiplication = Chained_Hash(10, 'multiplicacion')

#se crean numeros aleatorios
numeros = [random.randint(0,100) for _ in range(20)]

#se incertan los numeros aleatorios en la tabla de division
for numero in numeros:
    hash_table_division.insert(numero, numero)

#se busca el numero en la tabla de division
buscar_numero = numeros[0]
encuentra_division = hash_table_division.search(buscar_numero)
print(f"Numero {buscar_numero} encontrado en (division):", encuentra_division)

#se borra el numero en la tabla de division
borrar_numero = numeros[1]
hash_table_division.delete(borrar_numero)
print(f"Numero {borrar_numero} eliminado de (division)")

#se incertan los numeros aleatorios en la tabla de multiplicacion
for numero in numeros:
    hash_table_multiplication.insert(numero, numero)

#se busca el numero en la tabla de multiplicacion
encuentra_multiplicacion = hash_table_division.search(buscar_numero)
print(f"Numero {buscar_numero} encontrado en (multiplicacion):", encuentra_multiplicacion)

#se borra el numero en la tabla de multiplicacion
hash_table_multiplication.delete(borrar_numero)
print(f"Numero {borrar_numero} eliminado de (multiplicacion)")