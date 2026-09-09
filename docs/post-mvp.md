# Pós-MVP — Waves

## 1. Objetivo

Este documento registra funcionalidades e evoluções que fazem sentido
para o sistema Waves, mas que não são necessárias para colocar a
primeira versão operacional em funcionamento.

Esses itens não devem bloquear o desenvolvimento ou o lançamento do MVP.

O Aplicativo Mobile do Cliente faz parte do MVP e, portanto, não deve
ser tratado como uma funcionalidade pós-MVP.

---

# 2. Regra para classificação

Uma funcionalidade deve ser classificada como pós-MVP quando:

- não for necessária para completar o fluxo operacional principal;
- puder ser adicionada posteriormente sem impedir a operação;
- representar uma evolução, automação ou otimização;
- aumentar a complexidade da primeira entrega sem ser essencial;
- depender de dados que o próprio MVP ainda começará a gerar.

Uma funcionalidade já definida como necessária no `mvp.md` não deve ser
movida para pós-MVP apenas porque sua implementação é complexa.

---

# 3. Funcionalidades pós-MVP

## 3.1 IA avançada de atendimento

O MVP poderá possuir as funções básicas de atendimento previstas para
o WhatsApp.

Funcionalidades mais avançadas de inteligência artificial ficam para
uma etapa posterior.

Possíveis evoluções incluem:

- interpretação de perguntas mais complexas;
- atendimento com maior contexto;
- utilização do histórico do cliente durante a conversa;
- automações mais sofisticadas;
- integração da IA com processos comerciais.

Os detalhes deverão ser definidos quando essa evolução for planejada.

---

## 3.2 Campanhas de retenção

O MVP deverá gerar a informação necessária para identificar clientes:

- ativos;
- em risco;
- inativos.

A execução automática de campanhas de retenção não faz parte do MVP.

No futuro, o sistema poderá utilizar essa segmentação para apoiar
ações direcionadas aos clientes.

Exemplos de possibilidades futuras:

- campanhas para clientes em risco;
- campanhas para clientes inativos;
- comunicação com clientes recorrentes;
- ações baseadas no tempo desde a última compra.

As regras, canais e conteúdo dessas campanhas ainda deverão ser
definidos.

---

## 3.3 Programa de fidelidade

Programa de pontos, recompensas ou benefícios por recorrência não
faz parte do MVP.

Uma versão futura poderá incluir mecanismos de fidelização.

Antes da implementação deverão ser definidas regras como:

- como benefícios são adquiridos;
- validade;
- formas de utilização;
- condições de elegibilidade;
- impacto financeiro.

Nenhuma dessas regras deverá ser presumida durante o MVP.

---

## 3.4 Promoções sofisticadas

O MVP trabalhará com o funcionamento básico dos produtos e seus
respectivos preços.

Um mecanismo avançado de promoções deverá ser tratado posteriormente.

Possíveis evoluções poderão envolver:

- promoções programadas;
- regras condicionais;
- descontos automáticos;
- campanhas específicas.

As regras exatas ainda não estão definidas e não fazem parte da
primeira entrega.

---

## 3.5 Automações não essenciais

Automações que não sejam necessárias para executar a operação
principal não deverão ser implementadas durante o MVP.

Elas poderão ser avaliadas posteriormente conforme forem identificadas
tarefas repetitivas na operação real.

A prioridade inicial é garantir que os processos fundamentais
funcionem corretamente antes de automatizar processos adicionais.

---

# 4. Funcionalidades que NÃO devem ser classificadas como pós-MVP

Alguns assuntos ainda não possuem definição completa, mas isso não
significa que ficaram para depois do MVP.

Eles devem permanecer registrados em `open-questions.md`.

Exemplos relacionados ao backend e à operação:

- parceiro/API de entrega a ser utilizado;
- momento exato da baixa de estoque;
- comportamento de estoque em cancelamentos;
- possibilidade ou não de estoque negativo;
- regra exata de cancelamento;
- obrigatoriedade de CPF;
- limite de tempo considerado atraso na cozinha;
- relação entre pagamento aprovado e confirmação do pedido.

Exemplos relacionados ao Aplicativo Mobile:

- tecnologia utilizada para desenvolvimento do aplicativo;
- plataformas suportadas inicialmente;
- forma de cadastro e autenticação do cliente;
- recuperação de acesso;
- campos e regras de endereço de entrega;
- possibilidade de retirada no local;
- formas de pagamento;
- provedor de pagamento;
- comportamento quando o pagamento falhar;
- estratégia de atualização do status do pedido;
- uso ou não de notificações push;
- disponibilização do rastreamento dentro do aplicativo;
- regras para cancelamento pelo cliente.

Esses pontos precisam ser decididos para implementar corretamente
funcionalidades que já pertencem ao MVP.

Uma decisão ainda aberta não deve ser movida automaticamente para
pós-MVP. Primeiro deve ser registrada, discutida e aprovada.

---

# 5. Regra de proteção do escopo

Durante o desenvolvimento do MVP, novas ideias deverão seguir o
seguinte processo:

1. Registrar a ideia.
2. Verificar se ela é necessária para completar o fluxo principal.
3. Verificar se ela já está prevista no `mvp.md`.
4. Se for necessária, avaliar seu impacto no MVP.
5. Se não for necessária, avaliar se deve ser registrada neste documento.
6. Não iniciar o desenvolvimento sem aprovação do responsável pelo
   projeto.

O surgimento de uma nova ideia não significa automaticamente que ela
deve entrar na primeira versão.

Da mesma forma, uma dificuldade técnica não é motivo suficiente para
retirar do MVP uma funcionalidade já aprovada.

---

# 6. Lista atual do pós-MVP

| Funcionalidade | Status |
|---|---|
| IA avançada de atendimento | Pós-MVP |
| Campanhas de retenção | Pós-MVP |
| Programa de fidelidade | Pós-MVP |
| Promoções sofisticadas | Pós-MVP |
| Automações não essenciais | Pós-MVP |

---

# 7. Relação com o Aplicativo Mobile

O Aplicativo Mobile do Cliente está explicitamente incluído no MVP.

Portanto, fazem parte da primeira versão, conforme definido em
`mvp.md`, as capacidades mínimas necessárias para:

- identificar ou cadastrar o cliente;
- consultar o cardápio;
- consultar a disponibilidade dos produtos;
- montar o pedido;
- informar os dados necessários para o pedido;
- realizar ou iniciar o processo de pagamento;
- enviar o pedido ao backend;
- acompanhar o estado do pedido;
- acessar os recursos de acompanhamento da entrega definidos para o MVP;
- consultar o histórico básico de pedidos.

Funcionalidades futuras do aplicativo só deverão ser classificadas
como pós-MVP quando forem explicitamente propostas, avaliadas e
aprovadas.

Não deverão ser adicionadas a este documento apenas por suposição.

---

# 8. Observação

Este documento é uma lista viva.

Novas funcionalidades poderão ser adicionadas conforme o sistema for
desenvolvido, desde que sejam claramente separadas do escopo aprovado
do MVP.

Qualquer item movido entre MVP e pós-MVP deverá ser aprovado pelo
responsável pelo projeto e registrado na documentação.

Em caso de conflito entre este documento e `mvp.md` sobre o que faz
parte da primeira versão, o escopo aprovado no `mvp.md` deverá ser
revisado antes de qualquer alteração de desenvolvimento.