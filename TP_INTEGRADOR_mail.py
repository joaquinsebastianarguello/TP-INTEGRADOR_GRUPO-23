class ServidorCorreo:
    def __init__(self, usuarios):
        self.usuarios=[] #Creamos una lista vacía para guardar los usuarios


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
        self.nombre = nombre #Creamos un espacio para los datos que van a ir guardados adentro de la clase usuario
        self.dni = dni
        self.mail= mail
        self._contraseña = contraseña #A contraseña la creamos con un guión bajo para que sea privada
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
    def __init__(self, nombre, mensajes, ListaDeMensajes): #Acá vamos a almacenar los mensajes, y crear o eliminar nuevos
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
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.tipo = tipo
        self.adjuntar = adjuntar
        self.estado = estado
   
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
