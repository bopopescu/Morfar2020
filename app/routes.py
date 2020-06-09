import mysql.connector
import app.dbConfig as config
from app import app
from flask import jsonify
from flask import request

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
        return 'All fields are required.'
    if IdUsuario == None:
        return 'All fields are required.'
    if Puntaje == None:
        return 'All fields are required.'
    if Comentario == None:
        return 'All fields are required.'
    cursor.execute(sql, val)
    mydb.commit()
    resultId = cursor.lastrowid
    return jsonify(resultId)

@app.route('/lugares', methods=['POST'])
def lugares():
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
    query = ("Select * from Lugares where IdLugar %s" % (IdLugar))
    cursor.execute(query)
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/lugares/new', methods=['POST'])
def lugares_new():
    mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    db=config.db,
    passwd=config.passwd
    )
    cursor = mydb.cursor()
    nombreLugar = request.form.get('nombreLugar')
    sql = "INSERT INTO Lugares (nombreLugar) VALUES (%s)"
    val = (nombreLugar)
    if nombreLugar == None:
        return 'All fields are requred.'
    cursor.execute(sql, (val,))
    mydb.commit()
    resultId = cursor.lastrowid
    return jsonify(resultId)

@app.route('/platos', methods=["POST"])
def platos():
    mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    db=config.db,
    passwd=config.passwd
    )
    IdPlato = request.form.get('IdPlato')
    NombrePlato = request.form.get('NombrePlato')
    IdLugar = request.form.get('IdLugar')
    if IdPlato == None:
        IdPlato = "IS NOT NULL"
    else:
        IdPlato = "= %s" % IdPlato
    if NombrePlato == None:
       NombrePlato = 'IS NOT NULL'
    else:   
        NombrePlato = "LIKE %s%s%s" % ("'%",NombrePlato,"%'")
    if IdLugar == None:
        IdLugar = "IS NOT NULL"
    else:
        IdLugar = "= %s" % IdLugar
    cursor = mydb.cursor()
    query = ("SELECT * FROM Platos WHERE IdPlato %s AND NombrePlato %s AND IdLugar %s" % (IdPlato, NombrePlato, IdLugar))
    cursor.execute(query)
    rows = cursor.fetchall()
    return jsonify(rows)
    
@app.route('/platos/new', methods=['POST'])
def platos_new():
    mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    db=config.db,
    passwd=config.passwd
    )
    cursor = mydb.cursor()
    NombrePlato = request.form.get('NombrePlato')
    IdLugar = request.form.get('IdLugar')
    if NombrePlato == None:
        return 'All fields are required.'
    if IdLugar == None:
        return 'All fields are required.'
    sql = "INSERT INTO Platos (NombrePlato, IdLugar) VALUES (%s, %s)"
    val = (NombrePlato, IdLugar)
    cursor.execute(sql,val)
    mydb.commit()
    resultId = cursor.lastrowid
    return jsonify(resultId)

@app.route('/usuarios', methods=["POST"])
def usuarios():
    mydb = mysql.connector.connect(
        host=config.host,
        user=config.user,
        db=config.db,
        passwd=config.passwd
    )
    cursor = mydb.cursor()
    query = ("SELECT IdUsuario, Nombre, Apellido, Correo FROM Usuarios")
    if request.form.get('IdUsuario') != None:
        query = query  + (" WHERE IdUsuario = %s" % (request.form.get("IdUsuario")))
    if request.form.get('Correo') != None:  
        query = query  + (" WHERE Correo = %s" % (request.form.get("Correo")))
    cursor.execute(query)
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route('/usuarios/new', methods=['POST'])
def usuarios_new():
    mydb = mysql.connector.connect(
    host=config.host,
    user=config.user,
    db=config.db,
    passwd=config.passwd
    )
    cursor = mydb.cursor()
    NombreUsuario = request.form.get('NombreUsuario')
    ApellidoUsuario = request.form.get('ApellidoUsuario')
    CorreoUsuario = request.form.get('CorreoUsuario')
    if NombreUsuario == None:
        return 'All fields are required'
    if ApellidoUsuario == None:
        return 'All fields are required'
    if CorreoUsuario == None:
        return 'All fields are required'
    sql = "INSERT INTO Usuarios (Nombre, Apellido, Correo) VALUES (%s, %s, %s)"
    val = (NombreUsuario, ApellidoUsuario, CorreoUsuario)
    cursor.execute(sql,val)
    mydb.commit()
    resultId = cursor.lastrowid
    return jsonify(resultId)
    