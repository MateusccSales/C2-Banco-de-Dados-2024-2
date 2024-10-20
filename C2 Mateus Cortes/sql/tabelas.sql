drop table jogadores_personagens;

drop table personagens;

drop table jogadores;

create table jogadores(
    id_jogador number not null,
    nome_jogador varchar2(100) not null,
    regiao varchar2(100) not null
    );

create table personagens(
    id_personagem number not null,
    nome_personagem varchar2(100) not null
    );

create table jogadores_personagens(
    id_classificacao number not null,
    id_jogador number not null, 
    id_personagem number not null, 
    pontuacao number(4) not null
    );

drop view classificacao_mundial;

create or replace view classificacao_mundial as(
    select jogadores.id_jogador as id,
        jogadores.nome_jogador as jogador, 
        jogadores.regiao as regiao, 
        personagens.nome_personagem as personagem, 
        jogadores_personagens.pontuacao as pontuacao
    from jogadores
    inner join jogadores_personagens
    on jogadores.id_jogador = jogadores_personagens.id_jogador
    inner join personagens
    on jogadores_personagens.id_personagem = personagens.id_personagem
    );

alter table jogadores add primary key(id_jogador);

alter table personagens add primary key(id_personagem);

alter table jogadores_personagens add primary key(id_classificacao);



alter table jogadores_personagens add constraint id_jogador_fk foreign key(id_jogador) references jogadores(id_jogador);

alter table jogadores_personagens add constraint id_personagens_fk foreign key(id_personagem) references personagens(id_personagem);



drop index nome_jogador_idx;

drop index nome_personagem_idx;

create index nome_jogador_idx on jogadores(nome_jogador);

create index nome_personagem_idx on personagens(nome_personagem);