from abc import ABC, abstractmethod

class InterfazCorreo(ABC):
    @abstractmethod
    def enviar_mensaje(self, destinatario, asunto, contenido, prioridad=False):
        pass

    @abstractmethod
    def recibir_mensaje(self, mensaje):
        pass

    @abstractmethod
    def listar_mensaje(self):
        pass
