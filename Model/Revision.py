class Revision:
    IdRevision = 0
    TextoRevision = "a"
    Puntuacion = 0
    IdUsuario = 0
    IdPlato = 0
     
    def __init__(self, idUsuario, puntuacion, textoRevision):
        self.IdUsuario = idUsuario
        self.Puntuacion = puntuacion
        self.TextoRevision = textoRevision