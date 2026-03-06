from database.conexao import conectar

def adicionar_usuarios(a:str, b:str) -> bool:
    """Função que adiciona os usuários na database"""
    try:
        conexao, cursor = conectar()
        cursor.execute("INSERT INTO usuario(usuario, senha)" \
        "VALUES(%s,%s)", (a,b))

        conexao.commit()
        conexao.close()
        
        return True

    except:

        return False
    
def consulta_db(a:str, b:str) -> bool:
    """Função que consulta usuários na database"""

    conexao, cursor = conectar()
    cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND senha = %s", (a,b))
    
    v = cursor.fetchone()
    conexao.close()

    if v == None:
        return False
    else:
        return True

    