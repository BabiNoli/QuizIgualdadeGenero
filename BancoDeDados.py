import mysql.connector
from mysql.connector import Error


class BancoDeDados:
    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = self.create_connection()


    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            if connection.is_connected():
                print("✅ Conexão com o banco de dados bem-sucedida!")
                return connection
        except Error as e:
            print(f"Erro de conexão: {e}")
            print(f"❌ Erro de conexão com MySQL: {e}")
            return None

    def buscar_perguntas(self, idioma):
        if not self.connection:
            return []
        if idioma == "1":
            query = """SELECT id_pergunta, texto_pergunta AS texto_pergunta, tipo_pergunta 
                       FROM perguntas ORDER BY RAND() LIMIT 10"""
        elif idioma == "2":
            query = """SELECT id_pergunta, texto_pergunta_ingles AS texto_pergunta, tipo_pergunta 
                       FROM perguntas ORDER BY RAND() LIMIT 10"""
        else:
            query = """SELECT id_pergunta, texto_pergunta_alemao AS texto_pergunta, tipo_pergunta 
                       FROM perguntas ORDER BY RAND() LIMIT 10"""

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()

    def buscar_alternativas(self, id_pergunta, tipo_pergunta, idioma):
        if not self.connection:
            return []
        if idioma == "1":  # Português
            if tipo_pergunta == 1:
                query = """SELECT texto_resposta, peso 
                           FROM resposta_multipla 
                           WHERE Perguntas_id_pergunta = %s ORDER BY RAND()"""
            else:
                query = """SELECT texto_resposta, peso 
                           FROM verdadeiro_falso 
                           WHERE Perguntas_id_pergunta = %s ORDER BY RAND()"""
        elif idioma == "2":  # Inglês
            if tipo_pergunta == 1:
                query = """SELECT texto_resposta_ingles AS texto_resposta, peso 
                           FROM resposta_multipla 
                           WHERE Perguntas_id_pergunta = %s ORDER BY RAND()"""
            else:
                query = """SELECT texto_resposta_ingles AS texto_resposta, peso 
                           FROM verdadeiro_falso 
                           WHERE Perguntas_id_pergunta = %s ORDER BY RAND()"""
        else:  # Alemão
            if tipo_pergunta == 1:
                query = """SELECT texto_resposta_alemao AS texto_resposta, peso 
                           FROM resposta_multipla 
                           WHERE Perguntas_id_pergunta = %s ORDER BY RAND()"""
            else:
                query = """SELECT texto_resposta_alemao AS texto_resposta, peso 
                           FROM verdadeiro_falso 
                           WHERE Perguntas_id_pergunta = %s ORDER BY RAND()"""

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, (id_pergunta,))
        return cursor.fetchall()

    def registrar_usuario(self, nome, idade, genero, pin):
        if not self.connection:
            return False
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO usuario (nome, idade, genero, pin) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nome, idade, genero, pin))
            self.connection.commit()
            return True
        except Error:
            return False

    def login_usuario(self, nome, pin):
        if not self.connection:
            return None
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM usuario WHERE nome = %s AND pin = %s"
            cursor.execute(query, (nome, pin))
            return cursor.fetchone()
        except Error:
            return None

    def atualizar_pontuacao(self, nome, pin, pontuacao_atual):

        if not self.connection:
            return
        try:
            cursor = self.connection.cursor()
            query = """
                           UPDATE usuario
                           SET pont_max = GREATEST(pont_max, %s),
                               pont_atual = %s
                           WHERE nome = %s AND pin = %s
                           """
            cursor.execute(query, (pontuacao_atual, pontuacao_atual, nome, pin))
            self.connection.commit()
        except Error as e:
            print("Erro ao atualizar pontuação:", e)


    def buscar_pontuacao_maxima(self, nome, pin):

        if not self.connection:
            return 0
        try:
            cursor = self.connection.cursor()
            query = """SELECT pont_max FROM usuario WHERE nome = %s AND pin = %s"""
            cursor.execute(query, (nome, pin))
            result = cursor.fetchone()
            if result and result[0] is not None:
                return result[0]
            else:
                return 0
        except Error as e:
            print("Erro ao buscar pontuacao_maxima:", e)
            return 0
