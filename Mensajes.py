# ============================================================
# Archivo: mensaje.py
# Descripción: Clase Mensaje - Representa un mensaje de correo.
# Autor: [Tu nombre]
# Fecha: [Fecha de entrega]
# ============================================================


class Mensaje:
    """
    Representa un mensaje de correo electrónico con soporte para adjuntos,
    prioridad y marcado como destacado.
    """

    def __init__(self, remitente, destinatario, asunto, contenido, prioridad=False):
        """
        Constructor de la clase Mensaje.
        Parámetros:
            remitente : str
                Dirección de correo del emisor.
            destinatario : str o list
                Dirección o lista de direcciones de los receptores.
            asunto : str
                Título o tema principal del mensaje.
            contenido : str
                Texto completo del mensaje.
            prioridad : bool
                Indica si el mensaje es prioritario (por defecto False).
        """
        self.__remitente = remitente
        # Se permite que el destinatario sea un solo correo o una lista de ellos.
        if isinstance(destinatario, list):
            self.__destinatarios = destinatario
        else:
            self.__destinatarios = [destinatario]

        self.__asunto = asunto
        self.__contenido = contenido
        self.__prioridad = prioridad
        self.__destacado = False  # Por defecto, no está marcado como destacado
        self.__adjuntos = []      # Lista vacía de adjuntos (archivos, links, etc.)

    # ------------------------------------------------------------
    # MÉTODOS GETTERS (acceso controlado a los datos)
    # ------------------------------------------------------------

    def get_remitente(self):
        """Devuelve el correo del remitente."""
        return self.__remitente

    def get_destinatarios(self):
        """Devuelve la lista de destinatarios del mensaje."""
        return self.__destinatarios

    def get_asunto(self):
        """Devuelve el asunto del mensaje."""
        return self.__asunto

    def get_contenido(self):
        """Devuelve el contenido completo del mensaje."""
        return self.__contenido

    def get_prioridad(self):
        """Devuelve True si el mensaje es prioritario."""
        return self.__prioridad

    def get_destacado(self):
        """Devuelve True si el mensaje está marcado como destacado."""
        return self.__destacado

    def get_adjuntos(self):
        """Devuelve la lista de adjuntos del mensaje."""
        return self.__adjuntos

    # ------------------------------------------------------------
    # MÉTODOS FUNCIONALES
    # ------------------------------------------------------------

    def marcar_destacado(self):
        """Marca el mensaje como destacado."""
        self.__destacado = True
        print("Mensaje marcado como destacado.")

    def quitar_destacado(self):
        """Desmarca el mensaje (deja de ser destacado)."""
        self.__destacado = False
        print("Mensaje quitado de destacados.")

    def adjuntar(self, tipo, nombre, ruta):
        """
        Agrega un nuevo archivo o enlace como adjunto.
        Parámetros:
            tipo : str  -> Tipo de adjunto (imagen, audio, documento, link, etc.)
            nombre : str -> Nombre del archivo o descripción
            ruta : str -> Dirección local o URL del adjunto
        """
        adjunto = {"tipo": tipo, "nombre": nombre, "ruta": ruta}
        self.__adjuntos.append(adjunto)
        print("Adjunto agregado correctamente: " + nombre)

    def buscar_adjunto(self, palabra_clave):
        """
        Busca adjuntos cuyo nombre contenga una palabra clave.
        Devuelve una lista con los adjuntos encontrados.
        """
        resultados = []
        for adj in self.__adjuntos:
            if palabra_clave.lower() in adj["nombre"].lower():
                resultados.append(adj)
        return resultados

    def mostrar_mensaje(self):
        """
        Devuelve una representación textual completa del mensaje.
        Incluye remitente, destinatarios, asunto, prioridad, destacado,
        contenido y adjuntos.
        """
        prioridad_txt = "URGENTE" if self.__prioridad else "Normal"
        destacado_txt = "Sí" if self.__destacado else "No"

        texto = "De: " + self.__remitente + "\n"
        texto += "Para: " + ", ".join(self.__destinatarios) + "\n"
        texto += "Asunto: " + self.__asunto + "\n"
        texto += "Prioridad: " + prioridad_txt + "\n"
        texto += "Destacado: " + destacado_txt + "\n\n"
        texto += self.__contenido + "\n"

        if len(self.__adjuntos) > 0:
            texto += "\nAdjuntos:\n"
            for adj in self.__adjuntos:
                texto += "- " + adj["tipo"] + ": " + adj["nombre"] + " (" + adj["ruta"] + ")\n"

        return texto


