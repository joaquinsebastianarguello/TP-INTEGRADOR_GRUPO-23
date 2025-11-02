
from ServidorCorreo import ServidorCorreo
from Usuario import Usuario


def mostrar_menu():
    """Muestra el menú principal con las opciones disponibles."""
    print(" MENÚ PRINCIPAL")
    print("1. Registrar nuevo usuario (solo administrador)")
    print("2. Iniciar sesión")
    print("3. Listar usuarios (solo administrador)")
    print("4. Enviar mensaje individual")
    print("5. Enviar mensaje a un departamento (solo jefes, gerentes o administradores)")
    print("6. Crear regla de filtro")
    print("7. Aplicar filtros automáticos")
    print("9. Salir")


def main():                                    # Crea el servidor y permite interactuar con el menú
    servidor = ServidorCorreo()
    print("Servidor de correo activo")

    admin = Usuario("Admin", "12345678", "admin@mail.com", "1234567890", "Sistemas", "administrador")
    servidor.registrar_usuario(admin)

    empleado = Usuario("limpiador", "34567890", "empleado@.com", "23456789", "limpieza", "barredor")
    servidor.registrar_usuario(empleado)
    
    usuario_actual = None

    usuario_actual = None                      # Guarda al usuario que inicia sesión
    opcion = ""

    while opcion != "9":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":                      # solo el admin puede registrar
            print(" Registro de nuevo usuario")                    
            if usuario_actual is None or usuario_actual.get_rol().lower() != "administrador":
                print("Solo un administrador puede registrar nuevos usuarios.")
                continue

            nombre = input("Nombre: ")
            dni = input("DNI: ")
            mail = input("Correo electrónico: ")
            telefono = input("Teléfono: ")
            departamento = input("Departamento: ")
            rol = input("Rol: ")

            nuevo_usuario = Usuario(nombre, dni, mail, telefono, departamento, rol)
            servidor.registrar_usuario(nuevo_usuario)

        elif opcion == "2":
            print("Inicio de sesión ")
            mail = input("Correo electrónico: ")
            contraseña = input("Contraseña: ")
            usuario_actual = servidor.login(mail, contraseña)

            if usuario_actual is not None:
                print("Sesión iniciada correctamente por: " + usuario_actual.get_nombre())
            else:
                print("Error al iniciar sesión.")

        elif opcion == "3":                            # Solo el administrador puede ver la lista de usuarios
            if usuario_actual is None or usuario_actual.get_rol().lower() != "administrador":
                print("Solo un administrador puede ver la lista de usuarios.")
                continue
            servidor.listar_usuarios()

        elif opcion == "4":
            if usuario_actual is None:
                print("Debe iniciar sesión para enviar mensajes.")
                continue

            print(" Envío de mensaje individual")
            destinatario = input("Correo del destinatario: ")
            asunto = input("Asunto: ")
            contenido = input("Contenido: ")

            servidor.enviar_mensaje_global(usuario_actual.get_mail(), destinatario, asunto, contenido)

        elif opcion == "5":
            if usuario_actual is None:
                print("Debe iniciar sesión para enviar mensajes.")
                continue

            rol = usuario_actual.get_rol().lower()                   # Solo jefes, gerentes o administradores pueden usar esta opción   
            if rol not in ["administrador", "jefe", "gerente"]:
                print("No tiene permisos para enviar mensajes a departamentos.")
                continue

            print("Envío de mensaje a un departamento")
            departamento = input("Departamento destino: ")
            asunto = input("Asunto: ")
            contenido = input("Contenido: ")

            servidor.enviar_a_departamento(usuario_actual.get_mail(), departamento, asunto, contenido)

        elif opcion == "6":
            if usuario_actual == None:
                print("Debe iniciar sesión para crear filtros.")
                return

            print("Nueva regla creada:")
            tipo = input("Filtrar por asunto/remitente: ").lower()
            valor = input("Ingrese palabra clave a buscar: ")
            carpeta = input("Nombre de la carpeta destino: ")

            usuario_actual.regla_filtro(tipo, valor, carpeta)

        elif opcion == "7":
            if usuario_actual == None:
                print("Debe iniciar sesión para aplicar filtros.")
                return

            print("Filtros aplicados.")
            usuario_actual.aplicar_filtros()
        
        elif opcion == "8":  # Nueva opción
            if usuario_actual is None:
                print("Debe iniciar sesión para enviar mensajes.")
                return
            destinatario = input("Correo del destinatario: ")
            asunto = input("Asunto: ")
            contenido = input("Contenido: ")
            servidor.enviar_mensaje_prioridad(usuario_actual.get_mail(), destinatario, asunto, contenido)

        elif opcion == "9":
            print("El correo se esta cerrando...")
        
        else:
            print("Opción no válida. Intente nuevamente.")

main()                    # EJECUCIÓN DIRECTA DEL PROGRAMA
