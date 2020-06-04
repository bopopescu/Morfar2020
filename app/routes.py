import mysql.connector
import app.dbConfig as config
from flask import render_template
from app import app
from flask import jsonify
from flask import request

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Le damos la bienvenida a la demo Morfar2020', user=user)

@app.route('/revisiones', methods=['POST'])
def revisiones():
    IdPlato = request.form.get('IdPlato')
    if IdPlato == None:
        IdPlato = 'IS NOT NULL'
    else:
        IdPlato = '= %s' % IdPlato
    IdUsuario = request.form.get('IdUsuario')
    if IdUsuario == None:
        IdUsuario = 'IS NOT NULL'
    else:
         IdUsuario = '= %s' % IdUsuario
    Puntaje = request.form.get('Puntaje')
    if Puntaje == None:
        Puntaje = 'IS NOT NULL'
    else:
        Puntaje = '= %s' % Puntaje
    IdLugar = request.form.get('IdLugar')
    if IdLugar == None:
        IdLugar = 'IS NOT NULL'
    else:
        IdLugar = '= %s' % IdLugar
    mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    db=config.db,
    passwd=config.passwd
    )
    cursor = mydb.cursor()
    query = ("Select Usuarios.Nombre, Usuarios.Apellido, Platos.NombrePlato, Lugares.nombreLugar, Revisiones.Puntaje, Revisiones.TextoRevision from Revisiones inner join Usuarios  on Revisiones.IdUsuario = Usuarios.IdUsuario inner join Platos on Revisiones.IdPlato = Platos.IdPlato inner join Lugares on Platos.idLugar = Lugares.idLugar where Platos.IdPlato %s AND Usuarios.IdUsuario %s AND Revisiones.Puntaje %s AND Lugares.IdLugar %s" % (IdPlato, IdUsuario, Puntaje, IdLugar))
    cursor.execute(query)
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/revisiones/new', methods=['POST'])
def revisiones_new():
    mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    db=config.db,
    passwd=config.passwd
    )
    cursor = mydb.cursor()
    IdPlato = request.form.get('IdPlato')
    IdUsuario = request.form.get('IdUsuario')
    Puntaje = request.form.get('Puntaje')
    Comentario = request.form.get('Texto')
    sql = "INSERT INTO Revisiones (IdPlato, IdUsuario, Puntaje, TextoRevision) VALUES (%s, %s, %s, %s)"
    val = (IdPlato, IdUsuario, Puntaje, Comentario)
    if IdPlato == None:
        return 'All fields are requred.'
    if IdUsuario == None:
        return 'All fields are requred.'
    if Puntaje == None:
        return 'All fields are requred.'
    if Comentario == None:
        return 'All fields are requred.'
    cursor.execute(sql, val)
    mydb.commit()
    resultId = cursor.lastrowid
    return jsonify(resultId)

@app.route('/lugares', methods=["POST"])
def lugares():
    mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    db=config.db,
    passwd=config.passwd
    )
    cursor = mydb.cursor()
    IdLugar = request.form.get('IdLugar')
    query = ("SELECT Revisiones.Puntaje, Revisiones.TextoRevision, Platos.NombrePlato, Lugares.idLugar FROM Revisiones INNER JOIN Platos on Revisiones.IdPlato = Platos.IdPlato INNER JOIN Lugares on Platos.idLugar = Lugares.idLugar WHERE Platos.idLugar = %s" % IdLugar)
    cursor.execute(query)
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/platos', methods=["POST"])
def platos():
    mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    db=config.db,
    passwd=config.passwd
    )
    cursor = mydb.cursor()
    IdPlato = request.form.get('IdPlato')
    query = ("SELECT Platos.IdPlato, Lugares.nombreLugar, Revisiones.Puntaje, Revisiones.TextoRevision, Usuarios.IdUsuario, Usuarios.Apellido, Usuarios.Nombre FROM Revisiones INNER JOIN Platos on Revisiones.IdPlato = Platos.IdPlato INNER JOIN Lugares on Platos.idLugar = Lugares.idLugar INNER JOIN Usuarios on Revisiones.IdUsuario = Usuarios.IdUsuario WHERE Platos.Idplato = %s" % IdPlato)
    cursor.execute(query)
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/usuarios', methods=["POST"])
def usuarios():
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

