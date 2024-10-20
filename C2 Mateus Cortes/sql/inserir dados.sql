insert into jogadores(id_jogador, nome_jogador, regiao) values(50000, 'joão', 'america do sul');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50001, 'jack', 'america do norte');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50002, 'gabriel', 'america do sul');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50003, 'vladmir', 'europa');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50004, 'friedrich', 'europa');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50005, 'karl', 'europa');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50006, 'joseph', 'europa');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50007, 'ernesto', 'america do sul');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50008, 'john', 'america do norte');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50009, 'mao', 'asia');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50010, 'hideo', 'asia');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50011, 'mohammad', 'oriente medio');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50012, 'ahmed', 'oriente medio');
insert into jogadores(id_jogador, nome_jogador, regiao) values(50013, 'raúl', 'america central');

insert into personagens(id_personagem, nome_personagem) values(00, 'goku');
insert into personagens(id_personagem, nome_personagem) values(01, 'vegeta');
insert into personagens(id_personagem, nome_personagem) values(02, 'gohan');
insert into personagens(id_personagem, nome_personagem) values(03, 'piccolo');
insert into personagens(id_personagem, nome_personagem) values(04, 'kuririn');
insert into personagens(id_personagem, nome_personagem) values(05, 'freeza');
insert into personagens(id_personagem, nome_personagem) values(06, 'cell');
insert into personagens(id_personagem, nome_personagem) values(07, 'majin buu');
insert into personagens(id_personagem, nome_personagem) values(08, 'super buu');
insert into personagens(id_personagem, nome_personagem) values(09, 'broly');

insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(000, 50000, 00, 1300);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(001, 50000, 05, 1000);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(002, 50001, 04, 1200);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(003, 50002, 05, 1350);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(004, 50002, 01, 1250);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(005, 50003, 00, 1800);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(006, 50003, 02, 1300);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(007, 50004, 03, 1700);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(008, 50005, 09, 1400);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(009, 50005, 07, 1100);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(010, 50006, 08, 2000);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(011, 50007, 06, 1750);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(012, 50007, 02, 1050);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(013, 50008, 01, 1000);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(014, 50009, 00, 1800);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(015, 50009, 04, 1400);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(016, 50010, 01, 1150);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(017, 50010, 00, 1050);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(018, 50011, 09, 1600);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(019, 50011, 02, 1000);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(020, 50012, 06, 1400);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(021, 50013, 01, 1300);
insert into jogadores_personagens(id_classificacao, id_jogador, id_personagem, pontuacao) values(022, 50013, 09, 1100);

commit;