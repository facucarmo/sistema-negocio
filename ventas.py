import sqlite3
from datetime import datetime
from database import get_conexion
from productos import obtener_producto, actualizar_stock

def registrar_venta(turno_id, items):
    conexion = get_conexion()
    cursor = conexion.cursor()

    total_venta = 0
    total_costo = 0
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item in items:
        producto = obtener_producto(item["producto_id"])
        total_venta += producto[4] * item["cantidad"]
        total_costo += producto[3] * item["cantidad"]

    cursor.execute("""
        INSERT INTO ventas (turno_id, fecha_hora, total_venta, total_costo) VALUES (?, ?, ?, ?)
    """, (turno_id, ahora, total_venta, total_costo))

    venta_id = cursor.lastrowid

    for item in items:
        producto = obtener_producto(item["producto_id"])
        cursor.execute("""
            INSERT INTO items_venta (venta_id, producto_id, cantidad, precio_unitario, costo_unitario) VALUES (?, ?, ?, ?, ?)
        """, (venta_id, item["producto_id"], item["cantidad"], producto[4], producto[3]))
        actualizar_stock(item["producto_id"], item["cantidad"], cursor)

    conexion.commit()
    conexion.close()

    ganancia = total_venta - total_costo
    print(f"Venta registrada. Total: ${total_venta}, Ganancia: ${ganancia}")
    
