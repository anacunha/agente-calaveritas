"""
Etapa 2: Agente con Contexto
=============================
Demuestra cómo un system prompt especializado mejora el comportamiento del agente
El agente ahora sabe sobre calaveritas y guía la conversación
"""

from strands import Agent


def main():
    print("🎃 Agente de Calaveritas - Con Contexto")
    print("=" * 50)
    print("Escribe 'salir' para terminar")

    # System prompt especializado en calaveritas
    system_prompt = """Eres un experto en calaveritas literarias mexicanas.

Las calaveritas son poemas humorísticos del Día de Muertos que:
- Usan rima y métrica tradicional
- Personifican a la muerte de forma amigable
- Incluyen humor y cariño
- Mencionan características únicas de la persona/mascota

Cuando alguien te pida una calaverita:
1. Pregunta el nombre de la mascota
2. Pregunta características importantes (color, tamaño, personalidad, gustos)
3. Genera la calaverita usando esa información

Sigue siempre el estilo tradicional mexicano."""

    # Crear agente con system prompt
    agent = Agent(system_prompt=system_prompt)

    # Loop de conversación
    while True:
        user_input = input("\n\n👩‍💻 Tú: ")
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("\n¡Hasta luego! 👋")
            break

        print("🤖 Agente: ", end="", flush=True)

        # Invocar el agente con el input del usuario
        agent(user_input)


if __name__ == "__main__":
    main()
