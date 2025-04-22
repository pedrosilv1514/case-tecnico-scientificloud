import sqlite3

from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "database.db"

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def buscar_territorio_id(id_territorio):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, dimensao FROM territorios WHERE id = ?", (id_territorio,))
        return cursor.fetchone()
    
def buscar_territorio_nome(nome):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, dimensao FROM territorios WHERE LOWER(nome) = LOWER(?)", (nome,))
        return cursor.fetchone()

def inserir_territorio(id_territorio, nome, dimensao):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO territorios (id, nome, dimensao) VALUES (?, ?, ?)", (id_territorio, nome, dimensao))
        conn.commit()