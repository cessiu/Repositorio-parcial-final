https://replit.com/join/ephchtjakt-cesar-tomastom2

def detectar_alexa(texto):
  palabras = texto.split()
  veces_alexa = palabras.count('Alexa')

  if veces_alexa > 1:
      return "¡Tranquilo, solo di mi nombre una vez!"
  else:
      return "¿Dime, cómo puedo ayudarte?"

# Ejemplo de uso
entrada_usuario = input("Introduce un texto: ")
respuesta = detectar_alexa(entrada_usuario)
print(respuesta)
