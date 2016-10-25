to-do:
- receber dados financeiros && gerar relatório financeiro
  - fazer form de data
  - fazer adição de dados pelo adm
    - ao salvar todos as taxas são salvas
    - nova tabela para "taxa"
      - um condomínio pode ter várias taxas
      - um apartamento pode ter várias taxas
  - adm editar dados
    - alguma forma de desabilitar dados (provavelmente gambi com 0)
  - adm visualizar relatório geral
  - morador visualizar relatório geral
  - morador visualizar relatório pessoal

iteração 4:
- colocar tudo em classe
	+ classe para model?
	+ classe para forms?
- fazer verificação do tipo de usuário na view para evitar problemas com link digitado
- uma função no model ou no view separada para quantidade de moradores de um apartamento
- edição morador e impacto na sua senha default
- permitir que um morador mude de apartamento
- requisitos do trello

melhoria prioridade baixa:
- fazer um usuário aprimorado com mais atributo
- não deixar que a senha default seja 'senhadefault' e melhorar lógica que verifica isso
- mudar autenticação para e-mail
- validações?
	- add validação para baixo no nro de apartamentos
	- add validação específica cpf
	- add validação específica cep
