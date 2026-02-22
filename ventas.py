import sqlite3
from datetime import datetime
from productos import obtener_producto, actualizar_stock

def registrar_venta(turno_id, items):
    conexion = sqlite3.connect("negocio.db")
    cursor = conexion.cursor()

    total_venta = 0
    total_costo = 0
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for item in items:
        producto = obtener_producto(item["producto_id"])

        precio_venta = producto[4]
        precio_costo = producto[3]
        cantidad = item["cantidad"] 

        total_venta += precio_venta * cantidad
        total_costo += precio_costo * cantidad
        
    cursor.execute("""
        INSERT INTO ventas (turno_id, fecha_hora, total_venta, total_costo) VALUES (?, ?, ?, ?)  
    """,(turno_id, ahora ,total_venta, total_costo))