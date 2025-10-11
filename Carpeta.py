from estructuras import ListaEnlazada

class Carpeta:                          # carpeta dentro del cliente de correo. 
                                        # Puede contener mensajes y subcarpetas, formando una estructura recursiva.
    def __init__(self, nombre:str):
        self.__nombre = nombre
        self.__mensajes = ListaEnlazada()   # Lista enlazada de mensajes
        self.__subcarpetas = []             # Lista de subcarpetas hijas

    # MÉTODOS GETTERS
    def get_nombre(self):                   # arroja el nombre de la carpeta
        return self.__nombre

    def get_mensajes(self):                 # lista enlazada de mensajes almacenado
        return self.__mensajes

    def get_subcarpetas(self):
        return self.__subcarpetas

    # MÉTODOS 
    def agregar_mensaje(self, mensaje):                      
        self.__mensajes.agregar(mensaje)
        print("Mensaje agregado en la carpeta: " + self.__nombre)

    def eliminar_mensaje(self, mensaje):
        self.__mensajes.eliminar(mensaje)
        print("Mensaje eliminado de la carpeta: " + self.__nombre)

    def agregar_subcarpeta(self, subcarpeta):               #cuando se acrega subcarpeta se desarrolla nodo hijo
        self.__subcarpetas.append(subcarpeta)
        print("Subcarpeta agregada a " + self.__nombre + ": " + subcarpeta.get_nombre())

    def buscar_subcarpeta(self, nombre):                    # busqueda recursiva si encuentra la subcarpeta la devuelve, sino muestra None
        for sub in self.__subcarpetas:
            if sub.get_nombre() == nombre:
                return sub
            resultado = sub.buscar_subcarpeta(nombre)
            if resultado is not None:
                return resultado
        return None

    def listar_contenido(self, nivel=0):            #Muestra de forma recursiva las carpetas, el nivel de arbos es amrcado por las sangrias, cuando mas espaciado el nodo es de un grado menor
        sangria = "  " * nivel
        print(sangria + "Carpeta: " + self.__nombre)
        for mensaje in self.__mensajes.recorrer():                        # Mostrar mensajes de la carpeta actual
            print(sangria + "   Asunto: " + mensaje.get_asunto())

        for subcarpeta in self.__subcarpetas:                             # Mostrar contenido de las subcarpetas (recursividad)
            subcarpeta.listar_contenido(nivel + 1)

    def buscar_mensaje_por_asunto(self, palabra):              # Busqueda por palabra, hace lista de los mensajes que tienen esa palabra en asunto
        encontrados = []                                       # inicializa con lisat vacia
        
        for mensaje in self.__mensajes.recorrer():             # Buscar en la carpeta actual 
            if palabra.lower() in mensaje.get_asunto().lower():
                encontrados.append(mensaje)
        
        for subcarpeta in self.__subcarpetas:                  # Buscar en subcarpetas
            encontrados += subcarpeta.buscar_mensaje_por_asunto(palabra)

        return encontrados

    def mover_mensaje(self, mensaje, carpeta_destino):
       
        self.eliminar_mensaje(mensaje)
        carpeta_destino.agregar_mensaje(mensaje)
        print("Mensaje movido de " + self.__nombre + " a " + carpeta_destino.get_nombre())

