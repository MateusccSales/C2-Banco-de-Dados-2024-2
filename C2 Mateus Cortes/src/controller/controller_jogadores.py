from model.jogadores import Jogador
from conexion.oracle_queries import OracleQueries

class Controller_Jogador:
    def __init__(self):
        pass

    def inserir_jogador(self) -> Jogador:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_jogador = int(input("Novo ID de jogador (numero inteiro positivo): "))
        while id_jogador < 1:
            id_jogador = int(input("Insira um numero inteiro positivo para o novo Id de jogador: "))

        if self.verificar_existencia_jogador(oracle, id_jogador):
            nome_jogador = input("Nome do novo jogador: ")
            print("""Escolha a região do jogador: 
                    1 - America do Sul
                    2 - America Central
                    3 - America do Norte
                    4 - Europa
                    5 - Ásia
                    6 - Oriente Médio
                  """)
            opcao = int(input("Digite uma opção: "))
            while( opcao < 0 or opcao > 6):
                opcao = int(input("Digite uma opção válida: "))
            
            if(opcao == 1):
                regiao = "america do sul"
            elif(opcao == 2):
                regiao = "america central"
            elif(opcao == 3):
                regiao = "america do norte"
            elif(opcao == 4):
                regiao = "europa"
            elif(opcao == 5):
                regiao = "asia"
            elif(opcao == 6):
                regiao = "oriente medio"

            # Insere e persiste o novo jogador
            oracle.write(f"insert into jogadores values ({id_jogador}, '{nome_jogador}', '{regiao}')")
            # Recupera os dados do novo jogador criado transformando em um DataFrame
            df_jogador = oracle.sqlToDataFrame(f"select id_jogador, nome_jogador, regiao from jogadores where id_jogador = {id_jogador}")
            # Criar um nojo objeto Jogador
            novo_jogador = Jogador(df_jogador.id_jogador.values[0], df_jogador.nome_jogador.values[0], df_jogador.regiao.values[0])
            # Exibe os atributos do novo jogador
            print(novo_jogador.to_string())
            
            return novo_jogador
        else:
            print(f"O ID {id_jogador} já está cadastrado.")
            return None
    
    def atualizar_jogador(self) -> Jogador:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_jogador = int(input("Informe o ID do jogador que deseja atualizar: "))

        if not self.verificar_existencia_jogador(oracle, id_jogador):
            nome_jogador = input("Novo Nome do jogador: ")

            print("""Escolha a região do jogador: 
                    1 - America do Sul
                    2 - America Central
                    3 - America do Norte
                    4 - Europa
                    5 - Ásia
                    6 - Oriente Médio
                  """)
            opcao = int(input("Digite uma opção: "))
            while( opcao < 0 or opcao > 6):
                opcao = int(input("Digite uma opção válida: "))
            
            if(opcao == 1):
                regiao = "america do sul"
            elif(opcao == 2):
                regiao = "america central"
            elif(opcao == 3):
                regiao = "america do norte"
            elif(opcao == 4):
                regiao = "europa"
            elif(opcao == 5):
                regiao = "asia"
            elif(opcao == 6):
                regiao = "oriente medio"
            
            # Atualiza o jogador existente
            oracle.write(f"update jogadores set nome_jogador = '{nome_jogador}', regiao = '{regiao}' where id_jogador = {id_jogador}")

            df_jogador = oracle.sqlToDataFrame(f"select id_jogador, nome_jogador, regiao from jogadores where id_jogador = {id_jogador}")

            jogador_atualizado = Jogador(df_jogador.id_jogador.values[0], df_jogador.nome_jogador.values[0], df_jogador.regiao.values[0])

            print(jogador_atualizado.to_string())

            return jogador_atualizado
        else:
            print(f"O ID {id_jogador} não existe.")
            return None

    def excluir_jogador(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_jogador = int(input("Informe o ID do jogador que deseja excluir: "))

        if not self.verificar_existencia_jogador(oracle, id_jogador):
            df_jogador = oracle.sqlToDataFrame(f"select id_jogador, nome_jogador, regiao from jogadores where id_jogador = {id_jogador}")
            # Remove o jogador da tabela
            oracle.write(f"delete from jogadores where id_jogador = {id_jogador}")
            # Cria um novo objeto jogador para informar que foi removido
            jogador_excluido = Jogador(df_jogador.id_jogador.values[0], df_jogador.nome_jogador.values[0], df_jogador.regiao.values[0])
            # Exibe os atributos do jogador excluído
            print("Jogador removido com sucesso!")
            print(jogador_excluido.to_string())
        else:
            print(f"O ID {id_jogador} não existe.")
    
    def verificar_existencia_jogador(self, oracle:OracleQueries, id_jogador:int=None) -> bool:
        # Recupera os dados do novo jogador criado transformando em um DataFrame
        df_jogador = oracle.sqlToDataFrame(f"select id_jogador, nome_jogador, regiao from jogadores where id_jogador = {id_jogador}")
        return df_jogador.empty