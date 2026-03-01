from datetime import datetime
import sqlite3
from database import get_conexion

def abrir_turno(empleado_id):
    conexion = get_conexion()
    cursor = conexion.cursor()

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO turnos (empleado_id, fecha_apertura, estado) VALUES (? ,? ,?)
    """, (empleado_id, ahora, 'abierto'))

    conexion.commit()
    conexion.close()


def cerrar_turno(turno_id):
    conexion = sqlite3.connect("negocio.db")
    cursor = conexion.cursor()

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        UPDATE turnos SET fecha_cierre = ? , estado = ? WHERE id = ?
    """, (ahora, 'cerrado', turno_id))

    conexion.commit()
    conexion.close()
