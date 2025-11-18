
from ServidorCorreo import ServidorCorreo
from Usuario import Usuario


def mostrar_menu():
    print(" MENÚ PRINCIPAL")
    print("1. Registrar nuevo usuario (solo administrador)")
    print("2. Iniciar sesión")
    print("3. Listar usuarios (solo administrador)")
    print("4. Enviar mensaje individual")
    print("5. Enviar mensaje a un departamento (solo jefes, gerentes o administradores)")
    print("6. Crear regla de filtro")
    print("7. Aplicar filtros automáticos")
    print("8. Procesar mensajes prioritarios")
    print("9. Salir")


def main():
    servidor = ServidorCorreo()
    print("Servidor de correo activo")

    usuario_actual = None
    opcion = ""

    while opcion != "9":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # 1) Registrar usuario
        if opcion == "1":
            if usuario_actual is None or usuario_actual.get_rol().lower() != "administrador":
                print("Solo un administrador puede registrar nuevos usuarios.")
                continue

            nombre = input("Nombre: ")
            dni = input("DNI: ")
            mail = input("Correo electrónico: ")
            celular = input("Celular (10 dígitos): ")
            departamento = input("Departamento: ")
            rol = input("Rol: ")
            respuesta = input("Respuesta a la pregunta de seguridad: ")

            nuevo = Usuario(nombre, dni, mail, celular, departamento, rol, respuesta)
            servidor.registrar_usuario(nuevo)

        # 2) Login
        elif opcion == "2":
            mail = input("Correo electrónico: ")
            password = input("Contraseña: ")

            usuario = servidor.login(mail, password)
            if usuario is not None:
                usuario_actual = usuario
                print("Sesión iniciada correctamente.")
            else:
                print("No fue posible iniciar sesión.")

        # 3) Listar usuarios
        elif opcion == "3":
            if usuario_actual is None or usuario_actual.get_rol().lower() != "administrador":
                print("Solo el administrador puede ver la lista de usuarios.")
                continue

            servidor.listar_usuarios()

        # 4) Enviar mensaje individual
        elif opcion == "4":
            if usuario_actual is None:
                print("Debe iniciar sesión.")
                continue

            destinatario = input("Correo del destinatario: ")
            asunto = input("Asunto: ")
            contenido = input("Contenido: ")

            servidor.enviar_mensaje_global(usuario_actual.get_mail(), destinatario, asunto, contenido)

        # 5) Enviar mensaje a un departamento
        elif opcion == "5":
            if usuario_actual is None:
                print("Iniciar sesión.")
                continue

            rol = usuario_actual.get_rol().lower()
            if rol not in ["administrador", "jefe", "gerente"]:
                print("No tiene permisos para enviar al departamento.")
                continue

            departamento = input("Departamento destino: ")
            asunto = input("Asunto: ")
            contenido = input("Mensaje: ")

            servidor.enviar_a_departamento(usuario_actual.get_mail(), departamento, asunto, contenido)

        # 6) Crear regla de filtro
        elif opcion == "6":
            if usuario_actual is None:
                print("Iniciar sesión.")
                continue

            tipo = input("Tipo de filtro (asunto/remitente): ").lower()
            palabra = input("Palabra clave: ")
            carpeta = input("Carpeta destino: ")

            usuario_actual.agregar_regla_filtro(tipo, palabra, carpeta)

        # 7) Aplicar filtros
        elif opcion == "7":
            if usuario_actual is None:
                print("Iniciar sesión.")
                continue

            usuario_actual.aplicar_filtros()

        # 8) Procesar mensajes prioritarios
        elif opcion == "8":
            if usuario_actual is None:
                print("Iniciar sesión.")
                continue

            servidor.procesar_mensajes_prioritarios()

        # 9) Salir
        elif opcion == "9":
            print("El correo se esta cerrando...")

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
