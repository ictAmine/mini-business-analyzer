import sqlite3
import pandas as pd

conn = sqlite3.connect("empresa.db")

query = """
SELECT
    c.nombre,
    c.ciudad,
    p.monto
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
"""

df = pd.read_sql(query, conn)

print("\n📌 Datos combinados:")
print(df)

print("\n💰 Gasto total por cliente:")
print(df.groupby("nombre")["monto"].sum().sort_values(ascending=False))

print("\n🏙️ Gasto total por ciudad:")
print(df.groupby("ciudad")["monto"].sum())

conn.close()
