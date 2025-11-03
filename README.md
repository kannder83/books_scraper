# Books Scraper

Un web scraper eficiente para extraer información de libros del sitio [Books to Scrape](https://books.toscrape.com/).

## 🎯 Objetivo

Desarrollar un scraper robusto que extraiga información completa de libros implementando buenas prácticas de web scraping, usando las librerías `httpx` y `selectolax` para máximo rendimiento.

## 🚀 Instalación Rápida

```bash
uv init
uv add httpx selectolax
source .venv/bin/active
# python --version
# Python 3.13.3
```

## 📚 Documentación

### Parte 1: Análisis y Estrategia
📖 **[Documentación Completa del Proceso](docs/parte_01.md)**

Esta documentación incluye:
- Análisis detallado de la estrategia de scraping
- Justificación técnica de las librerías elegidas
- Diseño de estructuras de datos
- Algoritmo de navegación página por página
- Proceso de extracción de detalles por libro
- Consideraciones de rendimiento y memoria

## 🗂️ Estructura del Proyecto

```
books_scraper/
├── README.md              # Este archivo
├── docs/
│   └── parte_01.md        # Documentación detallada del proceso
├── scraper.py             # Script principal del scraper
├── models.py              # Estructuras de datos
└── pyproject.toml         # Configuración del proyecto
```

## 🌟 Características

- ⚡ **Alto Rendimiento**: Usa httpx y selectolax para máxima velocidad
- 🔄 **Navegación Automática**: Procesa todas las páginas automáticamente
- 💾 **Gestión de Memoria**: Optimizado para procesar grandes volúmenes
- 📊 **Datos Estructurados**: Modelos de datos con validación de tipos
- 🛡️ **Scraping Responsable**: Respeta rate limits y robots.txt

## 🎯 Datos Extraídos

Por cada libro se obtiene:
- Título y autor
- Precio y disponibilidad
- Calificación (estrellas)
- ISBN y categoría
- Descripción completa
- URL de imagen de portada

## 🔧 Branch: `parte_01`

Esta rama contiene la implementación inicial con documentación completa del proceso de análisis y diseño.

