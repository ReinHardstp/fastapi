from fastapi import FastAPI
import pymysql
import os

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola desde FastAPI"}

@app.get("/usuarios")
def obtener_usuarios():
    conexion = pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE"),
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios")
            return cursor.fetchall()
    finally:
        conexion.close()