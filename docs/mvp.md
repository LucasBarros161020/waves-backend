# MVP — Waves

## 1. Objetivo

Definir o conjunto mínimo de funcionalidades necessário para que a
operação principal da Waves possa funcionar de ponta a ponta dentro
do sistema.

O MVP deve permitir que um cliente realize um pedido pelo Aplicativo
Mobile da Waves, que esse pedido seja recebido pelo backend, processado
pela cozinha, despachado, entregue e registrado, mantendo estoque,
cliente e indicadores básicos atualizados.

Também deverá ser possível registrar pedidos manualmente pelo
atendimento, utilizando o mesmo fluxo operacional.

---

## 2. Princípio do MVP

Uma funcionalidade faz parte do MVP quando é necessária para que o
fluxo operacional principal da Waves funcione sem depender de
planilhas ou controles paralelos.

O fluxo principal é:

Cliente
→ Aplicativo Mobile
→ Backend Waves
→ Pedido
→ Confirmação
→ Cozinha
→ Expedição
→ Entrega
→ Finalização

Também deverá existir o fluxo alternativo:

Cliente
→ Atendimento
→ Backend Waves
→ Pedido
→ Confirmação
→ Cozinha
→ Expedição
→ Entrega
→ Finalização

Estoque, cardápio, clientes e gestão devem acompanhar esses fluxos.

---

# 3. Funcionalidades incluídas no MVP

## 3.1 Usuários e perfis de acesso

O sistema deve possuir usuários internos com diferentes níveis de
acesso.

Perfis necessários:

- Administrador
- Gestor
- Cozinha
- Expedição
- Atendimento
- Estoque

Cada perfil deverá visualizar ou executar apenas as funcionalidades
relacionadas à sua função.

---

## 3.2 Clientes

O sistema deve permitir:

- cadastrar clientes;
- identificar o cliente pelo CPF;
- consultar os dados do cliente;
- manter o histórico de pedidos;
- reconhecer um cliente em compras futuras;
- classificar clientes conforme o tempo desde a última compra.

Segmentações iniciais:

- Ativo: comprou nos últimos 30 dias;
- Em risco: entre 31 e 60 dias sem comprar;
- Inativo: mais de 60 dias sem comprar.

A forma de autenticação do cliente no Aplicativo Mobile será definida
posteriormente nas regras de negócio e decisões técnicas.

---

## 3.3 Ingredientes

O sistema deve permitir:

- cadastrar ingredientes;
- editar ingredientes;
- consultar ingredientes;
- definir unidade de medida;
- informar quantidade disponível;
- definir estoque mínimo;
- consultar ingredientes abaixo do estoque mínimo.

Exemplos:

- pão;
- hambúrguer;
- queijo;
- bacon;
- molho;
- embalagem.

---

## 3.4 Produtos

O sistema deve permitir:

- cadastrar produtos;
- editar produtos;
- definir nome;
- descrição;
- preço;
- imagem;
- status;
- consultar produtos disponíveis.

Exemplos:

- X-Burger;
- X-Salada;
- X-Tudo.

---

## 3.5 Receitas / fichas técnicas

Cada produto deverá possuir uma receita que determine quais
ingredientes são utilizados e em qual quantidade.

Exemplo:

X-Tudo

- 1 pão
- 1 hambúrguer
- 2 fatias de queijo
- 30 g de bacon
- 20 g de molho

A receita será utilizada pelo sistema para calcular disponibilidade,
consumo de estoque e custo de produção.

---

## 3.6 Disponibilidade automática do cardápio

O sistema deverá calcular automaticamente quantas unidades de cada
produto ainda podem ser produzidas considerando os ingredientes
disponíveis.

A quantidade disponível será determinada pelo ingrediente que
permitir produzir a menor quantidade de unidades.

Quando não houver ingredientes suficientes para produzir uma unidade,
o produto deverá ficar indisponível para venda.

