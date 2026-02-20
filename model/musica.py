from database.conexao import conectar

def recuperar_musicas():
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, nome_musica, caminho_capa, nome_genero FROM musica")
    musicas = cursor.fetchall()

    conexao.close()

    return musicas

def enviar_musica(a:str,b:str,c:str,d:str,e:str) -> bool:
    """Faz o envio dos dados formatados ao banco de dados e insere."""
    conexao, cursor = conectar()

    try:

        cursor.execute("INSERT INTO musica(cantor, duracao, nome_musica, caminho_capa, nome_genero)" \
        "VALUES(%s,%s,%s,%s,%s)", (a,b,c,d,e))

        conexao.commit()
        conexao.close()
        
        return True

    except:

        conexao.close()

        return False

    

    




