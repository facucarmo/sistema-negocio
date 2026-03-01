import sqlite3
from database import get_conexion

def agregar_producto(nombre, categoria, precio_costo, precio_venta, stock, stock_minimo):
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO productos (nombre, categoria, precio_costo, precio_venta, stock, stock_minimo) VALUES (?, ?, ?, ?, ?, ?)
    """, (nombre, categoria, precio_costo, precio_venta, stock, stock_minimo))
    conexion.commit()
    conexion.close()
    print(f"Producto '{nombre}' agregado correctamente.")

def listar_productos():
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()
    for producto in resultados:
        print(producto)
    conexion.close()

def obtener_producto(producto_id):
    conexion = get_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado

def actualizar_stock(producto_id, cantidad, cursor=None):
    if cursor is None:
        conexion = get_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE productos SET stock = stock - ? WHERE id = ?
        """, (cantidad, producto_id))
        conexion.commit()
        conexion.close()
    else:
        cursor.execute("""
            UPDATE productos SET stock = stock - ? WHERE id = ?
        """, (cantidad, producto_id))
