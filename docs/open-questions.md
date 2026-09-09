# Dúvidas em aberto — Waves

## 1. Objetivo

Este documento registra decisões de negócio que ainda precisam ser
definidas para que o MVP da Waves possa ser implementado sem que o
desenvolvedor precise assumir regras por conta própria.

Uma dúvida registrada aqui significa:

- a funcionalidade pertence ao MVP;
- o Guia funcional não define todos os detalhes necessários;
- a decisão precisa ser validada antes ou durante a implementação;
- nenhuma regra deve ser inventada silenciosamente pelo desenvolvedor.

---

# 2. Como usar este documento

Cada dúvida deverá possuir um status.

Status permitidos:

- `ABERTA` — ainda não existe decisão;
- `EM DISCUSSÃO` — decisão está sendo avaliada;
- `DECIDIDA` — regra aprovada;
- `DESCARTADA` — pergunta deixou de ser necessária.

Quando uma decisão for tomada, preencher:

- decisão;
- responsável pela decisão;
- data;
- impacto nos requisitos;
- impacto no MVP, caso exista.

Exemplo:

```text
Status: DECIDIDA
Decisão: O estoque será baixado quando o pedido for confirmado.
Responsável: Produto / Operação
Data: AAAA-MM-DD
```

---

# 3. Pedidos

## Q-PED-001 — Em qual momento o pedido passa de "Recebido" para "Confirmado"?

**Status:** ABERTA

O Guia define que o pedido confirmado possui pagamento aprovado e está
pronto para seguir para a cozinha.

Precisamos confirmar:

- a mudança será automática após aprovação do pagamento?
- algum operador deverá confirmar manualmente?
- pedidos criados manualmente pelo Atendimento seguem a mesma regra?
- existe algum cenário em que um pedido possa ser confirmado sem
  pagamento eletrônico?

**Decisão:** A definir.

---

## Q-PED-002 — Um pedido pode ser cancelado?

**Status:** ABERTA

O Dashboard previsto pelo Guia menciona pedidos cancelados, porém o
fluxo principal apresentado possui sete estados e não descreve o
processo de cancelamento.

Precisamos definir:

- cancelamento fará parte do MVP?
- quem pode cancelar?
- o cliente pode cancelar pelo Aplicativo Mobile?
- até qual estado o cancelamento será permitido?
- será necessário informar motivo?
- como ficará o histórico do pedido cancelado?

**Decisão:** A definir.

---

## Q-PED-003 — Um pedido pode voltar para um estado anterior?

**Status:** ABERTA

Exemplo:

```text
Em preparo
→ Confirmado
```

ou:

```text
Pronto para despacho
→ Em preparo
```

Precisamos definir se as transições serão sempre progressivas ou se
existirão exceções operacionais.

**Decisão:** A definir.

---

## Q-PED-004 — O pedido poderá ser alterado depois de criado?

**Status:** ABERTA

Precisamos definir se será possível:

- adicionar produtos;
- remover produtos;
- mudar quantidades;
- alterar observações;
- alterar endereço;
- alterar forma de pagamento.

Também precisamos definir até qual estado alterações serão permitidas.

**Decisão:** A definir.

---

## Q-PED-005 — O preço do pedido será congelado no momento da criação?

**Status:** ABERTA

O `mvp.md` já prevê que o item mantenha o preço considerado na venda.

Precisamos apenas confirmar a regra de negócio:

- o valor final é congelado na criação?
- é congelado na confirmação?
- alterações de preço no cardápio nunca modificam pedidos já criados?

**Decisão:** A definir.

---

# 4. Pagamento

## Q-PAG-001 — Quais formas de pagamento serão aceitas no MVP?

**Status:** ABERTA

Precisamos definir, por exemplo:

- PIX;
- cartão;
- dinheiro;
- pagamento na entrega;
- outros.

**Decisão:** A definir.

---

## Q-PAG-002 — Qual provedor de pagamento será utilizado?

**Status:** ABERTA

O Guia determina que o pedido confirmado possui pagamento aprovado,
mas não informa qual serviço ou provedor será utilizado.

Precisamos definir o provedor antes da implementação da integração.

**Decisão:** A definir.

