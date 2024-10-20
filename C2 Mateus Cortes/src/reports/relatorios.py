from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        with open("sql/relatorio_jogadores.sql") as f:
            self.query_relatorio_jogadores = f.read()

        with open("sql/relatorio_personagens.sql") as f:
            self.query_relatorio_personagens = f.read()
        
        with open("sql/relatorio_jogadores_personagens.sql") as f:
            self.query_relatorio_jogadores_personagens = f.read()

        with open("sql/relatorio_classificacao_mundial.sql") as f:
            self.query_relatorio_classificacao_mundial = f.read()

        with open("sql/relatorio_classificacao_america_do_sul_e_central.sql") as f:
            self.query_relatorio_classificacao_america_sul_central = f.read()

        with open("sql/relatorio_classificacao_america_do_norte.sql") as f:
            self.query_relatorio_classificacao_america_norte = f.read()

        with open("sql/relatorio_classificacao_europa.sql") as f:
            self.query_relatorio_classificacao_europa = f.read()

        with open("sql/relatorio_classificacao_oriente_medio.sql") as f:
            self.query_relatorio_classificacao_oriente_medio = f.read()

        with open("sql/relatorio_classificacao_asia.sql") as f:
            self.query_relatorio_classificacao_asia = f.read()

    def get_relatorio_jogadores(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_jogadores))
        input("Pressione Enter para Sair do Relatório de Jogadores")
    
    def get_relatorio_personagens(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_personagens))
        input("Pressione Enter para Sair do Relatório de Personagens")
    
    def get_relatorio_jogadores_personagens(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_jogadores_personagens))
        input("Pressione Enter para Sair do Relatório de Jogadores_Personagens")

    def get_relatorio_classificacao_mundial(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_classificacao_mundial))
        input("Pressione Enter para Sair do Relatório da Classificação Mundial")

    def get_relatorio_classificacao_america_sul_central(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_classificacao_america_sul_central))
        input("Pressione Enter para Sair do Relatório da Classificação America do Sul e Central")

    def get_relatorio_classificacao_america_norte(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_classificacao_america_norte))
        input("Pressione Enter para Sair do Relatório da Classificação America do Norte")

    def get_relatorio_classificacao_europa(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_classificacao_europa))
        input("Pressione Enter para Sair do Relatório da Classificação Europa")

    def get_relatorio_classificacao_oriente_medio(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_classificacao_oriente_medio))
        input("Pressione Enter para Sair do Relatório da Classificação Oriente Médio")

    def get_relatorio_classificacao_asia(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_classificacao_asia))
        input("Pressione Enter para Sair do Relatório da Classificação Ásia")