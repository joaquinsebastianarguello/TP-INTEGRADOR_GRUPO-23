
from Estructuras import ListaEnlazada, Pila

class Carpeta:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = ListaEnlazada()
        self.__subcarpetas = []
        self.__pila_auxiliar = Pila()

    #          GETTERS
  

    def get_nombre(self):
        return self.__nombre

    def get_mensajes(self):
        return self.__mensajes

    def get_subcarpetas(self):
        return self.__subcarpetas

    def get_tamaño(self):
        return self.__mensajes.tamaño

   
    #          SETTERS
   

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    
    #          MÉTODOS
   

    def agregar_mensaje(self, mensaje):
        self.__mensajes.insertar(mensaje)

    def eliminar_mensaje(self, mensaje):
        eliminado = self.__mensajes.eliminar(mensaje)
        if eliminado:
            self.__pila_auxiliar.apilar(mensaje)
        return eliminado

    def recuperar_ultimo_eliminado(self):
        if not self.__pila_auxiliar.esta_vacia():
            mensaje = self.__pila_auxiliar.desapilar()
            self.__mensajes.insertar(mensaje)
            return mensaje
        return None

    def agregar_subcarpeta(self, subcarpeta):
        self.__subcarpetas.append(subcarpeta)

    def buscar_subcarpeta(self, nombre):
        for sub in self.__subcarpetas:
            if sub.get_nombre() == nombre:
                return sub
            
            resultado = sub.buscar_subcarpeta(nombre)
            if resultado is not None:
                return resultado

        return None

    def listar_contenido(self, nivel=0):
        sangria = "  " * nivel
        print(sangria + "Carpeta: " + self.__nombre)

        mensajes = self.__mensajes.obtener_todos()
        for mensaje in mensajes:
            print(sangria + "   Asunto: " + mensaje.get_asunto())

        for subcarpeta in self.__subcarpetas:
            subcarpeta.listar_contenido(nivel + 1)

    def buscar_mensaje_por_asunto(self, palabra):
        encontrados = []

        mensajes = self.__mensajes.obtener_todos()
        for mensaje in mensajes:
            if palabra.lower() in mensaje.get_asunto().lower():
                encontrados.append(mensaje)

        for subcarpeta in self.__subcarpetas:
            encontrados += subcarpeta.buscar_mensaje_por_asunto(palabra)

        return encontrados

    def mover_mensaje(self, mensaje, carpeta_destino):
        if self.eliminar_mensaje(mensaje):
            carpeta_destino.agregar_mensaje(mensaje)

    def vaciar_carpeta(self):
        self.__mensajes = ListaEnlazada()
        self.__pila_auxiliar = Pila()


