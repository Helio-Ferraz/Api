# Api
Flask: microframework web que cria rotas HTTP de forma simples.

Rota/endpoint: caminho + método (ex.: GET /tarefas). Cada função com @app.get/post/put… responde a esse endpoint.

Métodos HTTP:

GET: ler dados (sem efeitos colaterais).

POST: criar novo recurso.

PUT: atualizar recurso por completo (idempotente).

PATCH: atualizar parcialmente.

DELETE: remover recurso.

Recurso: entidade manipulada pela API (aqui, “tarefa”). Geralmente exposto em plural ("/tarefas").

JSON: formato de troca de dados; usamos request.get_json() para ler e jsonify() para responder com cabeçalhos corretos.

Status HTTP: números que indicam o resultado. Exemplos: 200 (OK), 201 (Criado), 400 (Requisição inválida), 404 (Não encontrado), 204 (Sem conteúdo).
=-------------------------------------=
Ao usar "def", você cria uma função que pode receber parâmetros, executar instruções e retornar um resultado.
-------------------------------

Tabela: conjunto de dados sobre o mesmo tema

Registro: cada linha da tabela (exemplo: uma pessoa)

Campo/Atributo: cada coluna da tabela (exemplo: nome, email)

Chave primária: campo que identifica cada registro de forma única (como CPF)

Chave estrangeira: campo que se conecta a outra tabela (relações)

SQL: linguagem para criar, buscar, atualizar e apagar dados no banco

