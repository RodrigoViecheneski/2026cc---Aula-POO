import tkinter as tk
from tkinter import messagebox
import mysql.connector

class ClienteDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema"
        )
        self.cursor = self.conexao.cursor()

    def criar(self, cliente):
        sql = "INSERT INTO usuarios(nome, email) VALUES (%s, %s)"
        self.cursor.execute(sql, (cliente.nome, cliente.email ))
        self.conexao.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()
    
    def atualizar(self, cliente):
        sql = "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s"
        self.cursor.execute(sql, (cliente.nome, cliente.email, cliente.id))
        self.conexao.commit()

    