"""
Etapa 0: Agente Simple (Hardcoded)
===================================
Demuestra un agente básico con un request predefinido
"""

from strands import Agent


def main():
    print("🎃 Agente Simple")
    print("=" * 50)
    print()

    # Crear agente con configuración default
    agent = Agent()

    # Request hardcoded para la demo
    prompt = "¿Qué es una calaverita literaria?"

    print(f"👩‍💻 Prompt: {prompt}\n")
    print("🤖 Agente: ", end="", flush=True)

    # Invocar el agente con el prompt
    # El agente procesa la pregunta y hace streaming de la respuesta
    agent(prompt)

    print("\n")


if __name__ == "__main__":
    main()
