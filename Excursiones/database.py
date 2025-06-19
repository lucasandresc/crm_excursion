import os
import sqlite3
import sys

# Path base para PyInstaller
if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

DB_NAME = os.path.join(base_dir, "turismo.db")

# Contadores para el dashboard

def contar_excursiones():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM excursiones")
    total = cursor.fetchone()[0]
    conn.close()
    return total

def contar_agencias():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM agencias")
    total = cursor.fetchone()[0]
    conn.close()
    return total

def contar_reservas():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM reservas")
    total = cursor.fetchone()[0]
    conn.close()
    return total
