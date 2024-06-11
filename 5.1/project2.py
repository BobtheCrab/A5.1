import sqlite3
import time
import random


elementos_sistema = ['CPU', 'GPU', 'Disco Duro', 'RAM']


conexion = sqlite3.connect('temperaturas_sistema.db')
cursor = conexion.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS temperaturas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    elemento TEXT,
                    temperatura REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
conexion.commit()


def obtener_temperatura():
    return round(random.uniform(30.0, 90.0), 2)


def guardar_temperatura(elemento, temperatura):
    cursor.execute('''INSERT INTO temperaturas (elemento, temperatura) VALUES (?, ?)''', (elemento, temperatura))
    conexion.commit()


def revisar_temperaturas():
    while True:
        for elemento in elementos_sistema:
            temperatura = obtener_temperatura()
            guardar_temperatura(elemento, temperatura)
            print(f"Elemento: {elemento}, Temperatura: {temperatura}°C")
        
        
        time.sleep(5)


try:
    revisar_temperaturas()
except KeyboardInterrupt:
    print("Detenido por el usuario.")
finally:
    conexion.close()
