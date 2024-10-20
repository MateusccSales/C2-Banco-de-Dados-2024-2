from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_jogadores = config.QUERY_COUNT.format(tabela="jogadores")
        self.qry_total_personagens = config.QUERY_COUNT.format(tabela="personagens")
        self.qry_total_jogadores_personagens = config.QUERY_COUNT.format(tabela="jogadores_personagens")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Mateus Côrtes"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2024/2"

    def get_total_jogadores(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_jogadores)["total_jogadores"].values[0]

    def get_total_personagens(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_personagens)["total_personagens"].values[0]

    def get_total_jogadores_personagens(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_jogadores_personagens)["total_jogadores_personagens"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - JOGADORES:         {str(self.get_total_jogadores()).rjust(5)}
        #      2 - PERSONAGENS:         {str(self.get_total_personagens()).rjust(5)}
        #      3 - JOGADORES_PERSONAGENS:     {str(self.get_total_jogadores_personagens()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """