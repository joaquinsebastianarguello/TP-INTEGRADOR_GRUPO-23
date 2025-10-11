# Pensamos utilizar las listas enlazadas para almacenar mensajes dentro de cada carpeta
# De la misma manera utilizamos Pila nos serviria como comportamiento para la papelera, estamos en dudas si tambien para deshacer borrados de la papelera
# La cola nos sirve para ServidorCorreo como un sistema de orden de procesamiento de mensajes ingresados, mediante FIFO(Primero entrado, Primero salido)
# Estas estructuras estan puestas en esqueleto, falta seguir trabajando aún.


Class Nodo:                                  # creamos nodo
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class ListaEnlazada:                          # creamos lista enlazada para evr emnsajes dentro de las carpetas, inicia en vacio
    def __init__(self):
        self.inicio = None

    def insertar(self, dato):                 # inserta elemento en la lista
        nuevo = Nodo(dato)
        nuevo.sig = self.inicio
        self.inicio = nuevo

    def recorrer(self):                       # muestar lista en pantalla. inciiando con guion y espacio
        actual = self.inicio
        while actual is not None:
            print("- " + str(actual.dato))
            actual = actual.sig

    def obtener_todos(self):                  # esta es similar a la anterior pero nos permite trabajar en consecuencia, por ejemplo recorrer la lsiat de mensaje para agregar, o eliminar, la anterior termian su trabajo al listarlos e imprimirlos, esta eprmite seguir trabajando a partir de recorrer la lista
        elementos = []
        actual = self.inicio
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.sig
        return elementos

    def eliminar(self, dato):                 #Elimina el primer nodo cuyo dato coincida con el valor recibido. Si no encuentra el elemento, no realiza cambios.  
        actual = self.inicio
        anterior = None
 
        if actual is None:                    # Si la lista esta vacia arroja Falso, no elimina
            return False

        if actual.dato == dato:               # Si el nodo a eliminar es el primero, compara ese elemento, elimina yal finalizar devuelve true
            self.inicio = actual.sig
            return True
 
        while actual is not None:             # Si el nodo está más adelante, busca en forma recursiva con el while, hasta encontrarlo, lo elimina y convierte el posterior en siguiente del anterior.
            if actual.dato == dato:
                anterior.sig = actual.sig
                return True
            anterior = actual
            actual = actual.sig

        return False                          # Si al recorrer toda la lista no se encontró el elemento, arroja falso
 
class Pila:                                   # Creamos pila con metodo LIFO (ultimo entrado, Primero salido)
    def __init__(self):
        self.items = []

    def apilar(self, elemento):               # Agrega elemento en al parte de arriba de la pila
        self.items.append(elemento)

    def desapilar(self):                      # Si como en el topo esta la ultima apilada y el método es LIFO, elimina la de arriba de todo, dejando como tope ahora a la que antes estaba segunda contando desde arriba hacia abajo
        if not self.esta_vacia():             # Si esta vacia la pila devielve None.
            return self.items.pop()
        return None

    def esta_vacia(self):                     # Estará vacia, si sus elementos son nulos
        return len(self.items) == 0

    def buscar(self, elemento):               # Busca un elemento dentro de la fila, lo pensamos desde el punto de busqueda de un mensaje en papelera, su existencia o no.
        for i, item in enumerate(self.items): # Arroja la posición si se encontrara, de lo contrario None
           if item == elemento:
              return i
        return None

    def extraer(self, elemento):              # Elimina un elemento específico de la pila, sin alterar el orden de los demás.
        temporal = []                         # Devuelve el elemento si se encontró y eliminó, o None si no existe.
        encontrado = None
        while not self.esta_vacia():          # Desapilar hasta encontrar el elemento
          item = self.desapilar()
          if item == elemento and encontrado is None:
            encontrado = item                 # Si es encontrado, no lo volvemos a apilar
          else:
            temporal.append(item)             # Lo manda a un temporal hasta que le digamos que hacer con él.

    while len(temporal) > 0:                  # Restaurar los elementos en orden original  
        self.apilar(temporal.pop())

    return encontrado                         # Devuelve encontrado

class Cola:                                   # Creamos cola, con método FIFO (Primero entrado, primero salido)
    def __init__(self):
        self.items = []

    def encolar(self, elemento):              #agrega elemento al final de la cola
        self.items.append(elemento)

    def desencolar(self):                     # saca elemento ultimo de la cola, muestra la anterior
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):                     # estará vacia si sus elementos son nulos
        return len(self.items) == 0           # como la cola organiza las prioridades del Servidor, decidimos no implementar encontrar como sí lo hicimos en pila


