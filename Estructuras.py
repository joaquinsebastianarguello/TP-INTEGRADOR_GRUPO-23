
# LISTA

class nodoLista(object):
    info, sig = None, None


class lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato):
    nodo = nodoLista()
    nodo.info = dato

    if (lista.inicio is None) or (lista.inicio.info > dato):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig

        while (actual is not None) and (actual.info < dato):
            anterior = actual
            actual = actual.sig

        nodo.sig = actual
        anterior.sig = nodo

    lista.tamanio += 1


def buscar(lista, clave):
    actual = lista.inicio
    while actual is not None:
        if actual.info == clave:
            return actual
        actual = actual.sig
    return None


def buscar_todos(lista, clave):
    elementos = []
    actual = lista.inicio

    while actual is not None:
        if actual.info == clave:
            elementos.append(actual.info)
        actual = actual.sig
    return elementos


def eliminar(lista, clave):
    actual = lista.inicio
    anterior = None

    while actual is not None:
        if actual.info == clave:
            if anterior is None:
                lista.inicio = actual.sig
            else:
                anterior.sig = actual.sig
            lista.tamanio -= 1
            return True
        anterior = actual
        actual = actual.sig

    return False


def obtener_todos(lista):
    elementos = []
    actual = lista.inicio
    while actual is not None:
        elementos.append(actual.info)
        actual = actual.sig
    return elementos



# PILA 

class nodoPila(object):
    info, sig = None, None


class pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, dato):
    nuevo = nodoPila()
    nuevo.info = dato
    nuevo.sig = pila.cima
    pila.cima = nuevo
    pila.tamanio += 1


def desapilar(pila):
    if pila.cima is None:
        return None
    dato = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return dato


def pila_vacia(pila):
    return pila.cima is None


def pila_buscar(pila, elemento):
    actual = pila.cima
    posicion = 0
    while actual is not None:
        if actual.info == elemento:
            return posicion
        actual = actual.sig
        posicion += 1
    return None


def pila_extraer(pila, elemento):
    temporal = []
    encontrado = None

    while not pila_vacia(pila):
        item = desapilar(pila)
        if item == elemento and encontrado is None:
            encontrado = item
        else:
            temporal.append(item)

    while len(temporal) > 0:
        apilar(pila, temporal.pop())

    return encontrado



# COLA 

class nodoCola(object):
    info, sig = None, None


class cola(object):
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def encolar(cola, dato):
    nuevo = nodoCola()
    nuevo.info = dato

    if cola.frente is None:
        cola.frente = nuevo
    else:
        cola.final.sig = nuevo

    cola.final = nuevo
    cola.tamanio += 1


def desencolar(cola):
    if cola.frente is None:
        return None

    dato = cola.frente.info
    cola.frente = cola.frente.sig

    if cola.frente is None:
        cola.final = None

    cola.tamanio -= 1
    return dato


def cola_vacia(cola):
    return cola.frente is None



# ARBOL GENERAL 

class nodoArbol(object):
    info, hijo, hermano = None, None, None


class arbol(object):
    def __init__(self, nombre_raiz):
        self.raiz = nodoArbol()
        self.raiz.info = nombre_raiz


def agregar_hijo(padre, nombre):
    nuevo = nodoArbol()
    nuevo.info = nombre
    nuevo.hermano = padre.hijo
    padre.hijo = nuevo
    return nuevo


def buscar_arbol(nodo, nombre):
    if nodo is None:
        return None

    if nodo.info == nombre:
        return nodo

    resultado = buscar_arbol(nodo.hijo, nombre)
    if resultado is not None:
        return resultado

    return buscar_arbol(nodo.hermano, nombre)


def mostrar_arbol(nodo, nivel=0):
    if nodo is not None:
        print("  " * nivel + "- " + str(nodo.info))
        mostrar_arbol(nodo.hijo, nivel + 1)
        mostrar_arbol(nodo.hermano, nivel)
