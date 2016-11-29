to-do:
iteração 4:
  - adm editar dados financeiros
    - alguma forma de desabilitar dados (provavelmente gambi com 0)
- colocar tudo em classe
	+ classe para model?
	+ classe para forms?
- validar entrada do mês de uma maneira mais precisa. **é preciso fazer isso para a iteração 4??**
- fazer verificação do tipo de usuário na view para evitar problemas com link digitado. Talvez fazer uma função que verifica
- não ser igualitário na divisão das finanças para cada usuário e nem na inserção dos dados
- uma função no model ou no view separada para quantidade de moradores de um apartamento e para cálculo de taxas
- edição morador e impacto na sua senha default
- permitir que um morador mude de apartamento
- requisitos do trello

necessidades prioridade alta:
- multar reserva influenciar no finanças

bugs conhecidos:
- se tentar adicionar uma reserva que já existe, sistema não permite e continua na mesma tela. Se tentar salvar novamente uma reserva que já existe, agora ele irá salvar

melhoria prioridade baixa:
- fazer um usuário aprimorado com mais atributo
- não deixar que a senha default seja 'senhadefault' e melhorar lógica que verifica isso
- mudar autenticação para e-mail
- validações?
	- add validação para baixo no nro de apartamentos
	- add validação específica cpf
	- add validação específica cep
