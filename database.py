import sqlite3

def crear_database():
    conexion = sqlite3.connect("negocio.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            pin TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            categoria TEXT,
            precio_costo REAL NOT NULL,
            precio_venta REAL NOT NULL,
            stock INTEGER NOT NULL,
            stock_minimo INTEGER DEFAULT 0
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS turnos (
            id INTEGER PRIMARY KEY,
            empleado_id INTEGER NOT NULL,
            fecha_apertura TEXT NOT NULL,
            fecha_cierre TEXT,
            estado TEXT DEFAULT 'abierto',
            FOREIGN KEY (empleado_id) REFERENCES empleados(id)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY,
            turno_id INTEGER NOT NULL,
            fecha_hora TEXT NOT NULL,
            total_venta REAL NOT NULL,
            total_costo REAL NOT NULL,
            FOREIGN KEY(turno_id) REFERENCES turnos(id)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items_venta (
            id INTEGER PRIMARY KEY,
            venta_id INTEGER NOT NULL,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            costo_unitario REAL NOT NULL,
            FOREIGN KEY (venta_id) REFERENCES ventas(id),
            FOREIGN KEY (producto_id) REFERENCES productos(id)
        )
    """)
    
    conexion.commit()
    conexion.close()
    print("Base de datos creada correctamente.")

def get_conexion():
    conexion = sqlite3.connect("negocio.db")
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

if __name__ == "__main__":
    crear_database()