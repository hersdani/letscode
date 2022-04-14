USE faculdade;

-- 2.a. Relatório com dados dos alunos matriculados em todos os cursos oferecidos.
SELECT a.nome Nome, a.cpf CPF, a.endereco Endereço, a.telefone Telefone, a.data_nasc Data_Nascimento, c.nome Curso FROM aluno a
INNER JOIN matricula m ON a.CPF = m.cpf_aluno
INNER JOIN curso c ON c.codigo = m.codigo_curso
ORDER BY a.nome ASC;

-- 2.b. Relatório com dados de todos os cursos, com suas respectivas disciplinas sendo oferecidas.
SELECT c.nome Curso, c.descricao Descrição_Curso, c.codigo Codigo_Curso, c.cod_dpto Cód_Dep_Curso, d.nome Nome_Disciplina, d.codigo Código_Disciplina FROM curso c
INNER JOIN compoe co ON c.codigo = co.codigo_curso
INNER JOIN disciplina d ON d.codigo = co.cod_disciplina
ORDER BY c.nome ASC;

-- 2.c. Relatório com nome dos alunos e as disciplinas em que estão matriculados.
SELECT a.nome Nome_Aluno, a.cpf CPF, d.nome Disciplina, d.codigo Código_Disciplina FROM aluno a
INNER JOIN cursa c ON c.cpf_aluno = a.cpf
INNER JOIN disciplina d ON d.codigo = c.cod_disciplina
ORDER BY a.nome ASC;

-- 2.d. Relatório com os dados dos professores e as disciplinas que ministram.
SELECT p.nome Nome_Professor, d.nome Disciplina, d.codigo Código_Disc FROM professor p
INNER JOIN disciplina d ON d.matricula_prof	 = p.matricula
ORDER BY p.nome ASC;

-- 2.e. Relatório com nomes das disciplinas e seus pré-requisitos.
SELECT d.nome Disciplina, d.codigo Cod_Disciplina, pr.codigo_disc_dependencia Pré_Requisito FROM disciplina d
INNER JOIN pre_req pr ON d.codigo = pr.codigo_disc
ORDER BY d.nome;

-- 2.f. Relatório com média de idade dos alunos matriculados em cada curso.
SELECT cu.nome, FLOOR(AVG(DATEDIFF(CURRENT_DATE(), a.data_nasc) / 365)) AS 'Idade_Média' FROM aluno a
INNER JOIN matricula ma ON ma.cpf_aluno = a.cpf
INNER JOIN curso cu ON cu.codigo = ma.codigo_curso
GROUP BY cu.nome
ORDER BY cu.nome ASC;

-- 2.g. Relatório com cursos oferecidos por cada departamento.
SELECT d.nome Departamento, d.codigo Código_Depto, c.nome Nome_Curso, c.codigo Código_Curso FROM curso c
INNER JOIN departamento d ON d.codigo = c.cod_dpto
ORDER BY d.nome;
