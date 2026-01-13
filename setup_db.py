import sqlite3

conn = sqlite3.connect("empresa.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    ciudad TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    monto REAL,
    fecha TEXT
)
""")

clientes = [
    (1, "Ana", "Madrid"),
    (2, "Luis", "Barcelona"),
    (3, "Sara", "Valencia")
]

pedidos = [
    (1, 1, 120.50, "2025-01-01"),
    (2, 1, 80.00, "2025-01-10"),
    (3, 2, 200.00, "2025-01-03"),
    (4, 3, 50.00, "2025-01-05")
]

cursor.executemany("INSERT INTO clientes VALUES (?, ?, ?)", clientes)
cursor.executemany("INSERT INTO pedidos VALUES (?, ?, ?, ?)", pedidos)

conn.commit()
conn.close()
