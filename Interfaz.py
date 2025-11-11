from abc import ABC, abstractmethod  

class InterfazCorreo(ABC):    # Acá definimos la interfaz de correo  de forma abstracta, ponemos el formato, para despues definirla en usuario.
  
    @abstractmethod
    def enviar_mensaje(self, destinatario, asunto: str, contenido: str, prioridad: bool = False):   # La documentación necesita el tipo de valor que tiene cada parámetro.
        pass                        # usamos los pass para quqe el codigo no se rompa porque la definición no la estamos ahciendo acá.

    @abstractmethod
    def recibir_mensaje(self, mensaje):
        pass

    @abstractmethod
    def listar_mensaje(self):
        pass

    @abstractmethod
    def agregar_regla_filtro(self, tipo, palabra_clave, carpeta_destino):     #Agrega filtro: tipo(asunto o remitente), palabra_clave (omite mayúscula y busca coincidencia por palabra y no por frase textual)
        pass

    @abstractmethod
    def aplicar_filtros(self):
        pass

    @abstractmethod
    def procesar_mensajes_prioritarios(self):         # esto habilita otros metodos que van a estar definidos mas adelante como moverlos, mostrarlos, ordenarlos, ejecutarlos, vaciar colas despues de procesarlos 
        pass
