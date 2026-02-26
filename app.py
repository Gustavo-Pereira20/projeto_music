from flask import Flask, render_template, request, redirect
import mysql.connector
from model.musica import recuperar_musicas, enviar_musica, excluir_musica, ativo_inativo
from model.genero import recuperar_generos, filtrar_generos

app = Flask(__name__)

@app.route("/")

def pagina_index():

    musicas = recuperar_musicas()
    genero = recuperar_generos()

    return render_template("/principal.html", musicas = musicas, genero = genero)

@app.route("/filtrar/<nome_genero>")

def api_filtrar_musica(nome_genero):
    musicas = filtrar_generos(nome_genero)
    genero = recuperar_generos()

    return render_template("/principal.html", musicas = musicas, genero = genero)

@app.route("/adm")

def pagina_adm():

    musicas = recuperar_musicas()
    genero = recuperar_generos()

    return render_template("/administracao.html", musicas = musicas, genero = genero)

@app.route("/adm/post", methods = ["POST"])

def api_inserir_musica():
    
    musica = request.form.get("musica")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    atividade = "ATIVO"
    url_capa = request.form.get("url_capa")
    categoria = request.form.get("categoria")
    
    if enviar_musica(cantor, duracao, atividade, musica, url_capa, categoria):
        return redirect("/adm")
    else:
        return "erro"
    
@app.route("/adm/delete/<int:codigo>")

def api_deletar_musica(codigo):
    if excluir_musica(codigo):
        return redirect("/adm")
    else:
        return "erro"
    
@app.route("/adm/atividade/<int:codigo>/<atividade>")

def api_atividade_musica(codigo, atividade):
    if ativo_inativo(atividade, codigo):
        return redirect("/adm")
    else:
        return "erro"

app.run(debug=True)
