class Agenda:
  def __init__(self):
    self.lista_contactos = []

  def menu(self):
    print("""
        \tAgenda de contactos
    1.- Crear contacto.
    2.- Editar contacto.
    3.- Eliminar contacto.
    4.- Consultar contactos.
    5.- Salir.
    """)
    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
      self.crearContacto()
    elif opcion == 2:
      self.editarContacto()
    elif opcion == 3:
      self.eliminarContacto()
    elif opcion == 4:
      self.consultarContactos()
    elif opcion == 5:
      exit()
    else:
      print("Opción incorrecta. Vuelva a intentarlo.")
      self.menu()

  def crearContacto(self):
    nombre = input("\nNombre: ")
    apellido = input("Apellido: ")
    numero = input("Teléfono: ")
    lista_contacto = [nombre, apellido, numero]
    self.lista_contactos.append(lista_contacto)

    print("Contacto creado.")
    self.menu()
    
  def editarContacto(self):
    nombre_clave = input("\nDigite el nombre del contacto que desea editar: ")

    for contacto in self.lista_contactos:
      if nombre_clave in contacto:
        nombre = input("\nNombre: ")
        apellido = input("Apellido: ")
        numero = input("Teléfono: ")
        contacto[0] = nombre
        contacto[1] = apellido
        contacto[2] = numero
        
        print("Contacto editado.")

      else:
        print("Contacto no creado.")
        
    self.menu()
    
  def eliminarContacto(self):
    nombre_clave = input("\nDigite el nombre del contacto que desea eliminar: ")

    for contacto in self.lista_contactos:
      if nombre_clave in contacto:
        self.lista_contactos.remove(contacto)

        print("Contacto eliminado.")

      else:
        print("Contacto no creado.")
        
    self.menu()
    
  def consultarContactos(self):
    if self.lista_contactos:
      for contacto in range(0, len(self.lista_contactos)):
        print(f"\nContacto {contacto + 1}")
        print("Nombre: ", self.lista_contactos[contacto][0])
        print("Apellido: ", self.lista_contactos[contacto][1])
        print("Número: ", self.lista_contactos[contacto][2])

    else:
      print("No se han creado contactos.")
        
    self.menu()
    
if __name__ == "__main__":
  miAgenda = Agenda()
  miAgenda.menu()
