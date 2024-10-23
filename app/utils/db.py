from flask_mysqldb import MySQL

conexMysql = MySQL()

def init_app(app):
    conexMysql.init_app(app)