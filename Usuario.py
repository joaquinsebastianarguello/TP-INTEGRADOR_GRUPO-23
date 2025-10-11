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

        self.__root = Carpeta("Root")                              # Estructura de correo. Arbol recursivo donde root es el nodo raiz del arbol carpeta, es recursiva porque cada carpeta puede tener otras carpetas dentro
        self.__inbox = Carpeta("Bandeja de Entrada")               # Es raiz del arbol carpeat, porque el nodo raiz del arbol principal es el mismo servidor de correo
        self.__enviados = Carpeta("Enviados")                      # Se inicia aca un mini arbol en cada usuario
        self.__root.agregar_subcarpeta(self.__inbox)
        self.__root.agregar_subcarpeta(self.__enviados)
        self.__papelera = Pila()

    # METODOS GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def get_mail(self):
        return self.__mail

    def get_telefono(self):
        return self.__telefono

    def get_departamento(self):
        return self.__departamento

    def get_rol(self):
        return self.__rol

   
    # MÉTODOS SETTERS 
  
    def set_mail(self, nuevo_mail):                                # para hacer esto verifico que el mail tenga el @ y el . por el dominio
        if "@" in nuevo_mail and "." in nuevo_mail:
            self.__mail = nuevo_mail
            print("Correo actualizado correctamente.")
        else:
            print("Formato de correo inválido.")

    def set_contraseña(self, nueva_contraseña):                    # como al principio establecimos una contraseña de 4 digitos, mantenemos esa decisión en al recuepracion, aunque este límite nonera necesario
        if len(nueva_contraseña) >= 4:
            self.__contraseña = nueva_contraseña
            print("Contraseña modificada correctamente.")
        else:
            print("La contraseña debe tener al menos 4 caracteres.")   # si no cumple la cant de caracteres tira error. Tambien se podria limitar el tipo de valor que recibe, o trasnformarla en minuscula para que no importe si estuviera escrita en mayuscula o minuscula

    def set_rol(self, nuevo_rol):                                   # lo pensamos desde el punto que un empleado puede cambiar su jerarquia dentro de al empresa
        self.__rol = nuevo_rol
        print("Rol actualizado a: " + nuevo_rol)

    def set_departamento(self, nuevo_dep):                          # lo mismo que para rol
        self.__departamento = nuevo_dep
        print("Departamento actualizado correctamente.")

    def set_telefono(self, nuevo_tel):                              # modificacion de numero de contacto telefonico
        if nuevo_tel.isdigit() and len(nuevo_tel) >= 8:             # son 8 valores porque lo consideramos sin el 11, o el 15
            self.__telefono = nuevo_tel                             #deben ser números
            print("Teléfono actualizado correctamente.")
        else:
            print("Número telefónico inválido.")

# hay valores que no necesitan el set como por ejemplo el dni o el nombre, aunque poria cambiar en caso de identidad de genero o modificacion legal
    
    def login(self, mail, contraseña):                             # Autenticacion de contraseña, si es primer ingreso, pide cambio de pass
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
        else:                                                                # Si la pass no es correcta, envia a recuperar
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

    def cambiar_contraseña(self, nueva):                                   # Cambio de contraseña
        self.__contraseña = nueva

    def generar_codigo_validacion(self):                                   #genera codigo temporal de recuperación, aleatorio, gracias a random, de 6 digitos, los cuales van a estar entre 000000 y 999999. Envia a mail o tel.
        self.__codigo_validacion = str(random.randint(100000, 999999))
        print("Código enviado al teléfono " + self.__telefono + " o al correo " + self.__mail)
        
    def recuperar_contraseña(self):
        self.generar_codigo_validacion()                                    # simula validacion
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

    def get_mail(self):                                               # metodo de correo (interfazCorreo)
        return self.__mail                                            # define métodos heredados

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

