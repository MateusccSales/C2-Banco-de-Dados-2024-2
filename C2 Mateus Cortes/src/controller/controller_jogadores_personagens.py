from model.jogadores_personagens import JogadorPersonagem
from model.jogadores import Jogador
from controller.controller_jogadores import Controller_Jogador
from model.personagens import Personagem
from controller.controller_personagens import Controller_Personagem
from conexion.oracle_queries import OracleQueries
from utils.splash_screen import SplashScreen

class Controller_Jogador_Personagem:
    def __init__(self):
        self.ctrl_jogador = Controller_Jogador()
        self.ctrl_personagem = Controller_Personagem()
    
    def inserir_jogador_personagem(self) -> JogadorPersonagem:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_jogador = int(input("Informe o ID do Jogador: "))
        jogador = self.validar_jogador(oracle, id_jogador)
        if jogador == None:
            return None
        
        id_personagem = int(input("Informe o ID do Personagem: "))
        personagem = self.validar_personagem(oracle, id_personagem)
        if personagem == None:
            return None
        
        if self.verificar_existencia_jogador_personagem(oracle, id_jogador, id_personagem):
            pontuacao = int(input("Insira uma pontuação (numero inteiro positivo menor ou igual a 3000)"))
            while pontuacao < 0 or pontuacao > 3000:
                pontuacao = int(input("Insira uma pontuação valida: "))
            
            id_classificacao = int(SplashScreen.get_total_jogadores_personagens())

            oracle.write(f"insert into jogadores_personagens values ({id_classificacao}, {jogador.id_jogador}, {personagem.id_personagem}, {pontuacao})")

            df_jogador_personagem = oracle.sqlToDataFrame(f"select id_classificacao, id_jogador, id_personagem, pontuacao from jogadores_personagens where id_classificacao = {id_classificacao}")

            novo_jogador_personagem = JogadorPersonagem(df_jogador_personagem.id_classificacao.values[0], jogador, personagem, df_jogador_personagem.pontuacao.values[0])

            print(novo_jogador_personagem.to_string())

            return novo_jogador_personagem
        else:
            print(f"A combinação de ID de jogador {id_jogador} e do ID de Personagem {id_personagem} já está cadastrada.")
            return None
    
    def atualizar_jogador_personagem(self) -> JogadorPersonagem:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_jogador = int(input("Informe o ID do Jogador: "))
        jogador = self.validar_jogador(oracle, id_jogador)
        if jogador == None:
            return None
        
        id_personagem = int(input("Informe o ID do Personagem: "))
        personagem = self.validar_personagem(oracle, id_personagem)
        if personagem == None:
            return None
        
        df_jogador_personagem = oracle.sqlToDataFrame(f"select id_classificacao, id_jogador, id_personagem, pontuacao from jogadores_personagens where (id_jogador = {id_jogador} and id_personagem = {id_personagem})")
        jogador_personagem = JogadorPersonagem(df_jogador_personagem.id_classificacao.values[0], jogador, personagem, df_jogador_personagem.pontuacao.values[0])
        print("Jogador Personagem a ser modificado: ")
        print(jogador_personagem.to_string())
        print(" ")
        id_classificacao = jogador_personagem.get_id_classificacao()
        
        if not self.verificar_existencia_jogador_personagem(oracle, id_jogador, id_personagem):
            print("""Deseja mudar o ID do jogador?
                    1 - Sim
                    2 - Não""")
            opcao = int(input("Digite o numero da opção: "))
            while(opcao < 1 or opcao > 2):
                opcao = int(input("Digite uma opcao valida: "))
            
            if opcao == 1:
                novo_id_jogador = int(input("Informe o novo ID de jogador: "))
                novo_jogador = self.validar_jogador(oracle, novo_id_jogador)
                if novo_jogador == None:
                    return None
                else:
                    jogador = novo_jogador
            elif opcao == 2:
                novo_id_jogador = id_jogador
                jogador = jogador

            print("""Deseja mudar o ID do personagem?
                    1 - Sim
                    2 - Não""")
            opcao = int(input("Digite o numero da opção: "))
            while(opcao < 1 or opcao > 2):
                opcao = int(input("Digite uma opcao valida: "))
            
            if opcao == 1:
                novo_id_personagem = int(input("Informe o novo ID de personagem: "))
                novo_personagem = self.validar_personagem(oracle, novo_id_personagem)
                if novo_personagem == None:
                    return None
                else:
                    personagem = novo_personagem
            elif opcao == 2:
                novo_id_personagem = id_personagem
                personagem = personagem
            
            if self.verificar_existencia_jogador_personagem(oracle, novo_id_jogador, novo_id_personagem):

                nova_pontuacao = int(input("Insira uma nova pontuação (numero inteiro positivo menor ou igual a 3000)"))
                while nova_pontuacao < 0 or nova_pontuacao > 3000:
                    nova_pontuacao = int(input("Insira uma pontuação valida: "))

                oracle.write(f"update jogadores_personagens set id_jogador = {novo_id_jogador}, id_personagem = {novo_id_personagem}, pontuacao = {nova_pontuacao} where id_classificacao = {id_classificacao}")
                df_jogador_personagem_atualizado = oracle.sqlToDataFrame(f"select id_classificacao, id_jogador, id_personagem, pontuacao from jogadores_personagens where id_classificacao = {id_classificacao}")
                jogador_personagem_atualizado = JogadorPersonagem(df_jogador_personagem_atualizado.id_classificacao.values[0], jogador, personagem, df_jogador_personagem_atualizado.pontuacao.values[0])
                print("Registro atualizado para: ")
                print(jogador_personagem_atualizado.to_string())
            else:
                print(f"A combinação de ID de jogador {novo_id_jogador} e do ID de Personagem {novo_id_personagem} já está cadastrada.")
                return None

    def excluir_jogador_personagem(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_jogador = int(input("Informe o ID do Jogador: "))
        jogador = self.validar_jogador(oracle, id_jogador)
        if jogador == None:
            return None
        
        id_personagem = int(input("Informe o ID do Personagem: "))
        personagem = self.validar_personagem(oracle, id_personagem)
        if personagem == None:
            return None
        
        if not self.verificar_existencia_jogador_personagem(oracle, id_jogador, id_personagem):
            df_jogador_personagem = oracle.sqlToDataFrame(f"select id_classificacao, id_jogador, id_personagem, pontuacao from jogadores_personagens where (id_jogador = {id_jogador} and id_personagem = {id_personagem})")
            jogador_personagem_excluido = JogadorPersonagem(df_jogador_personagem.id_classificacao.values[0], jogador, personagem, df_jogador_personagem.pontuacao.values[0])
            id_classificacao = jogador_personagem_excluido.get_id_classificacao()
            oracle.write(f"delete from jogadores_personagens where id_classificacao = {id_classificacao}")
            print("Registro removido com sucesso!")
            print(jogador_personagem_excluido.to_string())
        else:
            print("Registro não existe.")

    def verificar_existencia_jogador_personagem(self, oracle:OracleQueries, id_jogador:int=None, id_personagem:int=None) -> bool:
        df_jogador_personagem = oracle.sqlToDataFrame(f"select id_classificacao, id_jogador, id_personagem, pontuacao from jogadores_personagens where (id_jogador = {id_jogador} and id_personagem = {id_personagem})")
        return df_jogador_personagem.empty
    
    def validar_jogador(self, oracle:OracleQueries, id_jogador:int=None) -> Jogador:
        if self.ctrl_jogador.verificar_existencia_jogador(oracle, id_jogador):
            print(f"O jogador de ID {id_jogador} não existe.")
            return None
        else:
            oracle.connect()
            df_jogador = oracle.sqlToDataFrame(f"select id_jogador, nome_jogador, regiao from jogadores where id_jogador = {id_jogador}")
            jogador = Jogador(df_jogador.id_jogador.values[0], df_jogador.nome_jogador.values[0], df_jogador.regiao.values[0])
            return jogador
    
    def validar_personagem(self, oracle:OracleQueries, id_personagem:int=None) -> Personagem:
        if self.ctrl_personagem.verificar_existencia_personagem(oracle, id_personagem):
            print(f"O personagem de ID {id_personagem} não existe.")
            return None
        else:
            oracle.connect()
            df_personagem = oracle.sqlToDataFrame(f"select from id_personagem, nome_personagem from personagens where id_personagem = {id_personagem}")
            personagem = Personagem(df_personagem.id_personagem.values[0], df_personagem.nome_personagem.values[0])
            return personagem