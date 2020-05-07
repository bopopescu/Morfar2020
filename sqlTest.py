import mysql.connector

mydb = mysql.connector.connect(
  host="35.209.8.46",
  user="abovemed_morfar",
  db="abovemed_morfar2020",
  get_warnings=True,
  connect_timeout=60000,
  passwd="Watermelon123!"
)

cursor = mydb.cursor()

query = ("Select Usuarios.Nombre, Usuarios.Apellido, Platos.NombrePlato, Lugares.nombreLugar, Revisiones.Puntaje from Revisiones inner join Usuarios  on Revisiones.IdUsuario = Usuarios.IdUsuario inner join Platos on Revisiones.IdPlato = Platos.IdPlato inner join Lugares on Platos.idLugar = Lugares.idLugar ORDER by Revisiones.Puntaje desc")

cursor.execute(query)

rows = cursor.fetchall()
for row in rows:
    for col in row:
        print("%s" % col)
    print("\n")