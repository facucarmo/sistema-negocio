import sqlite3
from database import get_conexion

def agregar_empleado(nombre, pin):
    conexion = get_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO empleados (nombre, pin) VALUES (? , ?)
    """,(nombre, pin))

    conexion.commit()
    conexion.close()
    print (f"Empleado '{nombre}' agregado correctamente.")


def listar_empleados():
    conexion = sqlite3.connect("negocio.db")
    cursor = conexion.cursor()
    
    cursor.execute("""
        SELECT * FROM empleados
    """)
    resultados = cursor.fetchall()
    for empleado in resultados:
        print (empleado)
    conexion.close()
