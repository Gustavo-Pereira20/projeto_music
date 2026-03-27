import mysql.connector

def conectar():
        tipo = "NUVEM"
        if tipo == "LOCAL":
            conexao = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "root",
                database = "bcd_musica")
        else:
            conexao = mysql.connector.connect(
                host = "servidor-tavao-servidor-tavao.a.aivencloud.com",
                port = 26017,
                user = "avnadmin",
                password = "AVNS_TsFbdibzsDBGCyPHlxE",
                database = "bcd_musica")
                
        cursor = conexao.cursor(dictionary=True)
        return conexao, cursor
