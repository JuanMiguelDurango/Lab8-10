class Usuario:
    def __init__(self, nombre, id_num):
        self.nombre = nombre
        self.id_num = id_num

    def __repr__(self):
        return f"Usuario({self.nombre}, ID: {self.id_num})"

class BSTEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Key: {self.key}, Value: {self.value}"
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = BSTEntry(key, value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.key < current.key:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self._search_recursive(current.left, key)
        else:
            return self._search_recursive(current.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current, key):
        if current is None:
            return current
        
        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            
            temp = self._min_value_node(current.right)
            current.key = temp.key
            current.value = temp.value
            current.right = self._delete_recursive(current.right, temp.key)
        
        return current

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_min(self):
        if self.root is None:
            return None
        return self._min_value_node(self.root)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.key, end=" ")
            self._inorder_recursive(node.right)

    def show_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node.right:
            self.show_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.key)
        if node.left:
            self.show_tree(node.left, level + 1)

def sumar_digitos(num):
    return sum(int(digit) for digit in str(num))

# Instanciar el árbol
bst = BinarySearchTree()

# Crear usuarios
usuarios = [
    Usuario("Juan", 10101013),
    Usuario("Pablo", 10001011),
    Usuario("Maria", 10101015),
    Usuario("Ana", 1010000),
    Usuario("Diana", 10111105),
    Usuario("Mateo", 10110005)
]

# Insertar usuarios en el ABB con la clave siendo la suma de los dígitos del ID
for usuario in usuarios:
    clave = sumar_digitos(usuario.id_num)
    bst.insert(clave, usuario)

# Pruebas de los métodos
print("Inorder Traversal (Claves):")
bst.inorder_traversal()

print("\n\nÁrbol:")
bst.show_tree()

print("\nBuscar usuario con clave 4:")
clave_busqueda = sumar_digitos(10001011)
print(bst.search(clave_busqueda))

print("\nValor mínimo:")
print(bst.find_min())

print("\nValor máximo:")
print(bst.find_max())

print("\nEliminar clave de Ana:")
clave_eliminar = sumar_digitos(10101015)
bst.delete(clave_eliminar)

print("\nInorder Traversal después de eliminar:")
bst.inorder_traversal()

print("\n\nÁrbol después de eliminar:")
bst.show_tree()