Essa disponibilidade deverá ser refletida no cardápio apresentado ao
cliente no Aplicativo Mobile.

---

## 3.7 Estoque

O sistema deverá controlar o estoque dos ingredientes.

Deverá registrar movimentações decorrentes de:

- compras;
- vendas;
- desperdícios;
- ajustes autorizados.

O estoque deve ser atualizado automaticamente conforme essas
movimentações.

---

## 3.8 Estoque mínimo

Cada ingrediente deverá possuir uma quantidade mínima configurável.

Quando a quantidade disponível ficar abaixo desse limite, o sistema
deverá sinalizar o ingrediente.

---

## 3.9 Compras de ingredientes

O sistema deve permitir registrar compras de ingredientes.

Uma compra deverá:

- identificar os ingredientes adquiridos;
- registrar quantidades;
- registrar valores;
- aumentar o estoque;
- contribuir para o cálculo do custo médio do ingrediente.

---

## 3.10 Fornecedores

O MVP deverá permitir manter as informações básicas dos fornecedores
necessárias para registrar compras.

Informações mínimas:

- nome;
- identificação;
- contato;
- status.

Os detalhes exatos serão definidos posteriormente caso o Guia não
determine todos os campos necessários.

---

## 3.11 Custo médio

Ao registrar novas compras, o sistema deverá recalcular o custo médio
dos ingredientes.

Esse custo será utilizado para estimar o custo atual de produção dos
produtos.

---

## 3.12 Custo de produção

O sistema deverá ser capaz de calcular o custo aproximado de produção
de um produto considerando:

- sua receita;
- quantidade utilizada de cada ingrediente;
- custo médio atual dos ingredientes.

---

## 3.13 Desperdício

A cozinha deverá poder registrar desperdícios de ingredientes.

O registro deverá provocar a correspondente redução do estoque.

Informações adicionais, como motivo obrigatório, serão definidas nas
regras de negócio posteriormente.

---

# 4. Aplicativo Mobile do Cliente

## 4.1 Objetivo

O MVP deverá possuir um Aplicativo Mobile utilizado pelos clientes
para realizar pedidos diretamente à Waves.

O aplicativo será um dos principais canais de entrada de pedidos no
sistema e deverá consumir as informações e regras fornecidas pelo
backend da Waves.

---

## 4.2 Identificação do cliente

O aplicativo deverá permitir que o cliente seja identificado para
realizar pedidos.

O cadastro e a identificação deverão estar vinculados ao cadastro
central de clientes da Waves.

A estratégia exata de autenticação, login, sessão e recuperação de
acesso ainda deverá ser definida.

---

## 4.3 Visualização do cardápio

O aplicativo deverá permitir ao cliente visualizar o cardápio da
Waves.

Cada produto deverá apresentar, quando aplicável:

- imagem;
- nome;
- descrição;
- preço;
- disponibilidade.

A disponibilidade apresentada deverá ser determinada pelo backend com
base nas regras de produto, receita e estoque.

---

## 4.4 Produtos indisponíveis

Quando um produto não puder ser produzido por falta de ingredientes,
ele não deverá ser vendável pelo aplicativo.

A forma visual de ocultar, desabilitar ou sinalizar o produto será
definida durante o desenvolvimento da interface.

---

## 4.5 Montagem do pedido

O aplicativo deverá permitir:

- selecionar produtos;
- definir quantidades;
- adicionar observações ao item quando aplicável;
- adicionar itens ao pedido;
- remover itens;
- revisar os itens selecionados;
- visualizar o valor do pedido antes da confirmação.

---

## 4.6 Dados necessários para o pedido

Antes da confirmação, o aplicativo deverá obter os dados necessários
para que o pedido possa ser processado e entregue.

Os campos exatos, incluindo regras de endereço e dados adicionais,
serão definidos posteriormente.

---

## 4.7 Pagamento

O Aplicativo Mobile deverá permitir que o cliente realize ou inicie o
processo de pagamento necessário para o pedido.