---

## Q-PAG-003 — O que acontece quando o pagamento falha?

**Status:** ABERTA

Precisamos definir:

- o pedido é criado como `Recebido` antes do pagamento?
- pedidos com pagamento falho permanecem registrados?
- haverá nova tentativa?
- por quanto tempo o pedido fica aguardando?
- o estoque será afetado durante essa espera?

**Decisão:** A definir.

---

## Q-PAG-004 — Pagamentos de pedidos manuais seguem qual fluxo?

**Status:** ABERTA

Pedidos lançados pelo Atendimento poderão possuir comportamento
diferente dos pedidos do Aplicativo Mobile.

Precisamos definir como esses pedidos são considerados pagos e aptos
para confirmação.

**Decisão:** A definir.

---

# 5. Clientes

## Q-CLI-001 — CPF será obrigatório para todo cliente?

**Status:** ABERTA

O Guia determina que cada cliente é identificado pelo CPF e que seu
histórico deve permanecer unificado.

Precisamos confirmar:

- todo pedido exige CPF?
- cliente pode navegar no aplicativo sem CPF?
- cliente pode montar pedido sem CPF e informar apenas no checkout?
- pedidos manuais podem ser criados sem CPF?
- como tratar clientes que não desejem informar CPF?

**Decisão:** A definir.

---

## Q-CLI-002 — Quais dados mínimos serão obrigatórios no cadastro?

**Status:** ABERTA

Além do CPF, precisamos definir os campos mínimos do cliente.

Possíveis dados:

- nome;
- telefone;
- e-mail;
- data de nascimento;
- endereço.

Somente os campos aprovados deverão ser exigidos.

**Decisão:** A definir.

---

## Q-CLI-003 — Como a segmentação de clientes deve considerar pedidos cancelados?

**Status:** ABERTA

O Guia define:

- Ativo: comprou nos últimos 30 dias;
- Em risco: 31 a 60 dias sem comprar;
- Inativo: mais de 60 dias sem comprar.

Precisamos definir o que significa "comprou":

- pedido criado?
- pedido pago?
- pedido confirmado?
- pedido entregue?

**Decisão:** A definir.

---

# 6. Aplicativo Mobile

## Q-APP-001 — O aplicativo será lançado para quais plataformas no MVP?

**Status:** ABERTA

Precisamos decidir:

- Android;
- iOS;
- ambos.

Essa decisão impacta planejamento e tecnologia, mas não altera o fato
de que o Aplicativo Mobile pertence ao MVP.

**Decisão:** A definir.

---

## Q-APP-002 — Como o cliente fará cadastro e login?

**Status:** ABERTA

Precisamos definir a experiência de acesso.

Possibilidades a avaliar:

- telefone;
- e-mail e senha;
- código enviado por SMS;
- código enviado por WhatsApp;
- outros métodos.

**Decisão:** A definir.

---

## Q-APP-003 — O cliente poderá comprar sem criar uma conta completa?

**Status:** ABERTA

Precisamos definir se haverá:

- checkout como visitante;
- identificação obrigatória antes do pedido;
- cadastro automático durante o checkout.

Essa decisão deve ser compatível com a regra de identificação por CPF.

**Decisão:** A definir.

---

## Q-APP-004 — O Aplicativo Mobile permitirá retirada no local?

**Status:** ABERTA

O Guia descreve principalmente o fluxo com entrega.

Precisamos confirmar se o MVP terá:

- apenas entrega;
- entrega e retirada;
- outros tipos de atendimento.

Se retirada existir, o fluxo do pedido e os estados precisarão ser
reavaliados.

**Decisão:** A definir.

---

## Q-APP-005 — O cliente poderá cancelar pelo Aplicativo Mobile?

**Status:** ABERTA

Essa decisão depende da regra geral de cancelamento.

Precisamos definir:

- se o recurso existe;
- até qual estado;
- se haverá estorno;
- como o estoque será tratado.

**Decisão:** A definir.

---

## Q-APP-006 — O cliente receberá notificações push?

**Status:** ABERTA

Precisamos definir se o MVP enviará notificações quando o pedido mudar
de estado.

Exemplos:

