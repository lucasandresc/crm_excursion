import sqlite3
import os
from database import DB_NAME

# Crear todas las tablas necesarias si no existen

def crear_tabla_excursiones():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS excursiones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            duracion TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL,
            tipo TEXT NOT NULL,
            extra TEXT
        )
    """)
    conn.commit()
    conn.close()

def crear_tabla_agencias():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agencias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT,
            telefono TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

def crear_tabla_reservas():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agencia_id INTEGER,
            excursion_id INTEGER,
            fecha TEXT,
            FOREIGN KEY (agencia_id) REFERENCES agencias(id),
            FOREIGN KEY (excursion_id) REFERENCES excursiones(id)
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_tabla_excursiones()
    crear_tabla_agencias()
    crear_tabla_reservas()
    print("Base de datos y tablas creadas correctamente.")