from model.personagens import Personagem
from conexion.oracle_queries import OracleQueries

class Controller_Personagem:
    def __init__(self):
        pass

    def inserir_personagem(self) -> Personagem:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_personagem = int(input("Novo ID de personagem (numero inteiro positivo): "))
        while id_personagem < 1:
            id_personagem = int(input("Insira um numero inteiro positivo para o novo Id de personagem: "))
        
        if self.verificar_existencia_personagem(oracle, id_personagem):
            nome_personagem = input("Nome do novo personagem: ")

            oracle.write(f"insert into personagens values ({id_personagem}, '{nome_personagem}')")
            
            df_personagem = oracle.sqlToDataFrame(f"select id_personagem, nome_personagem from personagens where id_personagem = {id_personagem}")
            
            novo_personagem = Personagem(df_personagem.id_personagem.values[0], df_personagem.nome_personagem.values[0])
            
            novo_personagem.to_string()
            
            return novo_personagem
        else:
            print(f"O ID {id_personagem} já está cadastrado.")
            return None
    
    def atualizar_personagem(self) -> Personagem:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_personagem = int(input("Informe o ID do personagem que deseja atualizar: "))

        if not self.verificar_existencia_personagem(oracle, id_personagem):
            nome_personagem = input("Novo nome do personagem: ")

            oracle.write(f"update personagens set nome_personagem = '{nome_personagem}' where id_personagem = {id_personagem}")

            df_personagem = oracle.sqlToDataFrame(f"select id_personagem, nome_personagem from personagens where id_personagem = {id_personagem}")

            personagem_atualizado = Personagem(df_personagem.id_personagem.values[0], df_personagem.nome_personagem.values[0])

            personagem_atualizado.to_string()

            return personagem_atualizado
        else:
            print(f"O ID {id_personagem} não existe.")
            return None
        
    def excluir_personagem(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        id_personagem = int(input("Informe o ID do personagem que deseja excluir: "))

        if not self.verificar_existencia_personagem(oracle, id_personagem):
            df_personagem = oracle.sqlToDataFrame(f"select id_personagem, nome_personagem from personagens where id_personagem = {id_personagem}")

            oracle.write(f"delete from personagens where id_personagem = {id_personagem}")

            personagem_excluido = Personagem(df_personagem.id_personagem.values[0], df_personagem.nome_personagem.values[0])

            print("Personagem removido com sucesso!")
            print(personagem_excluido.to_string())
        else:
            print(f"O ID {id_personagem} não existe.")
            return None 
    
    def verificar_existencia_personagem(self, oracle:OracleQueries, id_personagem:int=None) -> bool:
        df_personagem = oracle.sqlToDataFrame(f"select id_personagem, nome_personagem from personagens where id_personagem = {id_personagem}")
        return df_personagem.empty