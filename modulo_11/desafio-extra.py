import sqlite3

conexao = sqlite3.connect("tarefas.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarefa TEXT NOT NULL
)
""")

conexao.commit()

def adicionar_tarefa():

    nome = input("Digite a tarefa: ")

    cursor.execute("""
    INSERT INTO tarefas (tarefa)
    VALUES (?)
    """, (nome,))

    conexao.commit()

    print("Tarefa adicionada!")

def visualizar_tarefas():

    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()

    print("\nLista de tarefas:")

    for tarefa in tarefas:
        print(tarefa)

def excluir_tarefa():

    id_tarefa = input("Digite o ID da tarefa: ")

    cursor.execute("""
    DELETE FROM tarefas
    WHERE id = ?
    """, (id_tarefa,))

    conexao.commit()

    print("Tarefa excluída!")

while True:

    print("""
1 - Adicionar tarefa
2 - Ver tarefas
3 - Excluir tarefa
4 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        visualizar_tarefas()

    elif opcao == "3":
        excluir_tarefa()

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")

conexao.close()