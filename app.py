from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

@app.route("/")

def pagina_index():

    conexao = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "bcd_musica"
    )

    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT codigo, cantor, duracao, nome_musica, caminho_capa, nome_genero FROM musica")

    cursor.fetchall()

    musicas = cursor.close()

    return render_template("/principal.html", musicas = musicas)

@app.route("/adm")

def pagina_adm():
    return render_template("/administracao.html")

app.run(debug=True)