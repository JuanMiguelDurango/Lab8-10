import csv
import heapq

# Clase para representar el grafo usando listas de adyacencia
class Grafo:
    def __init__(self):
        self.grafo = {}

    # Método para agregar una arista entre dos ciudades
    def agregar_arista(self, ciudad_a, ciudad_b, distancia, tiempo):
        if ciudad_a not in self.grafo:
            self.grafo[ciudad_a] = []
        if ciudad_b not in self.grafo:
            self.grafo[ciudad_b] = []
        # Agregar las conexiones para ambas ciudades
        self.grafo[ciudad_a].append((ciudad_b, distancia, tiempo))
        self.grafo[ciudad_b].append((ciudad_a, distancia, tiempo))

    # Constructor del grafo con el archivo csv
    def cargar_datos(self, archivo):
        with open(archivo, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Omitir la primera fila si es una cabecera
            for row in reader:
                ciudad_a, ciudad_b, distancia, tiempo = row
                # Asegurarse de que 'distancia' y 'tiempo' sean numéricos
                try:
                    distancia = float(distancia)
                    tiempo = float(tiempo)
                    self.agregar_arista(ciudad_a, ciudad_b, distancia, tiempo)
                except ValueError:
                    print(f"Error al convertir los valores de distancia o tiempo en la fila: {row}")

    # Verificar si están conectados por una único camino
    def estan_conectadas(self, ciudad_a, ciudad_b):
        if ciudad_a in self.grafo:
            for vecino in self.grafo[ciudad_a]:
                if vecino[0] == ciudad_b:
                    return True
        return False

    # Función para determinar el camino más corto en distancia utilizando Dijkstra
    def camino_mas_corto_distancia(self, ciudad_a, ciudad_b):
        if ciudad_a not in self.grafo or ciudad_b not in self.grafo:
            return None
        
        # Inicializar la distancia mínima a infinito para todas las ciudades
        distancias = {ciudad: float('inf') for ciudad in self.grafo}
        distancias[ciudad_a] = 0
        
        # Usar un heap para priorizar las ciudades con la menor distancia
        cola_prioridad = [(0, ciudad_a)]  # (distancia, ciudad)
        camino_previo = {}

        while cola_prioridad:
            distancia_actual, ciudad_actual = heapq.heappop(cola_prioridad)

            if ciudad_actual == ciudad_b:
                # Reconstruir el camino más corto
                camino = []
                while ciudad_actual in camino_previo:
                    camino.insert(0, ciudad_actual)
                    ciudad_actual = camino_previo[ciudad_actual]
                camino.insert(0, ciudad_a)
                return camino, distancias[ciudad_b]

            for vecino, dist, _ in self.grafo[ciudad_actual]:
                nueva_distancia = distancia_actual + dist
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    camino_previo[vecino] = ciudad_actual
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
        
        return None

    # Función para determinar el camino más corto en tiempo utilizando Dijkstra
    def camino_mas_corto_tiempo(self, ciudad_a, ciudad_b):
        if ciudad_a not in self.grafo or ciudad_b not in self.grafo:
            return None
        
        # Inicializar el tiempo mínimo a infinito para todas las ciudades
        tiempos = {ciudad: float('inf') for ciudad in self.grafo}
        tiempos[ciudad_a] = 0
        
        # Usar un heap para priorizar las ciudades con el menor tiempo
        cola_prioridad = [(0, ciudad_a)]  # (tiempo, ciudad)
        camino_previo = {}

        while cola_prioridad:
            tiempo_actual, ciudad_actual = heapq.heappop(cola_prioridad)

            if ciudad_actual == ciudad_b:
                # Reconstruir el camino más corto
                camino = []
                while ciudad_actual in camino_previo:
                    camino.insert(0, ciudad_actual)
                    ciudad_actual = camino_previo[ciudad_actual]
                camino.insert(0, ciudad_a)
                return camino, tiempos[ciudad_b]

            for vecino, _, tiempo in self.grafo[ciudad_actual]:
                nuevo_tiempo = tiempo_actual + tiempo
                if nuevo_tiempo < tiempos[vecino]:
                    tiempos[vecino] = nuevo_tiempo
                    camino_previo[vecino] = ciudad_actual
                    heapq.heappush(cola_prioridad, (nuevo_tiempo, vecino))
        
        return None


# Función principal para ejecutar el programa para el usuario
def main():
    grafo = Grafo()
    grafo.cargar_datos('Datos vias Colombia.csv')

    while True:
        print("\nSeleccione una opción:")
        print("1. Verificar si dos ciudades están conectadas por una única carretera")
        print("2. Camino más corto en distancia (KM) entre dos ciudades")
        print("3. Camino más corto en tiempo (Minutos) entre dos ciudades")
        print("4. Salir")
        
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            ciudad_a = input("Ingrese la ciudad A: ")
            ciudad_b = input("Ingrese la ciudad B: ")
            if grafo.estan_conectadas(ciudad_a, ciudad_b):
                print(f"{ciudad_a} y {ciudad_b} están conectadas por una única carretera.")
            else:
                print(f"{ciudad_a} y {ciudad_b} NO están conectadas por una única carretera.")
        elif opcion == '2':
            ciudad_a = input("Ingrese la ciudad A: ")
            ciudad_b = input("Ingrese la ciudad B: ")
            resultado = grafo.camino_mas_corto_distancia(ciudad_a, ciudad_b)
            if resultado:
                camino, distancia = resultado
                print(f"El camino más corto entre {ciudad_a} y {ciudad_b} es: {camino} con una distancia de {distancia} KM.")
            else:
                print(f"No hay camino entre {ciudad_a} y {ciudad_b}.")
        elif opcion == '3':
            ciudad_a = input("Ingrese la ciudad A: ")
            ciudad_b = input("Ingrese la ciudad B: ")
            resultado = grafo.camino_mas_corto_tiempo(ciudad_a, ciudad_b)
            if resultado:
                camino, tiempo = resultado
                print(f"El camino más corto entre {ciudad_a} y {ciudad_b} es: {camino} con un tiempo de {tiempo} minutos.")
            else:
                print(f"No hay camino entre {ciudad_a} y {ciudad_b}.")
        elif opcion == '4':
            break

if __name__ == "__main__":
    main()