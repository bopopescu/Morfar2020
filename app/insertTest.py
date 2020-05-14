import mysql.connector
from flask import render_template
from app import app
from flask import jsonify
from flask import request


@app.route('/insertar/')
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

    IdPlato = request.args.get('plato')
    IdUsuario = request.args.get('user')
    Puntaje = request.args.get('puntaje')
    Comentario = request.args.get('comentario')

    sql = "INSERT INTO Revisiones (IdPlato, IdUsuario, Puntaje, TextoRevision) VALUES (%s, %s, %s, %s)"
    val = (IdPlato, IdUsuario, Puntaje, Comentario)
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "record inserted.")
    return render_template('success.html', title='Success', rows=cursor.rowcount)