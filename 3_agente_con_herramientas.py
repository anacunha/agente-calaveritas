"""
Etapa 3: Agente con Herramientas
=================================
Demuestra cómo las herramientas permiten al agente realizar acciones específicas
El agente puede buscar información de mascotas y guardar las calaveritas generadas
"""

from strands import Agent, tool


@tool
def obtener_info_mascota(nombre: str) -> str:
    """Busca información de una mascota guardada previamente.

    Args:
        nombre: El nombre de la mascota
    """
    mascotas = {
        "Chuby": "Perro pequeño, peludo, café y blanco, muy juguetón, le encanta ir a la playa",
        "Romina": "Beagle, orejas largas, ojos expresivos, comilona, ladrona y muy cariñosa",
        "Michi": "Gato naranja, dormilón, le gusta el sol",
    }
    info = mascotas.get(nombre)
    if info:
        return f"Encontré información sobre {nombre}: {info}"
    return f"No encontré información sobre {nombre}. ¿Puedes contarme sobre tu mascota?"


@tool
def guardar_calaverita(nombre_mascota: str, calaverita: str) -> str:
    """Guarda una calaverita en un archivo de texto.

    Args:
        nombre_mascota: El nombre de la mascota
        calaverita: El texto de la calaverita a guardar
    """
    import os

    # Crear carpeta si no existe
    carpeta = "calaveritas_generadas"
    os.makedirs(carpeta, exist_ok=True)

    # Crear ruta completa del archivo
    nombre_archivo = f"calaverita_{nombre_mascota.lower()}.txt"
    ruta_completa = os.path.join(carpeta, nombre_archivo)

    try:
        with open(ruta_completa, "w", encoding="utf-8") as f:
            f.write(f"Calaverita para {nombre_mascota}\n")
            f.write("=" * 40 + "\n\n")
            f.write(calaverita)

        return f"✅ Calaverita guardada exitosamente en: {ruta_completa}"
    except Exception as e:
        return f"❌ Error al guardar la calaverita: {str(e)}"


def main():
    print("🎃 Agente de Calaveritas - Con Herramientas")
    print("=" * 50)
    print("Escribe 'salir' para terminar")

    # System prompt especializado
    system_prompt = """Eres un experto en calaveritas literarias mexicanas, especializado en crear calaveritas para mascotas.

Las calaveritas son poemas humorísticos del Día de Muertos que:
- Usan rima y métrica tradicional
- Personifican a la muerte de forma amigable
- Incluyen humor y cariño
- Mencionan características únicas de la mascota

Tu especialidad es crear calaveritas SOLO para mascotas (perros, gatos, etc.).

Tienes acceso a herramientas para:
1. Buscar información de mascotas guardadas previamente
2. Guardar las calaveritas que generes

Cuando alguien te pida una calaverita:
1. Intenta buscar información de la mascota primero
2. Si no la encuentras, pregunta por las características
3. Genera la calaverita usando esa información
4. Ofrece guardar la calaverita en un archivo

Sigue siempre el estilo tradicional mexicano."""

    # Crear agente con system prompt y herramientas
    agent = Agent(system_prompt=system_prompt, tools=[obtener_info_mascota, guardar_calaverita])

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
