import mysql.connector
from flask import render_template
from app import app
from flask import jsonify
from flask import request


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/reporte')
def reporte():
    mydb = mysql.connector.connect(
    host="35.209.8.46",
    user="abovemed_morfar",
    db="abovemed_morfar2020",
    get_warnings=True,
    connect_timeout=60000,
    passwd="Watermelon123!"
    )
    cursor = mydb.cursor()

    query = ("Select Usuarios.Nombre, Usuarios.Apellido, Platos.NombrePlato, Lugares.nombreLugar, Revisiones.Puntaje, Revisiones.TextoRevision from Revisiones inner join Usuarios  on Revisiones.IdUsuario = Usuarios.IdUsuario inner join Platos on Revisiones.IdPlato = Platos.IdPlato inner join Lugares on Platos.idLugar = Lugares.idLugar ORDER by Revisiones.Puntaje desc")

    cursor.execute(query)

    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/post')
def post():
    return render_template('form.html')

@app.route('/insertar/', methods=['POST'])
def insertar():
    mydb = mysql.connector.connect(
    host="35.209.8.46",
    user="abovemed_morfar",
    db="abovemed_morfar2020",
    get_warnings=True,
    connect_timeout=60000,
    passwd="Watermelon123!"
    )
    cursor = mydb.cursor()

    IdPlato = request.form.get('IdPlato')
    IdUsuario = request.form.get('IdUsuario')
    Puntaje = request.form.get('Puntaje')
    Comentario = request.form.get('Texto')

    sql = "INSERT INTO Revisiones (IdPlato, IdUsuario, Puntaje, TextoRevision) VALUES (%s, %s, %s, %s)"
    val = (IdPlato, IdUsuario, Puntaje, Comentario)
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "record inserted.")
    return render_template('success.html', title='Success', rows=cursor.rowcount)

@app.route('/buscarLugares')
def buscarLugares():
    return render_template('buscadorLugares.html')

@app.route('/resultadoLugares', methods=["POST"])
def resultadoLugares():
    mydb = mysql.connector.connect(
    host="35.209.8.46",
    user="abovemed_morfar",
    db="abovemed_morfar2020",
    get_warnings=True,
    connect_timeout=60000,
    passwd="Watermelon123!"
    )
    cursor = mydb.cursor()
    IdLugar = request.form.get('IdLugar')
    query = ("SELECT Revisiones.Puntaje, Revisiones.TextoRevision, Platos.NombrePlato, Lugares.idLugar FROM Revisiones INNER JOIN Platos on Revisiones.IdPlato = Platos.IdPlato INNER JOIN Lugares on Platos.idLugar = Lugares.idLugar WHERE Platos.idLugar = %s" % IdLugar)
    

    cursor.execute(query)

    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/buscarPlatos')
def buscarPlatos():
    return render_template('buscadorPlatos.html')

@app.route('/resultadoPlatos', methods=["POST"])
def resultadoPlatos():


    mydb = mysql.connector.connect(
    host="35.209.8.46",
    user="abovemed_morfar",
    db="abovemed_morfar2020",
    get_warnings=True,
    connect_timeout=60000,
    passwd="Watermelon123!"
    )
    cursor = mydb.cursor()
    IdPlato = request.form.get('IdPlato')
    query = ("SELECT Platos.IdPlato, Lugares.nombreLugar, Revisiones.Puntaje, Revisiones.TextoRevision, Usuarios.IdUsuario, Usuarios.Apellido, Usuarios.Nombre FROM Revisiones INNER JOIN Platos on Revisiones.IdPlato = Platos.IdPlato INNER JOIN Lugares on Platos.idLugar = Lugares.idLugar INNER JOIN Usuarios on Revisiones.IdUsuario = Usuarios.IdUsuario WHERE Platos.Idplato = %s" % IdPlato)
    

    cursor.execute(query)

    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/buscarUsuarios')
def buscarUsuarios():
    return render_template('buscadorUsuarios.html')

@app.route('/resultadoUsuarios', methods=["POST"])
def resultadoUsuarios():



    mydb = mysql.connector.connect(
    host="35.209.8.46",
    user="abovemed_morfar",
    db="abovemed_morfar2020",
    get_warnings=True,
    connect_timeout=60000,
    passwd="Watermelon123!"
    )
    cursor = mydb.cursor()
    IdUsuario = request.form.get('IdUsuario')
    query = ("SELECT Usuarios.Apellido, Usuarios.Nombre, Platos.NombrePlato, Lugares.nombreLugar, Revisiones.Puntaje, Revisiones.TextoRevision FROM Revisiones INNER JOIN Platos on Revisiones.IdPlato = Platos.IdPlato INNER JOIN Lugares on Platos.idLugar = Lugares.idLugar INNER JOIN Usuarios on Revisiones.IdUsuario = Usuarios.IdUsuario WHERE Usuarios.IdUsuario = %s" % IdUsuario)
    cursor.execute(query)
    rows = cursor.fetchall()
    return jsonify(rows) 