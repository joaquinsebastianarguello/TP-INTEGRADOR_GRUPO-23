

import datetime

class Mensaje:

    def __init__(self, remitente, destinatario, asunto, contenido, prioridad=False):
        self.__remitente = remitente

        if isinstance(destinatario, list):
            self.__destinatarios = destinatario
        else:
            self.__destinatarios = [destinatario]

        self.__asunto = asunto
        self.__contenido = contenido
        self.__prioridad = prioridad
        self.__destacado = False
        self.__adjuntos = []
        self.__fecha = datetime.datetime.now()

    # GETTERS
    def get_remitente(self):
        return self.__remitente

    def get_destinatarios(self):
        return self.__destinatarios

    def get_asunto(self):
        return self.__asunto

    def get_contenido(self):
        return self.__contenido

    def get_prioridad(self):
        return self.__prioridad

    def get_destacado(self):
        return self.__destacado

    def get_adjuntos(self):
        return self.__adjuntos

    def get_fecha(self):
        return self.__fecha

    # SETTERS
    def set_prioridad(self, valor):
        self.__prioridad = valor

    def set_destacado(self, valor):
        self.__destacado = valor

    # METODOS
    def es_prioritario(self):
        return self.__prioridad

    def marcar_destacado(self):
        self.__destacado = True

    def quitar_destacado(self):
        self.__destacado = False

    def adjuntar(self, tipo, nombre, ruta):
        adj = {"tipo": tipo, "nombre": nombre, "ruta": ruta}
        self.__adjuntos.append(adj)

    def mostrar_mensaje(self):
        prioridad_txt = "URGENTE" if self.__prioridad else "Normal"
        destacado_txt = "SI" if self.__destacado else "NO"

        texto = "De: " + self.__remitente + "\n"
        texto += "Para: " + ", ".join(self.__destinatarios) + "\n"
        texto += "Asunto: " + self.__asunto + "\n"
        texto += "Fecha: " + str(self.__fecha) + "\n"
        texto += "Prioridad: " + prioridad_txt + "\n"
        texto += "Destacado: " + destacado_txt + "\n"
        texto += "\n" + self.__contenido + "\n"

        if len(self.__adjuntos) > 0:
            texto += "Adjuntos:\n"
            for adj in self.__adjuntos:
                texto += "- " + adj["tipo"] + ": " + adj["nombre"] + " (" + adj["ruta"] + ")\n"

        return texto
