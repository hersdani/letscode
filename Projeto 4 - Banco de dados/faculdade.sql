CREATE DATABASE faculdade;

USE faculdade;

CREATE TABLE aluno(
id SERIAL,
cpf CHAR(11) PRIMARY KEY NOT NULL,
nome VARCHAR(100) NOT NULL,
endereco VARCHAR(100) NOT NULL,
telefone VARCHAR(11) NOT NULL,
data_nasc DATE NOT NULL
);

CREATE TABLE departamento(
id SERIAL,
codigo CHAR(5) PRIMARY KEY NOT NULL,
nome VARCHAR(100) NOT NULL
);

CREATE TABLE curso(
id SERIAL,
codigo CHAR(6) PRIMARY KEY NOT NULL,
nome VARCHAR(30) NOT NULL,
descricao VARCHAR(100),
cod_dpto CHAR(5) NOT NULL,
FOREIGN KEY (cod_dpto) REFERENCES departamento (codigo)
);

CREATE TABLE matricula (
id SERIAL,
codigo_curso CHAR(6) NOT NULL,
CONSTRAINT PK_matricula PRIMARY KEY (codigo_curso, cpf_aluno), 
FOREIGN KEY (codigo_curso) REFERENCES curso (codigo),
cpf_aluno CHAR(11) NOT NULL,
FOREIGN KEY (cpf_aluno) REFERENCES aluno (cpf),
data_matricula DATE NOT NULL
);

CREATE TABLE professor(
id SERIAL,
matricula CHAR(5) PRIMARY KEY NOT NULL,
nome VARCHAR(100) NOT NULL,
endereco VARCHAR(100),
telefone VARCHAR(11),
data_nasc DATE,
cod_depto CHAR(5) NOT NULL,
FOREIGN KEY (cod_depto) REFERENCES departamento (codigo),
data_contratacao DATE NOT NULL
);

CREATE TABLE disciplina(
id SERIAL,
codigo CHAR(6) PRIMARY KEY NOT NULL,
nome VARCHAR(50),
qtde_creditos CHAR(2) NOT NULL,
matricula_prof CHAR(5) NOT NULL,
FOREIGN KEY (matricula_prof) REFERENCES professor (matricula)
);

CREATE TABLE cursa(
id SERIAL,
cpf_aluno CHAR(11) NOT NULL,
FOREIGN KEY (cpf_aluno) REFERENCES aluno (cpf),
cod_disciplina CHAR(6) NOT NULL,
FOREIGN KEY (cod_disciplina) REFERENCES disciplina (codigo)
);

CREATE TABLE compoe(
id SERIAL,
codigo_curso CHAR(6) NOT NULL,
FOREIGN KEY (codigo_curso) REFERENCES curso (codigo),
cod_disciplina CHAR(6) NOT NULL,
FOREIGN KEY (cod_disciplina) REFERENCES disciplina (codigo)
);

CREATE TABLE pre_req(
id SERIAL,
codigo_disc CHAR(6) NOT NULL,
FOREIGN KEY (codigo_disc) REFERENCES disciplina (codigo),
codigo_disc_dependencia CHAR(6),
FOREIGN KEY (codigo_disc_dependencia) REFERENCES disciplina (codigo)
);

INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("11122233345", "José das Couves", "Rua das Pedras, S/N - Pasargada", "39999900000", "2005-03-16");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("22233344456", "João de Barro", "Avenida das Minhocas, 987 - Barreiras", "39991190901", "2004-12-29");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("33344455565", "Antonio Pike", "Boulevard da Galáxia, 99 - Via Láctea", "39990091910", "2006-02-01");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("44355466501", "João das Neves", "Rua do Castelo Antigo, 1600 - Muro do Norte", "39912132700", "2001-05-07");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("34351267098", "Lucas de Caminha", "Avenida das Estrelas, 9999 - Localonge", "39989290521", "2008-04-01");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("35342176980", "Danielle Amada", "Avenida do Amor, 16 - Rio Infinito", "38989889123", "2003-06-11");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("39358262097", "João Sem Braço", "Rua dos Olhos, 10 - Copachata", "39929900239", "2007-08-21");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("02328127742", "Monalisa di Caprio", "Rua das Artistas, 100 - Artegrande", "39912322427", "2008-06-01");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("05312200198", "Marcos Cascadura", "Rua dos Pedregulhos, 12 - Conde Real", "39914515531", "2003-08-11");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("06432200198", "Luiza do Canadá", "Estrada de Neve, 44 - Jardim de Cima", "39929491522", "2003-08-11");
INSERT INTO aluno (cpf, nome, endereco, telefone, data_nasc) VALUES ("07221199223", "Gabriela Bombrilho", "Rua Pedro Flores, 286 - Cascamole", "39900193598", "2003-08-11");

INSERT INTO departamento (codigo, nome) VALUES ("DENQU", "Departamento de Engenharia Química");
INSERT INTO departamento (codigo, nome) VALUES ("DENBI", "Departamento de Engenharia de Bioprocessos");
INSERT INTO departamento (codigo, nome) VALUES ("INMAT", "Instituto de Matemática e Cálculo Numérico");
INSERT INTO departamento (codigo, nome) VALUES ("INSFI", "Instituto de Física");

