"""
Etapa 1: Agente Simple Conversacional
======================================
Demuestra un agente básico con loop interactivo
Permite múltiples preguntas en una conversación
"""

from strands import Agent

def main():
  print("🎃 Agente Simple Conversacional")
  print("=" * 50)
  print("Escribe 'salir' para terminar")

  # Crear agente con configuración default
  agent = Agent()

  # Loop de conversación
  while True:
    user_input = input("\n\n👩‍💻 Tú: ")
    if user_input.lower() in ['salir', 'exit', 'quit']:
      print("\n¡Hasta luego! 👋")
      break

    print("🤖 Agente: ", end="", flush=True)

    # Invocar el agente con el input del usuario
    # El agente procesa la pregunta y hace streaming de la respuesta
    agent(user_input)

if __name__ == "__main__":
  main()
