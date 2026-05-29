import sqlite3

conexao = sqlite3.connect("clientes.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conexao.commit()

cursor.execute(
    "INSERT INTO clientes (nome, email) VALUES (?, ?)",
    ("Ana", "ana@gmail.com")
)

cursor.execute(
    "INSERT INTO clientes (nome, email) VALUES (?, ?)",
    ("Carlos", "carlos@gmail.com")
)

cursor.execute(
    "INSERT INTO clientes (nome, email) VALUES (?, ?)",
    ("Amanda", "amanda@gmail.com")
)

conexao.commit()

print("Clientes cadastrados!")

cursor.execute("SELECT * FROM clientes")

clientes = cursor.fetchall()

print("\nLista de clientes:")

for cliente in clientes:
    print(cliente)

cursor.execute(
    "SELECT * FROM clientes WHERE nome LIKE 'A%'"
)

resultado = cursor.fetchall()

print("\nClientes com nome começando com A:")

for cliente in resultado:
    print(cliente)

cursor.execute("""
UPDATE clientes
SET email = ?
WHERE nome = ?
""", ("novoemail@gmail.com", "Carlos"))

conexao.commit()

print("\nCliente atualizado!")

cursor.execute("""
DELETE FROM clientes
WHERE nome = ?
""", ("Amanda",))

conexao.commit()

print("\nCliente deletado!")

cursor.execute("SELECT * FROM clientes")

clientes = cursor.fetchall()

print("\nLista final:")

for cliente in clientes:
    print(cliente)

conexao.close()