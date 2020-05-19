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