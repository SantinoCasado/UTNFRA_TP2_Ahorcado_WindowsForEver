🕹️ Juego del Ahorcado en Consola (Python)

🎯 Objetivo
Desarrollar el clásico juego del Ahorcado en modo texto utilizando Python. El jugador deberá adivinar una palabra antes de que se complete el monigote. Las palabras estarán almacenadas en un archivo JSON en español e inglés.

📁 Estructura del Proyecto
ahorcado/
├── data.json           # Palabras en español e inglés
├── scores.json         # Puntajes guardados
├── hangman.py          # Lógica principal del juego
├── utils/
│   ├── loader.py       # Carga de archivos JSON
│   ├── score_manager.py# Gestión de puntajes
│   └── display.py      # Representación del monigote y menú
└── README.md



🧰 Requisitos Técnicos

  🔧 Herramientas necesarias
    - Visual Studio Code
    - Python 3.10 o superior
    - Extensión de Python para VS Code
    - Terminal integrada o externa
    
  📦 Librerías utilizadas
    - json (incluida en la biblioteca estándar)
    - random (para selección aleatoria)

🚀 Cómo Ejecutar el Proyecto
  - Clona el repositorio o descarga los archivos.
  - Abre la carpeta en Visual Studio Code.
  - Asegúrate de tener Python instalado y configurado.
  - Ejecuta el archivo principal:
      python hangman.py
  - Sigue las instrucciones en consola para jugar.

🧠 Funcionalidades Clave
  - Selección de idioma (Español/Inglés)
  - Representación progresiva del monigote
  - Sistema de puntaje por letra y palabra completa
  - Guardado de puntajes en scores.json
  - Menú interactivo con opciones: Jugar, Puntajes, Salir
  - Visualización de los 5 mejores puntajes

🌟 Mejoras Opcionales
    - Animaciones de texto con time.sleep() y efectos ASCII
    - Mensajes personalizados para aciertos y errores
    - Colores en consola usando colorama (opcional)


📌 Ejemplo de Monigote en Texto
 +---+
 |   O
 |  /|\
 |  / \
 |
=========


📈 Ejemplo de Puntajes
[
  {"nombre": "Santino", "puntaje": 15},
  {"nombre": "Lucía", "puntaje": 12},
  {"nombre": "Tomás", "puntaje": 10}
]



💬 Créditos y Autoría
Desarrollado como ejercicio académico para practicar estructuras, validaciones y lógica de juego en Python. Ideal para reforzar el uso de archivos, funciones, y modularidad.

¿Querés que te ayude a escribir el código base modular por carpetas como lo hacés en tus proyectos? También puedo ayudarte a refactorizarlo con validaciones defensivas y separación por responsabilidades.
