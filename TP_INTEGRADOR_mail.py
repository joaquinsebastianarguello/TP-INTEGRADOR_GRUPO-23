class ServidorCorreo:
    def __init__(self, usuarios):
        self.usuarios=[]


    def listaDeUsuarios(self):
        for i in self.usuarios:
            print(i.nombre) #i la variable que permite reocrrer la funcion, y conecta con self.usuarios[]


    def CrearUsuarios (self, nombre, dni, mail, contraseña, departamento, rol):
        usuario = Usuario (nombre, dni, mail, contraseña, departamento, rol)
        self.usuarios.append(usuario) #se añade el usuario a la lista, y "usuario" almacena a "Usuario"
        print(f'se añadio el usuario {usuario} : {nombre} - {mail}') #verificacion de que se añadio al usuario


    def ListarEmpleados(self): #se buscan los usuuarios en [], y se extrae su mail, nombre y rol
        for i in self.usuarios:
            print (f'{i.nombre} , {i.mail}, {i.rol}') 


    def EliminarEmpleado(self, contraseña):
        for i in self.usuarios:
            if i._contraseña == i:
                self.usuarios.remove(i)
                print (f'usuario {i.usuario} eliminado!') #se compara la contraseña del usuario con la variable i, y se elimina de la lista

    def ModificarEmpleado(self, contraseña):
        print() #ni idea :/
       
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