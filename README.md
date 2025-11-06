# 🎃 Calaveritas Agent

Generador conversacional de calaveritas literarias usando Strands Agents.

Este proyecto demuestra cómo construir agentes de IA de forma progresiva, desde un agente simple hasta uno con capacidades multimodales, usando el framework Strands Agents.

## 🔧 Configuración

Strands Agents usa **Amazon Bedrock con Claude 4 Sonnet** como modelo por defecto. Necesitas credenciales de AWS para usar Amazon Bedrock.

### Opción 1: AWS CLI (Recomendado)

Si ya tienes AWS configurado:

```bash
aws configure
```

Strands automáticamente usará tus credenciales configuradas.

### Opción 2: Variables de Entorno

Alternativamente, puedes usar un archivo `.env`:

```bash
cp .env.example .env
# Edita .env con tus credenciales
```

## 🚀 Instalación

> **Nota:** Las siguientes instrucciones asumen que usas [`uv`](https://github.com/astral-sh/uv) como gestor de paquetes. Si usas `pip`, consulta la [documentación de Strands](https://strandsagents.com/latest/documentation/docs/user-guide/quickstart/).

```bash
# Iniciar proyecto
uv init calaveritas-agent
cd calaveritas-agent
```

```bash
# Agregar dependencia
uv add strands-agents
```

## 📚 Etapas del Demo

### Etapa 0: Agente Simple

Crea un agente básico con un request predefinido:

```python
from strands import Agent

# Crear agente con configuración default
agent = Agent()

# Request hardcoded para la demo
prompt = "¿Qué es una calaverita literaria?"

print(f"👩‍💻 Prompt: {prompt}\n")
print("🤖 Agente: ", end="", flush=True)

# Invocar el agente
agent(prompt)
```

### Etapa 1: Agente Simple Conversacional

Agrega un loop interactivo para múltiples preguntas:

```python
from strands import Agent

# Crear agente
agent = Agent()

# Loop de conversación
while True:
    user_input = input("\n\n👩‍💻 Tú: ")
    if user_input.lower() in ['salir', 'exit', 'quit']:
        print("\n¡Hasta luego! 👋")
        break

    print("🤖 Agente: ", end="", flush=True)
    agent(user_input)
```

### Etapa 2: Agente con Contexto

Agrega un system prompt especializado en calaveritas:

```python
from strands import Agent

# System prompt especializado
system_prompt = """Eres un experto en calaveritas literarias mexicanas, especializado en crear calaveritas para mascotas.

Las calaveritas son poemas humorísticos del Día de Muertos que:
- Usan rima y métrica tradicional
- Personifican a la muerte de forma amigable
- Incluyen humor y cariño
- Mencionan características únicas de la mascota

Tu especialidad es crear calaveritas SOLO para mascotas (perros, gatos, etc.).

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
    if user_input.lower() in ['salir', 'exit', 'quit']:
        print("\n¡Hasta luego! 👋")
        break

    print("🤖 Agente: ", end="", flush=True)
    agent(user_input)
```

### Etapa 3: Herramientas Personalizadas

Agrega tools para buscar información y guardar calaveritas:

```python
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

    carpeta = "calaveritas_generadas"
    os.makedirs(carpeta, exist_ok=True)

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

# System prompt con instrucciones para usar herramientas
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

# Crear agente con herramientas
agent = Agent(
    system_prompt=system_prompt,
    tools=[obtener_info_mascota, guardar_calaverita]
)

# Loop de conversación
while True:
    user_input = input("\n\n👩‍💻 Tú: ")
    if user_input.lower() in ['salir', 'exit', 'quit']:
        print("\n¡Hasta luego! 👋")
        break

    print("🤖 Agente: ", end="", flush=True)
    agent(user_input)
```

### Etapa 4: Agente Multimodal con Visión

Agrega capacidad de analizar imágenes de mascotas:

```python
from pathlib import Path
from strands import Agent
import re

def cargar_imagen(ruta: str) -> dict:
    """Carga una imagen desde el sistema de archivos."""
    ruta_path = Path(ruta)

    if not ruta_path.exists():
        raise FileNotFoundError(f"No se encontró la imagen en: {ruta}")

    with open(ruta_path, "rb") as f:
        imagen_bytes = f.read()

    extension = ruta_path.suffix.lower()
    formato_map = {".jpg": "jpeg", ".jpeg": "jpeg", ".png": "png", ".gif": "gif", ".webp": "webp"}
    formato = formato_map.get(extension, "jpeg")

    return {"image": {"format": formato, "source": {"bytes": imagen_bytes}}}

# System prompt para análisis de imágenes
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

# Crear agente
agent = Agent(system_prompt=system_prompt)

# Loop de conversación
while True:
    user_input = input("\n\n👩‍💻 Tú: ")
    if user_input.lower() in ['salir', 'exit', 'quit']:
        print("\n¡Hasta luego! 👋")
        break

    # Buscar rutas de imagen en el mensaje
    patron = r"[^\s]+\.(?:jpg|jpeg|png|gif|webp)"
    rutas_encontradas = re.findall(patron, user_input, re.IGNORECASE)

    if rutas_encontradas:
        try:
            imagen = cargar_imagen(rutas_encontradas[0])
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
```

## 💡 Conceptos Demostrados

- **Agent Loop**: Razonamiento y decisión de herramientas
- **System Prompts**: Especialización del comportamiento del agente
- **Custom Tools**: Herramientas específicas del dominio
- **Multimodal AI**: Procesamiento de imágenes
- **Progressive Enhancement**: Evolución incremental

## 📖 Recursos

- [Strands Agents Docs](https://strandsagents.com)
- [Calaveritas Literarias](https://es.wikipedia.org/wiki/Calaverita)
