# Lista para almacenar los usuarios
usuarios = []

# Función para mostrar el menú
def mostrar_menu():
    print("\nSistema de Gestión de Usuarios")
    print("1. Agregar Usuario")
    print("2. Eliminar Usuario")
    print("3. Mostrar Usuarios")
    print("4. Buscar Usuario")
    print("5. Salir")

# Función para agregar un usuario
def agregar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    usuarios.append(nombre)
    print(f"Usuario {nombre} agregado con éxito.")

# Función para eliminar un usuario
def eliminar_usuario():
    nombre = input("Ingrese el nombre del usuario a eliminar: ")
    if nombre in usuarios:
        usuarios.remove(nombre)
        print(f"Usuario {nombre} eliminado con éxito.")
    else:
        print("Usuario no encontrado.")

# Función para mostrar todos los usuarios
def mostrar_usuarios():
    if usuarios:
        print("Lista de Usuarios:")
        for usuario in usuarios:
            print(f"- {usuario}")
    else:
        print("No hay usuarios registrados.")

# Función para buscar un usuario
def buscar_usuario():
    nombre = input("Ingrese el nombre del usuario a buscar: ")
    if nombre in usuarios:
        print(f"Usuario {nombre} encontrado.")
    else:
        print("Usuario no encontrado.")

# Función principal para ejecutar el sistema
def ejecutar_sistema():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            eliminar_usuario()
        elif opcion == '3':
            mostrar_usuarios()
        elif opcion == '4':
            buscar_usuario()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecutar el sistema
ejecutar_sistema()
