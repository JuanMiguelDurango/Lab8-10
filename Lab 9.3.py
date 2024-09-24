#Clase usuario
class Usuario:
    def __init__(self, nombre, id_num):
        self.nombre = nombre
        self.id_num = id_num

    def __repr__(self):
        return f"Usuario({self.nombre}, ID: {self.id_num})"

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

#Cuenta cuantos elementos hay en la lista
    def count(self):
        count = 0
        actual = self.head
        while actual:
            count += 1
            actual = actual.next
        return count
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
 #Cuenta las entradas   
    def count_entries(self):
        counts = []
        for i, lista in enumerate(self.table):
            counts.append(lista.count())
        return counts
    
# Prueba con 6 usuarios
usuarios = [
    Usuario("Alice", 101),
    Usuario("Bob", 202),
    Usuario("Charlie", 303),
    Usuario("David", 404),
    Usuario("Eve", 505),
    Usuario("Frank", 606)
]

# Prueba con método de división
print("Prueba con método de división:")
hash_division = Chained_Hash(5, method="division")
for user in usuarios:
    hash_division.insert(user.id_num, user)

# Imprimir cuántos usuarios fueron almacenados en cada posición
counts_division = hash_division.count_entries()
for i, count in enumerate(counts_division):
    print(f"Posición {i}: {count} usuarios")

# Prueba con método de multiplicación
print("\nPrueba con método de multiplicación:")
hash_multiplicacion = Chained_Hash(5, method="multiplicacion")
for user in usuarios:
    hash_multiplicacion.insert(user.id_num, user)

# Imprimir cuántos usuarios fueron almacenados en cada posición
counts_multiplicacion = hash_multiplicacion.count_entries()
for i, count in enumerate(counts_multiplicacion):
    print(f"Posición {i}: {count} usuarios")