O meio de pagamento, provedor, formas aceitas e comportamento em caso
de falha ainda deverão ser definidos.

O backend será responsável por validar o estado do pagamento necessário
para que o pedido possa avançar no fluxo operacional.

---

## 4.8 Envio do pedido

Após a confirmação pelo cliente, o aplicativo deverá enviar o pedido
ao backend da Waves.

O backend deverá realizar as validações necessárias antes de aceitar o
pedido, incluindo disponibilidade e informações obrigatórias.

Quando aceito, o pedido deverá entrar no estado:

Recebido.

---

## 4.9 Acompanhamento do pedido

O aplicativo deverá permitir que o cliente consulte o estado atual do
pedido após sua criação.

Os estados operacionais são:

1. Recebido
2. Confirmado
3. Em preparo
4. Pronto para despacho
5. Motoboy a caminho
6. Saiu para entrega
7. Entregue

A forma de atualização em tempo real ou periódica será definida na
arquitetura técnica.

---

## 4.10 Rastreamento da entrega

Quando existir um link de rastreamento fornecido pelo parceiro de
entrega, o pedido deverá manter essa informação disponível.

O cliente deverá poder receber ou acessar esse rastreamento conforme
os canais definidos para a operação.

O Guia prevê o envio do link pelo WhatsApp. A disponibilização também
dentro do Aplicativo Mobile poderá ser implementada no MVP caso seja
confirmada como requisito operacional.

---

## 4.11 Histórico de pedidos no aplicativo

O aplicativo deverá permitir ao cliente consultar seus pedidos
anteriores vinculados ao cadastro central.

O nível de detalhe apresentado no histórico será definido durante o
desenvolvimento da interface.

---

## 4.12 Regra de integração com o backend

O Aplicativo Mobile não deverá manter cópias independentes das regras
de negócio centrais.

Regras como:

- disponibilidade dos produtos;
- preços válidos;
- estoque;
- criação do pedido;
- estado do pedido;
- identificação do cliente;
- pagamento;
- entrega;

deverão ser fornecidas ou validadas pelo backend da Waves.

O aplicativo atuará como cliente da API.

---

## 4.13 Fluxo mínimo do Aplicativo Mobile

O cliente deverá conseguir executar o seguinte fluxo:

1. Abrir o aplicativo.
2. Identificar-se ou cadastrar-se.
3. Visualizar o cardápio disponível.
4. Consultar os produtos.
5. Selecionar produtos.
6. Definir quantidades e observações.
7. Revisar o pedido.
8. Informar os dados necessários para entrega.
9. Realizar ou iniciar o pagamento.
10. Confirmar o pedido.
11. Enviar o pedido ao backend.
12. Consultar o andamento do pedido.
13. Acompanhar a entrega pelos canais disponibilizados.
14. Visualizar a conclusão do pedido.

---

# 5. Pedidos

## 5.1 Criação de pedidos

O sistema deverá permitir receber pedidos originados do Aplicativo
Mobile e também pedidos inseridos manualmente pelo atendimento.

Todos os pedidos deverão utilizar o mesmo fluxo operacional após serem
aceitos pelo backend.

Um pedido deverá registrar pelo menos:

- cliente;
- produtos;
- quantidades;
- valores;
- observações;
- origem;
- data e hora;
- situação atual.

---

## 5.2 Origem do pedido

O sistema deverá registrar a origem do pedido.

No MVP, deverão existir pelo menos as seguintes origens:

- Aplicativo Mobile;
- Atendimento manual.

Essa informação deverá permitir identificar por qual canal cada pedido
foi criado.

---

## 5.3 Itens do pedido

Cada pedido deverá possuir um ou mais itens.

Cada item deverá registrar:

- produto;
- quantidade;
- preço considerado na venda;
- observações relevantes.

O histórico do pedido não deverá depender de alterações futuras no
preço atual do produto.

---

## 5.4 Fluxo de estados

