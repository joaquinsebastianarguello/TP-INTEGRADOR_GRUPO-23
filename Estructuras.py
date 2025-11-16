

#   LISTA ENLAZADA SIMPLE


class nodoLista(object):
    info, sig = None, None


class lista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0

    def insertar(self, dato):
        nuevo_nodo = nodoLista()
        nuevo_nodo.info = dato

        if (self.inicio is None):
            nuevo_nodo.sig = self.inicio
            self.inicio = nuevo_nodo

        else:
            nuevo_nodo.sig = self.inicio
            self.inicio = nuevo_nodo

        self.tamaño += 1

    def recorrer(self):
        actual = self.inicio
        while actual is not None:
            print("- " + str(actual.info))
            actual = actual.sig

    def obtener_todos(self):
        elementos = []
        actual = self.inicio
        while actual is not None:
            elementos.append(actual.info)
            actual = actual.sig
        return elementos

    def buscar(self, dato):
        actual = self.inicio
        while actual is not None:
            if actual.info == dato:
                return actual
            actual = actual.sig
        return None

    def eliminar(self, dato):
        actual = self.inicio
        anterior = None

        while actual is not None:
            if actual.info == dato:
                if anterior is None:
                    self.inicio = actual.sig
                else:
                    anterior.sig = actual.sig
                self.tamaño -= 1
                return True
            anterior = actual
            actual = actual.sig
        return False



#   PILA (LIFO)


class Pila(object):
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def buscar(self, elemento):
        for i, item in enumerate(self.items):
            if item == elemento:
                return i
        return None

    def extraer(self, elemento):
        temporal = []
        encontrado = None

        while not self.esta_vacia():
            item = self.desapilar()
            if item == elemento and encontrado is None:
                encontrado = item
            else:
                temporal.append(item)

        while len(temporal) > 0:
            self.apilar(temporal.pop())

        return encontrado



#   COLA (FIFO)


class Cola(object):
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.items) == 0



#   ÁRBOL GENERAL (RECURSIVO)


class nodoArbol(object):
    def __init__(self, info):
        self.info = info
        self.hijos = []        # lista de subárboles

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def recorrer(self, nivel=0):
        sangria = "  " * nivel
        print(sangria + str(self.info))
        for hijo in self.hijos:
            hijo.recorrer(nivel + 1)

    def buscar(self, dato):
        if self.info == dato:
            return self
        for hijo in self.hijos:
            resultado = hijo.buscar(dato)
            if resultado is not None:
                return resultado
        return None
