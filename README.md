# 🎃 Agente de Calaveritas

Generador conversacional de calaveritas literarias usando Strands Agents.

Este proyecto demuestra cómo construir agentes de IA de forma progresiva, desde un agente simple hasta uno con capacidades multimodales, usando el framework Strands Agents.

## 📚 Estructura del Demo

El proyecto está organizado en etapas progresivas:

### Etapa 0: Agente Simple

- Agente básico sin herramientas
- Request predefinido para demo rápida
- Concepto básico de agente

### Etapa 1: Agente Simple Conversacional

- Mismo agente básico pero con loop interactivo
- Permite múltiples preguntas
- Muestra conversación real

### Etapa 2: Agente con Contexto

- System prompt especializado en calaveritas
- Guía la conversación para recopilar información
- Genera calaveritas con estilo tradicional mexicano

### Etapa 3: Herramientas Personalizadas

- Tool para buscar información de mascotas guardadas
- Tool para guardar calaveritas en archivos
- Muestra el agent loop: el agente decide cuándo usar cada herramienta

### Etapa 4: Agente Multimodal con Visión

- Análisis de fotos de mascotas
- El agente "ve" y describe características visuales
- Genera calaveritas basadas en la imagen
- Demuestra capacidades multimodales de Claude

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
uv add strands-a tus credenciales
```

## 🎮 Uso

Ejecuta cada etapa en orden:

```bash
# Etapa 0: Simple (hardcoded)
uv run 0_agente_simple.py

# Etapa 1: Simple conversacional
uv run 1_agente_simple_conversacional.py

# Etapa 2: Con contexto
uv run 2_agente_contexto.py

# Etapa 3: Con herramientas
uv run 3_agente_con_herramientas.py

# Etapa 4: Multimodal (con visión)
uv run 4_agente_multimodal.py
```

## 💡 Conceptos Demostrados

- **Agent Loop**: Razonamiento y decisión de herramientas
- **Custom Tools**: Herramientas específicas del dominio
- **Multimodal AI**: Procesamiento de imágenes
- **Progressive Enhancement**: Evolución incremental

## 📖 Recursos

- [Strands Agents Docs](https://strandsagents.com)
- [Proyecto Original](https://github.com/anacunha/calaveritas)
- [Calaveritas Literarias](https://es.wikipedia.org/wiki/Calaverita)
