import sqlite3

conn = sqlite3.connect("caja.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagos (
        id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
        id_alumno varchar(10) NOT NULL,
        monto REAL NOT NULL,
        concepto_pago TEXT NOT NULL
    )
'''
)

conn.commit()
conn.close()