
from Interfaz import InterfazCorreo
from Carpeta import Carpeta
from Mensajes import Mensaje
from Estructuras import Pila


class Usuario(InterfazCorreo):

    def __init__(self, nombre, dni, mail, celular, departamento, rol, respuesta_seguridad):
        # DATOS PRIVADOS
        self.__nombre = nombre
        self.__dni = dni
        self.__mail = mail
        self.__celular = celular
        self.__departamento = departamento
        self.__rol = rol

        # CONTRASEÑA INICIAL
        self.__password = "1234"
        self.__primer_login = True

        # PREGUNTA Y RESPUESTA DE SEGURIDAD
        self.__pregunta_seguridad = "Nombre de tu profesor favorito"
        self.__respuesta_seguridad = respuesta_seguridad.lower()

        # ESTRUCTURA DE CARPETAS
        self.__root = Carpeta("Root")
        self.__inbox = Carpeta("Bandeja de Entrada")
        self.__enviados = Carpeta("Enviados")

        self.__root.agregar_subcarpeta(self.__inbox)
        self.__root.agregar_subcarpeta(self.__enviados)

        # PAPELERA (PILA)
        self.__papelera = Pila()
    
    # GETTERS

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

    # SETTERS

    def set_mail(self, nuevo_mail):
        if "@" in nuevo_mail and "." in nuevo_mail:
            self.__mail = nuevo_mail
        else:
            print("Formato de correo inválido.")

    def set_password(self, nueva_pass):
        if len(nueva_pass) >= 4:
            self.__password = nueva_pass
        else:
            print("La contraseña debe tener al menos 4 caracteres.")

    def set_celular(self, nuevo_cel):
        if nuevo_cel.isdigit() and len(nuevo_cel) == 10:
            self.__celular = nuevo_cel
        else:
            print("Número de celular inválido. Debe tener 10 digitos, solo números, sin el 0 y el 15 del codigo de área")

    def set_departamento(self, nuevo_dep):
        self.__departamento = nuevo_dep

    def set_rol(self, nuevo_rol):
        self.__rol = nuevo_rol

    # AUTENTICACIÓN

    def verificar_password(self, password_ingresada):
        return password_ingresada == self.__password

    def es_primer_login(self):
        return self.__primer_login

    def confirmar_primer_login(self):
        self.__primer_login = False

    # RECUPERACIÓN DE CONTRASEÑA

    def verificar_respuesta_seguridad(self, respuesta):
        return respuesta.lower() == self.__respuesta_seguridad

    # MÉTODOS DE MENSAJERÍA (INTERFAZ)

    def enviar_mensaje(self, destinatario, asunto, contenido, prioridad=False):
        mensaje = Mensaje(self.__mail, destinatario.get_mail(), asunto, contenido, prioridad)
        self.__enviados.agregar_mensaje(mensaje)
        destinatario.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        self.__inbox.agregar_mensaje(mensaje)

    def listar_mensaje(self):
        self.__root.listar_contenido()

    # GESTIÓN DE MENSAJES

    def eliminar_mensaje(self, mensaje):
        self.__papelera.apilar(mensaje)

    def recuperar_de_papelera(self):
        if not self.__papelera.esta_vacia():
            return self.__papelera.desapilar()
        return None
