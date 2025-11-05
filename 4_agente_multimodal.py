"""
Etapa 4: Agente Multimodal con Visión
======================================
Demuestra cómo el agente puede analizar fotos de mascotas
El agente "ve" la imagen y genera calaveritas basadas en características visuales
"""

from pathlib import Path

from strands import Agent, tool


def cargar_imagen(ruta: str) -> dict:
    """Carga una imagen desde el sistema de archivos.

    Args:
        ruta: Ruta completa al archivo de imagen
    """
    ruta_path = Path(ruta)

    if not ruta_path.exists():
        raise FileNotFoundError(f"No se encontró la imagen en: {ruta}")

    # Leer imagen como bytes
    with open(ruta_path, "rb") as f:
        imagen_bytes = f.read()

    # Determinar formato
    extension = ruta_path.suffix.lower()
    formato_map = {".jpg": "jpeg", ".jpeg": "jpeg", ".png": "png", ".gif": "gif", ".webp": "webp"}
    formato = formato_map.get(extension, "jpeg")

    # Retornar en formato Bedrock
    return {"image": {"format": formato, "source": {"bytes": imagen_bytes}}}


def main():
    print("🎃 Agente de Calaveritas - Multimodal")
    print("=" * 50)
    print("Escribe 'salir' para terminar\n")

    # System prompt especializado
    system_prompt = """Eres un experto en calaveritas literarias mexicanas, especializado en crear calaveritas para mascotas.

Las calaveritas son poemas humorísticos del Día de Muertos que:
- Usan rima y métrica tradicional
- Personifican a la muerte de forma amigable
- Incluyen humor y cariño
- Mencionan características únicas de la mascota

Tu especialidad es crear calaveritas SOLO para mascotas (perros, gatos, etc.).

Cuando recibas una imagen de una mascota:
1. Analiza la imagen cuidadosamente (raza, color, tamaño, expresión, entorno)
2. Pregunta el nombre de la mascota si no lo mencionaron
3. Genera una calaverita basada en lo que ves en la imagen

Sigue siempre el estilo tradicional mexicano."""

    # Crear agente con system prompt (sin herramientas)
    agent = Agent(system_prompt=system_prompt)

    # Loop de conversación
    while True:
        user_input = input("\n\n👩‍💻 Tú: ")
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("\n¡Hasta luego! 👋")
            break

        # Buscar rutas de imagen en el mensaje
        import re
        patron = r"[^\s]+\.(?:jpg|jpeg|png|gif|webp)"
        rutas_encontradas = re.findall(patron, user_input, re.IGNORECASE)

        if rutas_encontradas:
            try:
                # Cargar imagen
                imagen = cargar_imagen(rutas_encontradas[0])
                # Enviar imagen + texto al agente
                mensaje = [imagen, {"text": user_input}]
                print("🤖 Agente: ", end="", flush=True)
                agent(mensaje)
            except FileNotFoundError as e:
                print(f"❌ Error: {e}")
            except Exception as e:
                print(f"❌ Error al procesar la imagen: {e}")
        else:
            print("🤖 Agente: ", end="", flush=True)
            agent(user_input)


if __name__ == "__main__":
    main()
