from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector
from model.musica import recuperar_musicas, enviar_musica, excluir_musica, ativo_inativo
from model.genero import recuperar_generos
from model.usuario import adicionar_usuarios, consulta_db

app = Flask(__name__)

app.secret_key = 'megamats'

@app.route("/")

def pagina_index():

    musicas = recuperar_musicas(True,0)
    genero = recuperar_generos()

    return render_template("/principal.html", musicas = musicas, genero = genero)

@app.route("/filtrar/<nome_genero>")

def api_filtrar_musica(nome_genero):
    musicas = recuperar_musicas(0,nome_genero)
    genero = recuperar_generos()

    return render_template("/principal.html", musicas = musicas, genero = genero)

@app.route("/login")

def pagina_login():
    return render_template("/login.html")

@app.route("/login/post", methods=["POST"])

def pagina_login_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    if consulta_db(usuario, senha):
        session['usuario_logado'] = usuario
        flash(f"Seja bem-vindo {usuario}!")
        return redirect("/adm")
    else:
        flash("Usuário ou senha inválida")
        return redirect("/login")
    
@app.route("/adm")

def pagina_adm():

    musicas = recuperar_musicas(0,0)
    genero = recuperar_generos()

    if 'usuario_logado' in session:
        return render_template("/administracao.html", musicas = musicas, genero = genero)
    else:
        return redirect("/login")
    

@app.route("/adm/post", methods = ["POST"])

def api_inserir_musica():
    
    musica = request.form.get("musica")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    atividade = "1"
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
    
@app.route("/adm/atividade/<int:codigo>/<int:atividade>")

def api_atividade_musica(codigo, atividade):
    if ativo_inativo(atividade, codigo):
        return redirect("/adm")
    else:
        return "erro"
    
@app.route("/cadastro")

def pagina_cadastro():
    return render_template("/cadastro.html")

@app.route("/cadastro/post", methods=["POST"])

def pagina_cadastro_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    senha2 = request.form.get("senha2")
    if senha != senha2:
        return redirect("/cadastro")
    else:
        if adicionar_usuarios(usuario, senha):
            return redirect("/")
        else:
            return "erro"

@app.route("/logout")

def logout_post():
    session.pop('usuario_logado', default=None)
    return redirect("/")
    
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080)