- pedido confirmado;
- pedido em preparo;
- pronto;
- saiu para entrega;
- entregue.

O acompanhamento do pedido pertence ao MVP, mas o canal exato de
notificação ainda precisa ser decidido.

**Decisão:** A definir.

---

## Q-APP-007 — O rastreamento também ficará disponível dentro do aplicativo?

**Status:** ABERTA

O Guia prevê que o link fornecido pelo parceiro seja enviado ao cliente
via WhatsApp.

Precisamos decidir se o mesmo link também aparecerá na tela do pedido
dentro do Aplicativo Mobile.

**Decisão:** A definir.

---

# 7. Endereço e entrega

## Q-ENT-001 — Quais dados de endereço serão obrigatórios?

**Status:** ABERTA

Precisamos definir os campos necessários para solicitar uma entrega.

Exemplos:

- CEP;
- rua;
- número;
- complemento;
- bairro;
- cidade;
- referência.

**Decisão:** A definir.

---

## Q-ENT-002 — O cliente poderá possuir múltiplos endereços?

**Status:** ABERTA

Precisamos definir se o MVP permitirá:

- somente um endereço por cliente;
- múltiplos endereços salvos;
- endereço informado apenas durante o pedido.

**Decisão:** A definir.

---

## Q-ENT-003 — Qual parceiro de entrega será utilizado?

**Status:** ABERTA

O Guia prevê motoboy sob demanda, com consulta do custo antes da
confirmação da chamada, porém não define a empresa ou API.

Precisamos escolher o parceiro antes de implementar a integração.

**Decisão:** A definir.

---

## Q-ENT-004 — Quem confirma a contratação do motoboy?

**Status:** ABERTA

O Guia informa que o custo deve ser mostrado antes da confirmação.

Precisamos definir:

- Expedição confirma manualmente?
- Gestor também pode confirmar?
- poderá existir confirmação automática no futuro?

**Decisão:** A definir.

---

## Q-ENT-005 — Como os estados de entrega serão atualizados?

**Status:** ABERTA

Precisamos confirmar se o parceiro fornece:

- webhook;
- consulta periódica;
- atualização manual;
- outra forma.

Essa definição impactará os estados:

- Motoboy a caminho;
- Saiu para entrega;
- Entregue.

**Decisão:** A definir.

---

## Q-ENT-006 — O custo da entrega será pago por quem?

**Status:** ABERTA

Precisamos definir:

- custo integral para o cliente;
- custo integral para a Waves;
- valor fixo;
- valor calculado pelo parceiro;
- subsídio parcial;
- outras regras.

**Decisão:** A definir.

---

# 8. Estoque

## Q-EST-001 — Em qual momento os ingredientes serão baixados do estoque?

**Status:** ABERTA

O Guia informa que a venda desconta automaticamente os ingredientes,
mas não determina exatamente em qual estado do pedido isso acontece.

Possibilidades a decidir:

- criação do pedido;
- pagamento aprovado;
- confirmação;
- início do preparo;
- outro momento.

**Decisão:** A definir.

---

## Q-EST-002 — O sistema poderá permitir estoque negativo?

**Status:** ABERTA

Precisamos definir se uma operação poderá deixar a quantidade de um
ingrediente abaixo de zero.

**Decisão:** A definir.

---

## Q-EST-003 — Como o estoque será tratado em cancelamentos?

**Status:** ABERTA

Caso os ingredientes já tenham sido descontados, precisamos definir:

- devolução automática;
- devolução somente antes do preparo;
- ajuste manual;
- nenhuma devolução em determinados estados.

**Decisão:** A definir.

---

## Q-EST-004 — Haverá reserva de estoque antes da baixa definitiva?

**Status:** ABERTA

Essa regra é importante especialmente para pedidos simultâneos pelo
Aplicativo Mobile.

Precisamos definir conceitualmente se:

- o estoque será apenas baixado;
- existirá quantidade reservada;
- a reserva acontecerá em algum estado específico.

A implementação técnica será definida posteriormente.

**Decisão:** A definir.

---

## Q-EST-005 — Ajustes manuais exigirão motivo?

**Status:** ABERTA

O MVP prevê ajustes autorizados.

