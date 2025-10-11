# CLASE USUARIO (con gestión de contraseñas)
# Incluye autenticación, cambio obligatorio de contraseña en el primer ingreso, y recuperación mediante código de validación.

from interfaz import InterfazCorreo
from carpeta import Carpeta
from mensaje import Mensaje
from estructuras import Pila
import random                                    # para crear los codigos de contraseñas aleatorios

class Usuario(InterfazCorreo):                   # Representa a un empleado con cuenta de correo y autenticación.
    def __init__(self, nombre, dni, mail, telefono, departamento, rol):  # Por defecto, la contraseña inicial es '1234' y debe cambiarse en el primer inicio de sesión.
        self.__nombre = nombre                   # Elementos privados
        self.__dni = dni
        self.__mail = mail
        self.__telefono = telefono
        self.__departamento = departamento
        self.__rol = rol
        self.__contraseña = "1234"
        self.__es_primer_login = True                              #la primera vez que ingresa debe cambiar la pass que se le dio por default, por lo tanto se neecsiat saber si es la primera vez que entra o no, para derivar en la accion necesaria
        self.__codigo_validacion = None                            #en caso de recuperacion de contraseña, se le enviara un codigo de validacion por mail o correo

        self.__root = Carpeta("Root")                              # Estructura de correo
        self.__inbox = Carpeta("Bandeja de Entrada")
        self.__enviados = Carpeta("Enviados")
        self.__root.agregar_subcarpeta(self.__inbox)
        self.__root.agregar_subcarpeta(self.__enviados)
        self.__papelera = Pila()

    # ------------------------------------------------------------
    # AUTENTICACIÓN Y GESTIÓN DE CONTRASEÑAS
    # ------------------------------------------------------------
    def login(self, mail, contraseña):
        """
        Verifica el ingreso del usuario.
        Si es el primer login, fuerza el cambio de contraseña.
        Si la contraseña no coincide, ofrece recuperación.
        """
        if mail != self.__mail:
            print("El correo ingresado no pertenece a este usuario.")
            return False

        if self.__contraseña == contraseña:
            if self.__es_primer_login:
                print("Primer inicio de sesión detectado.")
                nueva = input("Ingrese su nueva contraseña: ")
                self.cambiar_contraseña(nueva)
                print("Contraseña actualizada correctamente.")
                self.__es_primer_login = False
                return True
            else:
                print("Login correcto.")
                return True
        else:
            print("Contraseña incorrecta.")
            opcion = input("¿Desea intentar nuevamente (I) o recuperar contraseña (R)? ").upper()
            if opcion == "I":
                nueva_prueba = input("Reingrese su contraseña: ")
                return self.login(mail, nueva_prueba)
            elif opcion == "R":
                return self.recuperar_contraseña()
            else:
                print("Operación cancelada.")
                return False

    def cambiar_contraseña(self, nueva):
        """Permite cambiar la contraseña actual."""
        self.__contraseña = nueva

    def generar_codigo_validacion(self):
        """Genera un código numérico temporal para recuperación."""
        self.__codigo_validacion = str(random.randint(100000, 999999))
        print("Código enviado al teléfono " + self.__telefono + " o al correo " + self.__mail)
        print("(Simulación: el código es " + self.__codigo_validacion + ")")  # visible solo para pruebas

    def recuperar_contraseña(self):
        """
        Simula el proceso de recuperación mediante validación.
        Envía un código y permite definir una nueva contraseña.
        """
        self.generar_codigo_validacion()
        codigo_ingresado = input("Ingrese el código de validación recibido: ")
        if codigo_ingresado == self.__codigo_validacion:
            nueva = input("Ingrese su nueva contraseña: ")
            self.cambiar_contraseña(nueva)
            self.__codigo_validacion = None
            self.__es_primer_login = False
            print("Contraseña restablecida correctamente.")
            return True
        else:
            print("Código incorrecto. No se pudo recuperar la contraseña.")
            return False

    # ------------------------------------------------------------
    # MÉTODOS DE CORREO (InterfazCorreo)
    # ------------------------------------------------------------
    def get_mail(self):
        return self.__mail

    def enviar_mensaje(self, destinatario, asunto, contenido, prioridad=False):
        mensaje = Mensaje(self.__mail, destinatario.get_mail(), asunto, contenido, prioridad)
        self.__enviados.agregar_mensaje(mensaje)
        destinatario.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        self.__inbox.agregar_mensaje(mensaje)

    def listar_mensaje(self):
        self.__root.listar_contenido()

    def eliminar_mensaje(self, mensaje):
        self.__papelera.apilar(mensaje)
        print("Mensaje enviado a la papelera.")

