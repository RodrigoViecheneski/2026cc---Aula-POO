import mysql.connector

class Cliente:

    def __init__(self, id=None, nome="", email=""):
        self.id = id
        self.nome = nome
        self.email = email


        #pip install mysql-connector-
        
        # python -m pip install mysql-connector-python