import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            data_entrega TEXT,
            prioridade TEXT,
            status TEXT DEFAULT 'Pendente',
            responsavel TEXT
        )
    ''')
    conn.commit()
    conn.close()