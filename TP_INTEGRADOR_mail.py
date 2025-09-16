class ServidorCorreo:
    def __init__(self, usuarios):
        self.usuarios=[]


    def listaDeUsuarios():
        print()


    def CrearUsuarios (self, nombre, dni, mail, contraseña, departamento, rol):
        print() #placeholder


    def ListarEmpleados():
        print()


    def EliminarEmpleado(self, contraseña):
        print()


    def ModificarEmpleado(self, contraseña):
        print()
       
class Usuario:
    def __init__ (self, nombre, dni, mail, contraseña, departamento, rol, carpeta):
        self.nombre = nombre
        self.dni = dni
        self.mail= mail
        self._contraseña = contraseña
        self.departamento = departamento
        self.rol = rol
        self.carpeta = carpeta


    def Login (self, mail, contraseña):
        print()


    def recuperarContraseña(self, mail, nombre, departamento):
        print()


    def contraseñaErronea ():
        print()


    def listarCarpeta():
        print()


    def crearCarpeta():
        print()


    def EliminarCarpeta():
        print()


class Carpeta:
    def __init__(self, nombre, mensajes, ListaDeMensajes): #?????????
        print()


    def BandejaDeEntrada(self, listarMensaje):
        print()


    def CrearMensaje():
        print()


    def eliminarMensaje(self, listarMensaje):
        print()


    def Borradores():
        print()


    def destacados():
        print()


    def BuscarMensaje():
        print()


class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo, tipo, adjuntar, estado,):
        self.remitente = Usuario
        self.destinatario = Usuario
   
    def Enviar():
        print()


    def Descartar():
        print()


    def Adjuntar():
        print()


    def eliminarAdjuntado():
        print()


    def destacar():
        print()


    def QuitarDestacados():
        print()

#-----------------------------------------------------
def menu():
    servidor = ServidorCorreo()
    while True:
        print("MENU")
        print("1- crear usuario")
        print("2- listar usuarios")