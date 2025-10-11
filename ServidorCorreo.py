
from usuario import Usuario
from mensaje import Mensaje

class ServidorCorreo:                       # Servidor , administra usuarios, entrada al mail, coordina envios y administra mensajes
    def __init__(self):                     # inicia con lista vacia
        self.__usuarios = []                # Lista privada de objetos Usuario
        self.__nombre = "Servidor de Correo Central"

    # MÉTODOS GETTERS

    def get_usuarios(self):                  # devuelve lisat de usuarios en el servidor
        return self.__usuarios

    def get_nombre(self):                    # devuelve el nombre del servidor
        return self.__nombre                 # no se usan setters porque son atributos que no neecsitan cambios

    # MÉTODOS PRINCIPALES

    def registrar_usuario(self, usuario):           # Registra un nuevo usuario, chequea que no exista antes
        for u in self.__usuarios:
            if u.get_mail() == usuario.get_mail():
                print("Ya existe un usuario registrado con ese correo.")
                return
        self.__usuarios.append(usuario)
        print("Usuario registrado correctamente: " + usuario.get_mail())

    def buscar_usuario_por_mail(self, mail):               # busca usuario a partir de su mail
        for u in self.__usuarios:
            if u.get_mail() == mail:
                return u
        return None

    def listar_usuarios(self):
        print("Usuarios registrados en el " + self.__nombre + ":")
        for u in self.__usuarios:
            print("- " + u.get_nombre() + " (" + u.get_mail() + ")")

    def login(self, mail, contraseña):                      #Permite que el usuario inicie sesion
        usuario = self.buscar_usuario_por_mail(mail)
        if usuario is None:
            print("No existe ningún usuario con ese correo.")
            return None

        if usuario.login(mail, contraseña):
            print("Inicio de sesión exitoso para " + usuario.get_nombre())
            return usuario
        else:
            print("Error en el inicio de sesión.")
            return None

    def enviar_mensaje_global(self, remitente_mail:str, destinatario_mail:str, asunto:str, contenido:str, prioridad=False:bool):
        remitente = self.buscar_usuario_por_mail(remitente_mail)            # usamos la funcion de busqueda recursiva para enviar mensaje a todos los usuarios.
        destinatario = self.buscar_usuario_por_mail(destinatario_mail)

        if remitente is None:
            print("No se encontró el remitente en el servidor.")
            return
        if destinatario is None:
            print("No se encontró el destinatario en el servidor.")
            return
          
        mensaje = Mensaje(remitente_mail, destinatario_mail, asunto, contenido, prioridad)          # Crear y enviar mensaje 
        remitente.get_enviados().agregar_mensaje(mensaje)
        destinatario.get_inbox().agregar_mensaje(mensaje)
        print("Mensaje enviado correctamente de " + remitente_mail + " a " + destinatario_mail + ".")

    def buscar_usuarios_por_departamento(self, departamento):             # lista de usuarios de un departamento específico
  
        encontrados = []
        for u in self.__usuarios:
            if u.get_departamento().lower() == departamento.lower():
                encontrados.append(u)
        return encontrados

    def enviar_a_departamento(self, remitente_mail:str, departamento:str, asunto:str, contenido:str):
        remitente = self.buscar_usuario_por_mail(remitente_mail)
        if remitente is None:
            print("Remitente no encontrado.")
            return

        destinatarios = self.buscar_usuarios_por_departamento(departamento)
        if len(destinatarios) == 0:
            print("No hay usuarios en el departamento especificado.")
            return

        for usuario in destinatarios:
            mensaje = Mensaje(remitente_mail, usuario.get_mail(), asunto, contenido)
            remitente.get_enviados().agregar_mensaje(mensaje)
            usuario.get_inbox().agregar_mensaje(mensaje)

        print("Mensaje enviado a todo el departamento: " + departamento)

