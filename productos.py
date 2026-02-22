import sqlite3

def agregar_producto(nombre, categoria, precio_costo, precio_venta, stock, stock_minimo):
    conexion = sqlite3.connect("negocio.db")
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO productos (nombre, categoria, precio_costo, precio_venta, stock, stock_minimo) VALUES (?, ?, ? , ? , ? ,?)
    """,(nombre, categoria, precio_costo, precio_venta, stock, stock_minimo))

    conexion.commit()
    conexion.close()
    print(f"Fue agregado: Producto: {nombre}, Categoria: {categoria}, Precio de costo: {precio_costo}, Precio de venta: {precio_venta}, Stock: {stock}, Stock minimo {stock_minimo}")


def listar_productos():
    conexion = sqlite3.connect("negocio.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM productos
    """)

    resultados = cursor.fetchall()
    for productos in resultados:
        print(productos)
    conexion.close()


def actualizar_stock(producto_id, cantidad):
    conexion = sqlite3.connect("negocio.db")
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE productos SET stock = stock - ? WHERE id = ?
    """, (cantidad, producto_id))
    
    conexion.commit()
    conexion.close()

def obtener_producto(producto_id):
    conexion = sqlite3.connect("negocio.db")
    cursor = conexion.cursor()

    cursor.execute(""" 
        SELECT * FROM productos WHERE id = ?
    """,(producto_id,))

    resultados = cursor.fetchone()

    conexion.close()

    return resultados