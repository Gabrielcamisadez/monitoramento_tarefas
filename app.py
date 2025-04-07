from flask import Flask, render_template, request, redirect
import sqlite3
from models import init_db

app = Flask(__name__)

# Inicializa o banco
init_db()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tarefas = conn.execute('SELECT * FROM tarefas').fetchall()
    conn.close()
    return render_template('index.html', tarefas=tarefas)

@app.route('/nova', methods=['GET', 'POST'])
def nova_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        data_entrega = request.form['data_entrega']
        prioridade = request.form['prioridade']
        responsavel = request.form['responsavel']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO tarefas (titulo, descricao, data_entrega, prioridade, responsavel) VALUES (?, ?, ?, ?, ?)',
                     (titulo, descricao, data_entrega, prioridade, responsavel))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('nova_tarefa.html')

@app.route('/concluir/<int:id>')
def concluir(id):
    conn = get_db_connection()
    conn.execute('UPDATE tarefas SET status = "Concluída" WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)