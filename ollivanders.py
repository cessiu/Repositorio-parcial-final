class TiendaVaritas:
  def __init__(self):
      self.clientes_totales = 0
      self.clientes_que_compraron = 0
      self.varitas_vendidas = {'Varita de Saúco': 0, 'Varita de Espino': 0, 'Varita de Sauce': 0, 'Varita de Acebo': 0}

  def registrar_cliente(self):
      respuesta = input("¿Entra un cliente? (si/no): ").lower()
      return respuesta == 'si'

  def procesar_compra(self):
      respuesta = input("¿Compró algo? (si/no): ").lower()
      return respuesta == 'si'

  def mostrar_opciones_varitas(self):
      print("Varita de Saúco [1], Varita de Espino [2], Varita de Sauce [3] y Varita de Acebo [4].")

  def comprar_varita(self):
      opcion = input("¿Qué varita compró? Elige 1, 2, 3 o 4: ")
      opciones_varitas = {'1': 'Varita de Saúco', '2': 'Varita de Espino', '3': 'Varita de Sauce', '4': 'Varita de Acebo'}
      varita_elegida = opciones_varitas.get(opcion)

      if varita_elegida:
          self.varitas_vendidas[varita_elegida] += 1
          print(f"Hoy se vendió 1 {varita_elegida}.")
      else:
          print("Opción de varita no válida.")

  def ejecutar_tiendav(self):
      while self.registrar_cliente():
          if self.procesar_compra():
              self.mostrar_opciones_varitas()
              self.comprar_varita()
              self.clientes_que_compraron += 1

          self.clientes_totales += 1

      print(f"Clientes totales: {self.clientes_totales}")
      print(f"Clientes que compraron: {self.clientes_que_compraron}")
      print(f"Clientes que no compraron: {self.clientes_totales - self.clientes_que_compraron}")
      print(f"Hoy se vendieron {self.varitas_vendidas['Varita de Saúco']} varitas de saúco, {self.varitas_vendidas['Varita de Espino']} varitas de espino, {self.varitas_vendidas['Varita de Sauce']} varitas de sauce y {self.varitas_vendidas['Varita de Acebo']} varitas de acebo.")
      print("¡Qué gran día para Ollivanders!")
