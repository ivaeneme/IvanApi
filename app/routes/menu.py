from flask import Blueprint, request, jsonify
from app.utils.db import conexMysql

bp = Blueprint('menu', __name__, url_prefix='/api')

@bp.route('/menu', methods=['GET'])
def obtener_menu():
    con = conexMysql()
    cursor = con.connection.cursor()
    query = "SELECT * FROM menu"
    cursor.execute(query)

    resultado = cursor.fetchall()

    menu_items = []
    for row in resultado:
        post = {
            'nombre': row[1],
            'precio': row[2],
            'ingredientes': row[3],

        }
        menu_items.append(post)

    # Cerrar el cursor
    cursor.close()

    # Devolver los resultados como JSON
    return jsonify(menu_items)