Precisamos definir:

- quais perfis podem ajustar;
- se motivo é obrigatório;
- se haverá tipos de ajuste;
- se o histórico deverá identificar o responsável.

**Decisão:** A definir.

---

# 9. Desperdício

## Q-DES-001 — O registro de desperdício exige justificativa?

**Status:** ABERTA

Precisamos definir se o operador deverá informar:

- motivo;
- observação;
- quantidade;
- responsável.

**Decisão:** A definir.

---

## Q-DES-002 — Quais perfis podem registrar desperdício?

**Status:** ABERTA

O Guia associa a função à Cozinha.

Precisamos confirmar se:

- somente Cozinha;
- Gestor;
- Administrador;

também poderão registrar ou corrigir desperdícios.

**Decisão:** A definir.

---

# 10. Compras e fornecedores

## Q-COM-001 — Quais dados de fornecedor serão necessários no MVP?

**Status:** ABERTA

O Guia menciona fornecedores e compras, mas não define os dados
cadastrais.

Precisamos definir o mínimo necessário para a operação.

**Decisão:** A definir.

---

## Q-COM-002 — Uma compra precisa armazenar documento fiscal?

**Status:** ABERTA

Precisamos decidir se o MVP registrará informações como:

- número da nota;
- chave;
- data de emissão;
- anexo;
- nenhum documento fiscal.

**Decisão:** A definir.

---

## Q-COM-003 — Como será tratado o custo médio?

**Status:** ABERTA

O Guia determina o recálculo automático do custo médio após compras.

Precisamos validar com o responsável financeiro/operacional a regra
exata utilizada quando:

- existe estoque anterior;
- entra nova compra;
- há ajuste de estoque;
- há desperdício.

A fórmula técnica deverá refletir essa regra aprovada.

**Decisão:** A definir.

---

# 11. Produtos e cardápio

## Q-CAR-001 — Produto indisponível some do aplicativo ou aparece como indisponível?

**Status:** ABERTA

O Guia diz que, quando um ingrediente acaba, o produto correspondente
desaparece automaticamente do cardápio visível.

Precisamos confirmar se essa regra será seguida literalmente no
Aplicativo Mobile ou se o produto poderá permanecer visível com estado
"indisponível".

**Decisão:** A definir.

---

## Q-CAR-002 — Um produto pode ser desativado manualmente mesmo tendo estoque?

**Status:** ABERTA

Exemplos:

- produto temporariamente suspenso;
- produto fora de temporada;
- problema operacional.

Precisamos confirmar se existirá disponibilidade manual além da
disponibilidade calculada pelo estoque.

**Decisão:** A definir.

---

## Q-CAR-003 — O preço pode variar por canal?

**Status:** ABERTA

Precisamos confirmar se o preço será sempre o mesmo para:

- Aplicativo Mobile;
- Atendimento manual.

**Decisão:** A definir.

---

# 12. Cozinha / KDS

## Q-KDS-001 — Qual tempo caracteriza atraso no preparo?

**Status:** ABERTA

O Guia determina que pedidos demorados sejam destacados
automaticamente, mas não define o limite.

Precisamos definir:

- um tempo único para todos os pedidos;
- tempo por produto;
- tempo por categoria;
- outra regra.

**Decisão:** A definir.

---

## Q-KDS-002 — Quem pode iniciar e finalizar o preparo?

**Status:** ABERTA

O perfil Cozinha claramente possui essa função.

Precisamos confirmar se Administrador ou Gestor também poderão executar
essas ações.

**Decisão:** A definir.

---

## Q-KDS-003 — Como pedidos com vários produtos afetam o tempo esperado?

**Status:** ABERTA

Precisamos saber se o limite de atraso será igual para qualquer pedido
ou se quantidade/complexidade influenciará.

**Decisão:** A definir.

---

# 13. Usuários e permissões

## Q-USR-001 — Administrador pode executar ações de todos os outros perfis?

**Status:** ABERTA

O Guia define "acesso completo", mas precisamos confirmar se isso
significa também executar todas as ações operacionais.

**Decisão:** A definir.

---

## Q-USR-002 — Gestor poderá alterar pedidos em andamento?

