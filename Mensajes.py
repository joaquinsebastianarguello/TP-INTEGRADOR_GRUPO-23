
# CLASE MENSAJE

# Contiene datos del remitente, destinatario, asunto, contenido y prioridad del mensaje.


class Mensaje:

    def __init__(self, remitente:str, destinatario: str, asunto:str, contenido: str, prioridad=False:bol):
        
            prioridad : bool
                True si es urgente, False por defecto.
        """
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__contenido = contenido
        self.__prioridad = prioridad                         # True si es urgente, False por defecto 

    # MÉTODOS GETTERS (acceso a atributos privados)
  
    def get_remitente(self):                                 # Arroja el correo del remitente.
        return self.__remitente

    def get_destinatario(self):                              # Arroja el correo del destinatario
        return self.__destinatario

    def get_asunto(self):                                    # Arroja el asunto                
        return self.__asunto

    def get_contenido(self):
        return self.__contenido

    def get_prioridad(self):                                # True si es urgente
        return self.__prioridad

   
    # MÉTODOS
   
    def mostrar_mensaje(self):
        prioridad_txt = "URGENTE" if self.__prioridad else "Normal"
        texto = "De: " + self.__remitente + "\n"
        texto += "Para: " + self.__destinatario + "\n"
        texto += "Asunto: " + self.__asunto + "\n"
        texto += "Prioridad: " + prioridad_txt + "\n\n"
        texto += self.__contenido
        return texto

    def guardar_borrador(self, asunto, contenido):                     # guarda mensaje en carpeta borradores. Se usa cuando el mensaje aun no fue enviado
        mensaje = Mensaje(self.__mail, self.__mail, asunto, contenido)
        self.__borradores.agregar_mensaje(mensaje)
        print("Mensaje guardado como borrador.")

    def responder_mensaje(self, mensaje_original, contenido_respuesta):       #para responder mensajes recibidos, cambia destinatario y emisor 
      
        asunto_respuesta = "Re: " + mensaje_original.get_asunto()
        respuesta = Mensaje(self.__mail,
                            mensaje_original.get_remitente(),
                            asunto_respuesta,
                            contenido_respuesta)
        self.enviar_mensaje(self.buscar_usuario_por_mail(mensaje_original.get_remitente()),
                            asunto_respuesta,
                            contenido_respuesta)

    def reenviar_mensaje(self, mensaje_original, nuevo_destinatario):           #reenvia mensaje a otro destinatario cualquiera
        asunto_reenvio = "Fwd: " + mensaje_original.get_asunto()
        nuevo_mensaje = Mensaje(self.__mail,
                                nuevo_destinatario.get_mail(),
                                asunto_reenvio,
                                mensaje_original.get_contenido())
        self.enviar_mensaje(nuevo_destinatario,
                            asunto_reenvio,
                            mensaje_original.get_contenido())

   