O pedido deverá seguir o fluxo operacional definido pela Waves:

1. Recebido
2. Confirmado
3. Em preparo
4. Pronto para despacho
5. Motoboy a caminho
6. Saiu para entrega
7. Entregue

O sistema deverá registrar a situação atual do pedido.

---

## 5.5 Histórico de estados

As mudanças de estado de um pedido deverão ser registradas para
permitir reconstruir sua jornada.

Isso deverá possibilitar posteriormente calcular tempos como:

- espera para confirmação;
- tempo de preparo;
- tempo aguardando despacho;
- tempo de entrega;
- tempo total do pedido.

---

## 5.6 Confirmação do pedido

O sistema deverá permitir que um pedido recebido seja confirmado
quando estiver apto a seguir para a cozinha.

A relação exata entre confirmação do pedido e aprovação do pagamento
será definida nas regras de negócio.

---

# 6. Cozinha / KDS

## 6.1 Fila da cozinha

Pedidos confirmados deverão aparecer na tela da cozinha.

A fila deverá apresentar:

- pedidos;
- itens;
- quantidades;
- observações do cliente;
- horário do pedido;
- estado atual.

---

## 6.2 Ordem de chegada

Por padrão, os pedidos deverão ser apresentados na ordem em que
chegaram à cozinha.

---

## 6.3 Início do preparo

A cozinha deverá conseguir indicar que iniciou o preparo de um pedido.

O pedido deverá passar para:

Em preparo.

---

## 6.4 Finalização do preparo

Quando a cozinha finalizar o pedido, deverá conseguir marcá-lo como:

Pronto para despacho.

---

## 6.5 Alerta de demora

Pedidos cujo tempo de preparo ultrapasse o limite esperado deverão
ser visualmente destacados na tela da cozinha.

O tempo exato considerado como atraso será definido posteriormente.

---

# 7. Expedição

## 7.1 Pedidos disponíveis para despacho

A expedição deverá visualizar pedidos que estejam:

Pronto para despacho.

---

## 7.2 Solicitação de entregador

A expedição deverá poder solicitar um entregador através do parceiro
de entrega utilizado pela Waves.

Antes da confirmação, deverá ser possível conhecer o custo informado
pelo parceiro.

O fornecedor/API de entrega ainda deverá ser definido.

---

## 7.3 Atualização do pedido

Após a solicitação de um entregador, o pedido deverá acompanhar os
estados relacionados à entrega:

- Motoboy a caminho;
- Saiu para entrega;
- Entregue.

---

# 8. Entrega

## 8.1 Registro da entrega

O sistema deverá armazenar as informações básicas relacionadas à
entrega de cada pedido.

---

## 8.2 Rastreamento

Quando o parceiro de entrega disponibilizar um link de rastreamento,
esse link deverá estar associado ao pedido.

---

## 8.3 Rastreamento para o cliente

O cliente deverá receber ou ter acesso ao link de rastreamento
fornecido pelo parceiro de entrega.

O Guia funcional prevê o envio desse link diretamente pelo WhatsApp.

Outros pontos de acesso ao rastreamento poderão ser definidos durante
o desenvolvimento do Aplicativo Mobile.

---

# 9. Atendimento

## 9.1 Pedido manual

O usuário do perfil Atendimento deverá poder registrar um pedido
quando o cliente realizar o contato diretamente com a Waves.

O pedido manual deverá seguir o mesmo fluxo operacional dos pedidos
originados pelo Aplicativo Mobile.

---

## 9.2 Consulta de cliente

O atendimento deverá conseguir localizar clientes e consultar seu
histórico necessário para o atendimento.

---

# 10. WhatsApp — funcionalidade básica

O MVP deverá contemplar apenas as funções operacionais necessárias
descritas pela Waves.

Inicialmente:

- responder informações básicas de cardápio;
- responder informações básicas de horário;
- direcionar o cliente para realizar o pedido pelo Aplicativo Mobile;
- permitir o envio do link de rastreamento da entrega.

