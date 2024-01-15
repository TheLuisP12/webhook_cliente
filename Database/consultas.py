import sqlite3

def conexion():
    conn = sqlite3.connect("Database/caja.db")
    cursor = conn.cursor()
    return conn, cursor

def agregarPago(codigo: str, monto: int, concepto: str):
    conn, cursor = conexion()
    cursor.execute("INSERT INTO pagos (id_alumno, monto, concepto_pago) VALUES (?, ?, ?)", (codigo, monto, concepto))
    conn.commit()
    conn.close()

def llamarUltimoPago():
    conn, cursor = conexion()
    cursor.execute("SELECT * FROM pagos ORDER BY id_pago DESC LIMIT 1")
    filas = cursor.fetchall()
    conn.close()
    return filas
def llamarHistorialPagos():
    conn, cursor = conexion()
    cursor.execute("SELECT * FROM pagos ORDER BY id_pago DESC")
    filas = cursor.fetchall()
    conn.close()
    return filas


