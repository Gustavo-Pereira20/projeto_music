from flask import Flask, render_template, request, redirect
import mysql.connector
from model.musica import recuperar_musicas, enviar_musica
from model.genero import recuperar_generos

app = Flask(__name__)

@app.route("/")

def pagina_index():

    musicas = recuperar_musicas()
    genero = recuperar_generos()

    return render_template("/principal.html", musicas = musicas, genero = genero)

@app.route("/adm")

def pagina_adm():

    musicas = recuperar_musicas()
    genero = recuperar_generos()

    return render_template("/administracao.html", musicas = musicas, genero = genero)

@app.route("/adm", methods = ["POST"])

def pagina_post():
    
    musica = request.form.get("musica")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    url_capa = request.form.get("url_capa")
    categoria = request.form.get("categoria")

    enviar_musica(cantor, duracao, musica, url_capa, categoria)
    
    return redirect("/adm")

app.run(debug=True)