INSERT INTO curso (codigo, nome, descricao, cod_dpto) VALUES ("ENGQUI", "Engenharia Química", "Graduação em Engenharia Química", "DENQU");
INSERT INTO curso (codigo, nome, descricao, cod_dpto) VALUES ("ENGBIO", "Engenharia de Bioprocessos", "Graduação em Engenharia de Bioprocessos", "DENBI");
INSERT INTO curso (codigo, nome, descricao, cod_dpto) VALUES ("MATPEA", "Matemática Pura e Aplicada", "Licenciatura em Matemática", "INMAT");
INSERT INTO curso (codigo, nome, descricao, cod_dpto) VALUES ("FMQUAN", "Física e Mecânica Quântica", "Bacharel Em Física e Mecânica Quântica", "INMAT");
INSERT INTO curso (codigo, nome, descricao, cod_dpto) VALUES ("QUIMIN", "Química Industrial", "Tecnólogo em Química Industrial", "DENQU");

INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("ENGQUI", "11122233345", "2022-02-15");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("ENGBIO", "22233344456", "2022-02-02");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("FMQUAN", "33344455565", "2022-03-03");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("FMQUAN", "34351267098", "2022-01-24");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("MATPEA", "39358262097", "2022-03-12");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("QUIMIN", "44355466501", "2022-02-14");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("ENGBIO", "35342176980", "2022-01-29");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("ENGQUI", "02328127742", "2021-09-29");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("MATPEA", "05312200198", "2020-12-13");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("QUIMIN", "06432200198", "2020-09-06");
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES ("FMQUAN", "07221199223", "2019-12-22");

INSERT INTO professor (matricula, nome, endereco, telefone, data_nasc, cod_depto, data_contratacao) VALUES ("20123", "Marcos", "Rua 1, 22", "12345678901", "1988-12-12", "DENQU", "2000-01-02");
INSERT INTO professor (matricula, nome, endereco, telefone, data_nasc, cod_depto, data_contratacao) VALUES ("10211", "Rogério", "Rua 2, 11", "98765432101", "1977-08-12", "INMAT", "1998-02-01");
INSERT INTO professor (matricula, nome, endereco, telefone, data_nasc, cod_depto, data_contratacao) VALUES ("01245", "Carlos", "Rua 3, 33", "12332210022", "1964-04-22", "INSFI", "1995-06-11");
INSERT INTO professor (matricula, nome, endereco, telefone, data_nasc, cod_depto, data_contratacao) VALUES ("31181", "Ney", "Rua 4, 24", "21999151902", "1964-04-22", "DENBI", "2002-03-21");

INSERT INTO disciplina (codigo, nome, qtde_creditos, matricula_prof) VALUES ("MAC101", "Cálculo I", "06", "01245");
INSERT INTO disciplina (codigo, nome, qtde_creditos, matricula_prof) VALUES ("FIM101", "Física I", "04", "20123");
INSERT INTO disciplina (codigo, nome, qtde_creditos, matricula_prof) VALUES ("MAC201", "Cálculo II", "04", "01245");
INSERT INTO disciplina (codigo, nome, qtde_creditos, matricula_prof) VALUES ("BIO101", "Bioquímica", "04", "31181");
INSERT INTO disciplina (codigo, nome, qtde_creditos, matricula_prof) VALUES ("EPR999", "Engenharia de Processos", "04", "10211");
INSERT INTO disciplina (codigo, nome, qtde_creditos, matricula_prof) VALUES ("MEQ101", "Mecânica Quântica", "06", "20123");

INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("11122233345", "MAC101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("22233344456", "MAC101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("33344455565", "MAC101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("44355466501", "MAC101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("34351267098", "MAC201");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("35342176980", "MAC201");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("33344455565", "MEQ101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("11122233345", "BIO101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("22233344456", "BIO101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("35342176980", "BIO101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("07221199223", "FIM101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("35342176980", "FIM101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("22233344456", "FIM101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("35342176980", "EPR999");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("39358262097", "EPR999");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("39358262097", "BIO101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("02328127742", "EPR999");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("02328127742", "MAC201");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("05312200198", "MAC201");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("05312200198", "BIO101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("06432200198", "BIO101");
INSERT INTO cursa (cpf_aluno, cod_disciplina) VALUES ("07221199223", "MAC101");

INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("ENGQUI", "MAC101");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("ENGQUI", "MAC201");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("ENGQUI", "FIM101");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("ENGQUI", "EPR999");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("ENGBIO", "MAC101");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("ENGBIO", "MAC201");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("ENGBIO", "BIO101");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("MATPEA", "MAC101");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("MATPEA", "MAC201");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("FMQUAN", "FIM101");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("FMQUAN", "MEQ101");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("QUIMIN", "MAC101");
INSERT INTO compoe (codigo_curso, cod_disciplina) VALUES ("QUIMIN", "EPR999");

INSERT INTO pre_req (codigo_disc, codigo_disc_dependencia) VALUES ("MAC201", "MAC101");
INSERT INTO pre_req (codigo_disc, codigo_disc_dependencia) VALUES ("FIM101", "MAC101");
INSERT INTO pre_req (codigo_disc, codigo_disc_dependencia) VALUES ("MEQ101", "FIM101");
