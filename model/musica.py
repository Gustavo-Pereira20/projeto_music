from database.conexao import conectar

def recuperar_musicas(ativos:bool, filtro:None):
    conexao, cursor = conectar()
    if ativos:
        cursor.execute("SELECT codigo, cantor, duracao, atividade, nome_musica, caminho_capa, nome_genero FROM musica WHERE atividade = %s", (ativos,))
        musicas = cursor.fetchall()
        conexao.close()
        return musicas
    elif filtro:
        cursor.execute("SELECT codigo, cantor, duracao, atividade, nome_musica, caminho_capa, nome_genero FROM musica WHERE nome_genero = %s AND atividade = 1", (filtro,))
        musicas = cursor.fetchall()
        conexao.close()
        return musicas
    else:
        cursor.execute("SELECT codigo, cantor, duracao, atividade, nome_musica, caminho_capa, nome_genero FROM musica ORDER BY atividade DESC")
        musicas = cursor.fetchall()
        conexao.close()
        return musicas

def enviar_musica(a:str,b:str,c:str,d:str,e:str, f:str) -> bool:
    """Faz o envio dos dados formatados ao banco de dados e insere."""
    
    try:
        conexao, cursor = conectar()
        cursor.execute("INSERT INTO musica(cantor, duracao, atividade, nome_musica, caminho_capa, nome_genero)" \
        "VALUES(%s,%s,%s,%s,%s,%s)", (a,b,c,d,e,f))

        conexao.commit()
        conexao.close()
        
        return True

    except:

        return False
    
def excluir_musica(a:int) -> bool:

    try:
        conexao, cursor = conectar()
        cursor.execute("DELETE FROM musica " \
               "WHERE codigo = %s", (a,))

        conexao.commit()
        conexao.close()
        
        return True

    except:

        return False
    
def ativo_inativo(a:int, b:int) -> bool:

    try:
        conexao, cursor = conectar()
        
        a = int(a)
        status_atual = 0 if a == 1 else 1

        cursor.execute("UPDATE musica SET atividade = %s WHERE codigo = %s", (status_atual,b))

        conexao.commit()
        conexao.close()
        
        return True
    
    except:

        return False

    

    




