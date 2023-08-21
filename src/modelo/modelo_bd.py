from src.config.database import obtener_conexion

def insertar_web(id, url, estatus, metodos, fecha):
    conn = obtener_conexion()
    query = "INSERT INTO dispotivos VALUES('" + id + "', '" + url + "','" + estatus + "', '" + metodos + "', '" + fecha + "')"
    cur_conn = conn.cursor()
    valor = cur_conn.execute(query)
    conn.commit()
    cur_conn.close()
    return valor


def consultar_estatus(estatus):
    conn = obtener_conexion()
    query = "SELEC * FROM servicio WHERE estatus=" + estatus + ";"
    cur_conn = conn.cursor()
    valor = cur_conn.execute(query)
    lestatus = cur_conn.fetchall()
    cur_conn.close()
    conn.close()
    return lestatus

def acualizar_web(estatus):
    conn = obtener_conexion()
    query = "UPDATE dispotivos SET estatus='" + estatus + ";"
    cur_conn = conn.cursor()
    valor = cur_conn.execute(query)
    conn.commit()
    cur_conn.close()
    conn.close()
    return valor

