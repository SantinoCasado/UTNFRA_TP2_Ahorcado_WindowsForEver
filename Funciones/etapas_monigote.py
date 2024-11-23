def dibujar_monigote(intento_actual):
    etapa = [
        """
          -----
          |   |
              |
              |
              |
              |
        """,
        """
          -----
          |   |
          O   |
              |
              |
              |
        """,
        """
          -----
          |   |
          O   |
          |   |
          |   |
              |
              |
        """,
        """
          -----
          |   |
          O   |
         /|   |
          |   |
              |
        """,
        """
          -----
          |   |
          O   |
         /|\  |
          |   |
              |
        """,
        """
          -----
          |   |
          O   |
         /|\  |
          |   |
         /    |
              |
        """,
        """
          -----
          |   |
          O   |
         /|\  |
          |   |
         / \  |
              |
        """
    ]
    #Dependiendo en que intento este el jugador se imprimira un monigote en especifico
    print(etapa[intento_actual])