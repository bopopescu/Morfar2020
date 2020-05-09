class Usuario:
    IdUsuario = 0
    Nombre = "a"
    Apellido = "b"
    Correo = "a@a.com"
     
    def __init__(self, nombre, apellido, correo):
        self.Nombre = nombre
        self.Apellido = apellido
        self.Correo = correo