IA sofisticada ou automações comerciais não fazem parte desta
definição inicial do MVP.

---

# 11. Dashboard básico

O sistema deverá fornecer um painel básico para acompanhamento da
operação.

## 11.1 Vendas

Exibir pelo menos:

- faturamento;
- ticket médio;
- produtos mais vendidos;
- horário de pico.

## 11.2 Produção

Exibir pelo menos:

- tempo médio de preparo;
- quantidade de pedidos em andamento;
- situação dos pedidos.

## 11.3 Logística

Exibir pelo menos:

- tempo médio de entrega;
- pedidos entregues;
- pedidos cancelados, caso cancelamento seja adotado nas regras de negócio.

## 11.4 Estoque

Exibir pelo menos:

- ingredientes próximos ou abaixo do mínimo;
- produtos indisponíveis;
- custo médio dos ingredientes.

---

# 12. Critério geral de conclusão do MVP

O MVP será considerado funcional quando for possível executar o
seguinte cenário de ponta a ponta:

1. Cadastrar ingredientes.
2. Registrar estoque.
3. Cadastrar um produto.
4. Criar sua receita.
5. Calcular sua disponibilidade.
6. Disponibilizar o produto no cardápio do Aplicativo Mobile.
7. Abrir o Aplicativo Mobile.
8. Cadastrar ou identificar um cliente.
9. Visualizar o cardápio disponível.
10. Selecionar produtos e montar um pedido.
11. Informar os dados necessários para o pedido.
12. Realizar ou iniciar o processo de pagamento.
13. Confirmar o pedido no aplicativo.
14. Enviar o pedido ao backend.
15. Registrar o pedido como Recebido.
16. Confirmar o pedido.
17. Visualizar o pedido na cozinha.
18. Iniciar o preparo.
19. Finalizar o preparo.
20. Visualizar o pedido na expedição.
21. Solicitar ou associar uma entrega.
22. Registrar o motoboy a caminho.
23. Marcar o pedido como saiu para entrega.
24. Disponibilizar o rastreamento quando fornecido pelo parceiro.
25. Finalizar o pedido como entregue.
26. Refletir o consumo dos ingredientes no estoque.
27. Manter o histórico do pedido.
28. Manter o histórico do cliente.
29. Refletir a operação nos indicadores básicos do dashboard.

Também deverá ser possível criar um pedido manualmente pelo
Atendimento e fazê-lo percorrer o mesmo fluxo operacional após sua
criação.

Esse fluxo deverá acontecer sem depender de planilhas paralelas para
controlar a operação principal.

---

# 13. Limites e decisões ainda em aberto

A inclusão do Aplicativo Mobile no MVP não significa que todas as
decisões relacionadas a ele já estão definidas.

Ainda deverão ser esclarecidos em `open-questions.md`, entre outros:

- tecnologia utilizada para desenvolvimento do aplicativo;
- plataformas suportadas inicialmente;
- forma de cadastro e autenticação do cliente;
- obrigatoriedade e uso do CPF no aplicativo;
- recuperação de acesso;
- campos e regras de endereço de entrega;
- possibilidade de retirada no local;
- formas de pagamento;
- provedor de pagamento;
- comportamento quando o pagamento falhar;
- momento exato em que o pedido é considerado confirmado;
- estratégia de atualização do status no aplicativo;
- uso ou não de notificações push;
- disponibilização do rastreamento dentro do aplicativo;
- regras para cancelamento pelo cliente;
- comportamento do estoque em cancelamentos.

Esses pontos não deverão ser decididos silenciosamente durante a
implementação.

---

# 14. Observação

Este documento define somente o escopo do MVP.

Funcionalidades classificadas como "pós-MVP" deverão ser mantidas em
documentação separada.

Alterações no escopo aprovado do MVP deverão ser registradas e
validadas antes de entrarem no desenvolvimento.