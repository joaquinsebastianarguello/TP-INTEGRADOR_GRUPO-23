git branch Usuario.py
git branch Mensaje.py
git branch Carpetas.py
git branch ServidorCorreo.py
git branch Documentos/



class ServidorCorreo:
    def __init__(self): #poner usuarios rompia el codigo.
        self._usuarios=[] #Creamos una lista vacía para guardar los usuarios


    def listaDeUsuarios(self):
        for i in self._usuarios:
            print(i._nombre) #i la variable que permite reocrrer la funcion, y conecta con self.usuarios[]


    def CrearUsuarios (self, nombre, dni, mail, contraseña, departamento, rol):
        usuario = Usuario (nombre, dni, mail, contraseña, departamento, rol)
        self._usuarios.append(usuario) #se añade el usuario a la lista, y "usuario" almacena a "Usuario"
        print(f'se añadio el usuario {usuario} : {nombre} - {mail}') #verificacion de que se añadio al usuario


    def ListarEmpleados(self): #se buscan los usuuarios en [], y se extrae su mail, nombre y rol
        for i in self._usuarios:
            print (f'{i.nombre} , {i.mail}, {i.rol}') 


    def EliminarEmpleado(self, contraseña):
        for i in self._usuarios:
            if i._contraseña == contraseña: #no iba i, iba contraseña para que funcione.
                self._usuarios.remove(i)
                print (f'usuario {i.usuario} eliminado!') #se compara la contraseña del usuario con la variable i, y se elimina de la lista

    def ModificarEmpleado(self, contraseña):
        print() #ni idea :/
       
#-----------------------------------------------------------------------

class Usuario:
    def __init__ (self, nombre, dni, mail, contraseña, departamento, rol):
        self._nombre = nombre #Creamos un espacio para los datos que van a ir guardados adentro de la clase usuario
        self._dni = dni
        self._mail= mail
        self._contraseña = contraseña #A contraseña la creamos con un guión bajo para que sea privada
        self._departamento = departamento
        self._rol = rol
        #quite carpeta, al crear el usuario no la pide


    def Login (self, mail, contraseña): #variables mail y contraseña comparan datos, y retornan si es correcto o no.
        if self._mail == mail and self._contraseña == contraseña:
            print("login correcto!")
            return True
        else:
            print("login incorrecto!")
            return False


    def recuperarContraseña(self, mail, nombre, departamento): #se comparan las variablesa con self, igual que en login.
        if self._mail == mail and self._nombre == nombre and self._departamento ==departamento:
            return (f"la contraseña es {self._contraseña}")
        else:
            return ("incorrecto!")

#contraseña erronea era innecesaria...

def crearCarpeta():
    print()


def listarCarpeta():
     print()

    
def EliminarCarpeta():
    print()

#-----------------------------------------------------------------------------------------

class Carpeta:
    def __init__(self, nombre, mensajes): #Acá vamos a almacenar los mensajes, y crear o eliminar nuevos
        self._nombre = nombre
        self._mensajes = []
 #[] cumple la funcion de la funcion eliminada (listaMensajes)


    def BandejaDeEntrada(self):
        print()


    def CrearMensaje():
        print()


    def eliminarMensaje(self):
        print()

    def listarMensaje(self):
        for i in self._mensajes:
            print(i.asunto) # i funciona como variable para acceder a la lista de mensajes completa a futuro

    def Borradores():
        print()


    def destacados():
        print()


    def BuscarMensaje():
        print()

#----------------------------------------------------------------------------

class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo, tipo, adjuntar, destacado):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.cuerpo = cuerpo
        self.tipo = tipo
        self.adjuntar = adjuntar
        self.destacado = destacado

    def EscribirMensaje():
        print()
   
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
        print ("MENU PRINCIPAL")
        print ("1- CREAR USUARIO")
        print ("2- LISTAR USUARIOS")
        print ("3- SALIR DEL PROGRAMA")

        opcion = input ("ingrese una opcion: ")

        if opcion == "1":
            nombre = input ("nombre: ")
            dni = input ("dni: ")
            mail = input ("mail a utilizar: ")
            contraseña = input ("contraseña: ")
            departamento = input ("departamento: ")
            rol = input ("rol: ")
            servidor.CrearUsuarios(nombre, dni, mail, contraseña, departamento, rol)

        elif opcion == "2":
            servidor.listaDeUsuarios()

        elif opcion == "3":
            print ("adios!")
            break

        else:
            print ("opcion invalida, intente otra vez!")

menu()
