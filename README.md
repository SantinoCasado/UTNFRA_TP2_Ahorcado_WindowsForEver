<body>

  <h1 class="emoji">🕹️ Juego del Ahorcado en Consola (Python)</h1>

  <h2 class="emoji">🎯 Objetivo</h2>
  <p>Desarrollar el clásico juego del Ahorcado en modo texto utilizando Python. El jugador deberá adivinar una palabra antes de que se complete el monigote. Las palabras estarán almacenadas en un archivo JSON en español e inglés.</p>

  <h2 class="emoji">📁 Estructura del Proyecto</h2>
  <pre>
ahorcado/
├── data.json           # Palabras en español e inglés
├── scores.json         # Puntajes guardados
├── hangman.py          # Lógica principal del juego
├── utils/
│   ├── loader.py       # Carga de archivos JSON
│   ├── score_manager.py# Gestión de puntajes
│   └── display.py      # Representación del monigote y menú
└── README.md
  </pre>

  <h2 class="emoji">🧰 Requisitos Técnicos</h2>
  <h3 class="emoji">🔧 Herramientas necesarias</h3>
  <ul>
    <li>Visual Studio Code</li>
    <li>Python 3.10 o superior</li>
    <li>Extensión de Python para VS Code</li>
    <li>Terminal integrada o externa</li>
  </ul>

  <h3 class="emoji">📦 Librerías utilizadas</h3>
  <ul>
    <li><code>json</code> (incluida en la biblioteca estándar)</li>
    <li><code>random</code> (para selección aleatoria)</li>
  </ul>

  <h2 class="emoji">🚀 Cómo Ejecutar el Proyecto</h2>
  <ul>
    <li>Clona el repositorio o descarga los archivos.</li>
    <li>Abre la carpeta en Visual Studio Code.</li>
    <li>Asegúrate de tener Python instalado y configurado.</li>
    <li>Ejecuta el archivo principal:</li>
  </ul>
  <pre>python hangman.py</pre>
  <p>Sigue las instrucciones en consola para jugar.</p>

  <h2 class="emoji">🧠 Funcionalidades Clave</h2>
  <ul>
    <li>Selección de idioma (Español/Inglés)</li>
    <li>Representación progresiva del monigote</li>
    <li>Sistema de puntaje por letra y palabra completa</li>
    <li>Guardado de puntajes en <code>scores.json</code></li>
    <li>Menú interactivo con opciones: Jugar, Puntajes, Salir</li>
    <li>Visualización de los 5 mejores puntajes</li>
  </ul>

  <h2 class="emoji">🌟 Mejoras Opcionales</h2>
  <ul>
    <li>Animaciones de texto con <code>time.sleep()</code> y efectos ASCII</li>
    <li>Mensajes personalizados para aciertos y errores</li>
    <li>Colores en consola usando <code>colorama</code> (opcional)</li>
  </ul>

  <h2 class="emoji">📌 Ejemplo de Monigote en Texto</h2>
  <pre>
 +---+
 |   O
 |  /|\
 |  / \
 |
=========
  </pre>

  <h2 class="emoji">📈 Ejemplo de Puntajes</h2>
  <pre>
[
  {"nombre": "Santino", "puntaje": 15},
  {"nombre": "Lucía", "puntaje": 12},
  {"nombre": "Tomás", "puntaje": 10}
]
  </pre>

  <h2 class="emoji">💬 Créditos y Autoría</h2>
  <p>Desarrollado como ejercicio académico para practicar estructuras, validaciones y lógica de juego en Python. Ideal para reforzar el uso de archivos, funciones, y modularidad.</p>

</body>
</html>
