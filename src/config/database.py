import mysql.connector


def obtener_conexion():
    conn = mysql.connector.connect(user='root',  password='Nathanesputoxd.123', host='localhost',
                                database='monitoreo',port=3306,
                          )

    if conn is not None:
        print("conexion exitosa")
    else:
        print("error al conectar a la base")
    return conn


if __name__ == '__main__':
    obtener_conexion()