**Status:** ABERTA

O Guia informa que o Gestor possui acesso a painel, estoque, clientes e
cancelamento de pedidos.

Precisamos definir exatamente quais ações sobre pedidos serão
permitidas.

**Decisão:** A definir.

---

## Q-USR-003 — Um usuário poderá possuir mais de um perfil?

**Status:** ABERTA

Precisamos decidir se cada usuário terá:

- exatamente um perfil;
- múltiplos perfis/permissões.

**Decisão:** A definir.

---

# 14. WhatsApp

## Q-WPP-001 — Qual provedor de WhatsApp será utilizado?

**Status:** ABERTA

O Guia define o comportamento esperado, mas não a integração.

A escolha do provedor deverá acontecer antes da implementação.

**Decisão:** A definir.

---

## Q-WPP-002 — Quais perguntas a IA básica deverá responder?

**Status:** ABERTA

O Guia cita:

- cardápio;
- horário.

Precisamos transformar isso em um escopo fechado de atendimento para o
MVP.

**Decisão:** A definir.

---

## Q-WPP-003 — Como o link para o Aplicativo Mobile será enviado?

**Status:** ABERTA

Precisamos definir o destino que será enviado ao cliente:

- App Store;
- Google Play;
- página intermediária;
- deep link;
- outro.

A decisão depende também das plataformas escolhidas para o MVP.

**Decisão:** A definir.

---

# 15. Dashboard

## Q-DASH-001 — Qual período padrão dos indicadores?

**Status:** ABERTA

Exemplos:

- dia atual;
- últimos 7 dias;
- mês atual;
- período selecionável.

**Decisão:** A definir.

---

## Q-DASH-002 — Como será calculado o ticket médio?

**Status:** ABERTA

Precisamos definir quais pedidos entram no cálculo:

- recebidos;
- confirmados;
- pagos;
- entregues;
- excluir cancelados.

**Decisão:** A definir.

---

## Q-DASH-003 — Como será determinado o horário de pico?

**Status:** ABERTA

Precisamos definir:

- quantidade de pedidos por faixa horária;
- faturamento;
- outro indicador.

**Decisão:** A definir.

---

## Q-DASH-004 — Como serão tratados pedidos cancelados nos indicadores?

**Status:** ABERTA

Essa definição depende também da regra geral de cancelamento.

Precisamos definir o impacto em:

- faturamento;
- ticket médio;
- produtos mais vendidos;
- tempo de preparo;
- logística.

**Decisão:** A definir.

---

# 16. Priorização das decisões

Nem todas as dúvidas precisam ser respondidas no mesmo momento.

## Prioridade A — resolver antes de implementar os respectivos módulos

- Q-PED-001 — confirmação do pedido;
- Q-PED-002 — cancelamento;
- Q-PAG-001 — formas de pagamento;
- Q-PAG-002 — provedor de pagamento;
- Q-CLI-001 — obrigatoriedade do CPF;
- Q-APP-001 — plataformas do Aplicativo Mobile;
- Q-APP-002 — cadastro e login;
- Q-ENT-003 — parceiro de entrega;
- Q-EST-001 — momento da baixa de estoque;
- Q-EST-002 — estoque negativo;
- Q-EST-003 — estoque em cancelamentos.

## Prioridade B — resolver antes da conclusão do módulo correspondente

- regras de endereço;
- múltiplos endereços;
- custo da entrega;
- desperdício;
- ajustes manuais;
- fornecedor;
- custo médio;
- produto indisponível;
- alerta da cozinha;
- permissões;
- WhatsApp;
- indicadores.

---

# 17. Critério de conclusão desta etapa

A etapa de levantamento de dúvidas será considerada concluída quando:

- as dúvidas relevantes do MVP estiverem registradas;
- nenhuma decisão ausente do Guia estiver sendo tratada como fato;
- os pontos críticos estiverem priorizados;
- existir um processo claro para registrar as respostas;
- o responsável pelo projeto puder revisar e decidir cada item
  progressivamente.

Não é necessário responder todas as perguntas para concluir esta etapa.

O objetivo é garantir que as perguntas estejam visíveis antes que o
desenvolvimento dependa delas.
