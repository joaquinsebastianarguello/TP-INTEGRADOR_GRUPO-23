
from Usuario import Usuario
from Mensajes import Mensaje
from collections import deque


class ServidorCorreo:

    def __init__(self, nombre="Servidor de Correo Central"):
        self.__nombre = nombre
        self.__usuarios = []
        self.__vecinos = []          # Servidores conectados (grafo)

    # GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_usuarios(self):
        return self.__usuarios

    def get_vecinos(self):
        return self.__vecinos

    # REGISTRO DE USUARIOS
    def registrar_usuario(self, usuario):
        for u in self.__usuarios:
            if u.get_mail() == usuario.get_mail():
                print("Ya existe un usuario registrado con ese correo.")
                return
        self.__usuarios.append(usuario)
        print("Usuario registrado correctamente: " + usuario.get_mail())

    def buscar_usuario_por_mail(self, mail):
        for u in self.__usuarios:
            if u.get_mail() == mail:
                return u
        return None

    def listar_usuarios(self):
        print("Usuarios registrados en el " + self.__nombre + ":")
        for u in self.__usuarios:
            print("- " + u.get_nombre() + " (" + u.get_mail() + ")")

    # LOGIN
    def login(self, mail, contraseña):
        usuario = self.buscar_usuario_por_mail(mail)
        if usuario is None:
            print("No existe ningún usuario con ese correo.")
            return None

        if usuario.verificar_password(contraseña):
            if usuario.es_primer_login():
                nueva = input("Primer inicio detectado. Ingrese nueva contraseña: ")
                usuario.set_password(nueva)
                usuario.confirmar_primer_login()
            print("Inicio de sesión exitoso para " + usuario.get_nombre())
            return usuario

        print("Contraseña incorrecta.")
        return None

    # ENVÍO LOCAL
    def enviar_mensaje_global(self, remitente_mail, destinatario_mail, asunto, contenido, prioridad=False):
        remitente = self.buscar_usuario_por_mail(remitente_mail)
        destinatario = self.buscar_usuario_por_mail(destinatario_mail)

        if remitente is None:
            print("No se encontró el remitente en el servidor.")
            return
        if destinatario is None:
            print("No se encontró el destinatario en el servidor.")
            return

        mensaje = Mensaje(remitente_mail, destinatario_mail, asunto, contenido, prioridad)
        remitente.get_enviados().agregar_mensaje(mensaje)
        destinatario.recibir_mensaje(mensaje)
        print("Mensaje enviado correctamente de " + remitente_mail + " a " + destinatario_mail + ".")

    # FILTRO POR DEPARTAMENTO
    def buscar_usuarios_por_departamento(self, departamento):
        encontrados = []
        for u in self.__usuarios:
            if u.get_departamento().lower() == departamento.lower():
                encontrados.append(u)
        return encontrados

    def enviar_a_departamento(self, remitente_mail, departamento, asunto, contenido):
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
            usuario.recibir_mensaje(mensaje)

        print("Mensaje enviado a todo el departamento: " + departamento)

   
    #   MODELO DE RED (GRAFO)

    def agregar_conexion(self, servidor_vecino):
        if servidor_vecino not in self.__vecinos:
            self.__vecinos.append(servidor_vecino)
            servidor_vecino.__vecinos.append(self)

    def bfs_ruta(self, servidor_destino):
        visitados = set()
        cola = deque([(self, [])])

        while cola:
            actual, ruta = cola.popleft()
            if actual == servidor_destino:
                return ruta + [actual]

            if actual not in visitados:
                visitados.add(actual)
                for vecino in actual.get_vecinos():
                    cola.append((vecino, ruta + [actual]))
        return None

    def enviar_mensaje_red(self, remitente_mail, destinatario_mail, asunto, contenido, prioridad=False):
        remitente = self.buscar_usuario_por_mail(remitente_mail)

        destino = None
        for servidor in self.__vecinos + [self]:
            candidato = servidor.buscar_usuario_por_mail(destinatario_mail)
            if candidato:
                destino = servidor
                break

        if destino is None:
            print("No se encontró el destinatario en la red.")
            return

        ruta = self.bfs_ruta(destino)
        if ruta is None:
            print("No existe ruta entre los servidores.")
            return

        print("Ruta encontrada: " + " -> ".join(s.get_nombre() for s in ruta))

        destino_usuario = destino.buscar_usuario_por_mail(destinatario_mail)
        mensaje = Mensaje(remitente_mail, destinatario_mail, asunto, contenido, prioridad)
        remitente.get_enviados().agregar_mensaje(mensaje)
        destino_usuario.recibir_mensaje(mensaje)

        print("Mensaje enviado correctamente a través de la red.")


