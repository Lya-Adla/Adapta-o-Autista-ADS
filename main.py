import tkinter as tk
import sqlite3

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()

# Criando a tabela, se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT NOT NULL)''')

# Função para adicionar tarefas
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa != "":
        cursor.execute('''INSERT INTO tarefas (descricao) VALUES (?)''', (tarefa,))
        conn.commit()
        listar_tarefas()
        entrada_tarefa.delete(0, tk.END)

# Função para listar as tarefas
def listar_tarefas():
    for widget in frame_tarefas.winfo_children():
        widget.destroy()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    for tarefa in tarefas:
        label_tarefa = tk.Label(frame_tarefas, text=tarefa[1])
        label_tarefa.pack()

# Configuração da janela
root = tk.Tk()
root.title("Assistente de Tarefas - Autista ADS")

# Caixa de entrada de tarefas
entrada_tarefa = tk.Entry(root, width=50)
entrada_tarefa.pack(pady=10)

# Botão para adicionar tarefa
botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=5)

# Frame para exibir as tarefas
frame_tarefas = tk.Frame(root)
frame_tarefas.pack(pady=10)

# Listar tarefas ao iniciar
listar_tarefas()

# Iniciar a interface gráfica
root.mainloop()

# Fechar a conexão com o banco de dados
conn.close()
