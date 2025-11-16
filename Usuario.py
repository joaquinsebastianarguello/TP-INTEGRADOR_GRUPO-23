
from Interfaz import InterfazCorreo
from Carpeta import Carpeta
from Mensajes import Mensaje
from Estructuras import Pila, ColaPrioridad


class Usuario(InterfazCorreo):

    def __init__(self, nombre, dni, mail, celular, departamento, rol, respuesta_seguridad):
        # DATOS PERSONALES
        self.__nombre = nombre
        self.__dni = dni
        self.__mail = mail
        self.__celular = celular
        self.__departamento = departamento
        self.__rol = rol

        # SEGURIDAD Y CONTRASEÑA
        self.__password = "1234"
        self.__primer_login = True
        self.__pregunta_seguridad = "Nombre de tu profesor favorito"
        self.__respuesta_seguridad = respuesta_seguridad.lower()

        # ESTRUCTURA DE CARPETAS
        self.__root = Carpeta("Root")
        self.__inbox = Carpeta("Bandeja de Entrada")
        self.__enviados = Carpeta("Enviados")

        self.__root.agregar_subcarpeta(self.__inbox)
        self.__root.agregar_subcarpeta(self.__enviados)

        # PAPELERA
        self.__papelera = Pila()

        # FILTROS (Entrega 3)
        # reglas = { "palabra" : Carpeta }
        self.__reglas_filtro = {}

        # PRIORIDAD (cola de prioridad)
        self.__cola_prioridad = ColaPrioridad()


    
    #          GETTERS
   

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def get_mail(self):
        return self.__mail

    def get_celular(self):
        return self.__celular

    def get_departamento(self):
        return self.__departamento

    def get_rol(self):
        return self.__rol

    def get_inbox(self):
        return self.__inbox

    def get_enviados(self):
        return self.__enviados

    def get_root(self):
        return self.__root


    #          SETTERS

    def set_mail(self, nuevo_mail):
        if "@" in nuevo_mail and "." in nuevo_mail:
            self.__mail = nuevo_mail

    def set_password(self, nueva_pass):
        if len(nueva_pass) >= 4:
            self.__password = nueva_pass

    def set_celular(self, nuevo_cel):
        if nuevo_cel.isdigit() and len(nuevo_cel) == 10:
            self.__celular = nuevo_cel

    def set_departamento(self, nuevo_dep):
        self.__departamento = nuevo_dep

    def set_rol(self, nuevo_rol):
        self.__rol = nuevo_rol


   
    #        AUTENTICACIÓN
    

    def verificar_password(self, pass_ingresada):
        return pass_ingresada == self.__password

    def es_primer_login(self):
        return self.__primer_login

    def confirmar_primer_login(self):
        self.__primer_login = False

   
    #   RECUPERACIÓN DE PASSWORD
    
    def verificar_respuesta_seguridad(self, respuesta):
        return respuesta.lower() == self.__respuesta_seguridad


   
    #  MÉTODOS DE MENSAJERÍA
    

    def enviar_mensaje(self, destinatario, asunto, contenido, prioridad=False):
        mensaje = Mensaje(self.__mail, destinatario.get_mail(), asunto, contenido, prioridad)
        self.__enviados.agregar_mensaje(mensaje)
        destinatario.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        # Si el mensaje es urgente → va a la cola de prioridad
        if mensaje.get_prioridad():
            self.__cola_prioridad.encolar(mensaje)

        # Aplicar filtros si coinciden
        self.aplicar_filtros(mensaje)

        # Siempre cae en inbox si no hay filtro específico
        self.__inbox.agregar_mensaje(mensaje)

    def listar_mensaje(self):
        self.__root.listar_contenido()


    #   GESTIÓN DE MENSAJES
   

    def eliminar_mensaje(self, mensaje):
        self.__papelera.apilar(mensaje)

    def recuperar_de_papelera(self):
        if not self.__papelera.esta_vacia():
            return self.__papelera.desapilar()
        return None


    
    #        FILTROS (Entrega 3)
   

    def agregar_regla_filtro(self, palabra, carpeta_destino):
        self.__reglas_filtro[palabra.lower()] = carpeta_destino

    def aplicar_filtros(self, mensaje):
        asunto = mensaje.get_asunto().lower()

        for palabra, carpeta_destino in self.__reglas_filtro.items():
            if palabra in asunto:
                carpeta_destino.agregar_mensaje(mensaje)
                return True

        return False

    #  MENSAJES PRIORITARIOS

    def procesar_mensajes_prioritarios(self):
        if self.__cola_prioridad.esta_vacia():
            return None
        return self.__cola_prioridad.desencolar()
