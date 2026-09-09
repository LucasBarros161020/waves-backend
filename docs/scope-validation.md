# Validação de Escopo — Waves

## 1. Objetivo

Este documento formaliza a revisão e aprovação do escopo do MVP da Waves
antes do início das etapas técnicas do projeto.

A validação existe para garantir que:

- o que faz parte do MVP está claro;
- o que ficou para depois do MVP está separado;
- as dúvidas ainda não resolvidas estão registradas;
- nenhuma funcionalidade crítica foi esquecida;
- o desenvolvimento não comece com escopo indefinido;
- mudanças futuras possam ser rastreadas.

Este documento não substitui:

- `requirements/system_requirements.docx`;
- `mvp.md`;
- `post-mvp.md`;
- `open-questions.md`.

Ele funciona como registro de aprovação do conjunto desses documentos.

---

# 2. Documentos considerados na validação

A validação do escopo considera os seguintes arquivos:

## 2.1 Documento de requisitos

Arquivo:

```text
docs/requirements/system_requirements.docx
```

Função:

Registrar os requisitos funcionais identificados a partir do Guia do
Sistema Waves.

---

## 2.2 Escopo do MVP

Arquivo:

```text
docs/mvp.md
```

Função:

Definir as funcionalidades que precisam existir na primeira versão
operacional da Waves.

---

## 2.3 Escopo pós-MVP

Arquivo:

```text
docs/post-mvp.md
```

Função:

Registrar funcionalidades válidas para evolução futura, mas que não
devem bloquear a primeira entrega.

---

## 2.4 Dúvidas em aberto

Arquivo:

```text
docs/open-questions.md
```

Função:

Registrar decisões que ainda precisam ser tomadas para que o
desenvolvedor não invente regras de negócio durante a implementação.

---

# 3. Fluxo operacional principal validado

O MVP foi definido para suportar o seguinte fluxo principal:

```text
Cliente
→ Aplicativo Mobile
→ Backend Waves
→ Pedido
→ Confirmação
→ Cozinha / KDS
→ Expedição
→ Entrega
→ Finalização
```

Também deverá existir o fluxo alternativo de criação manual:

```text
Cliente
→ Atendimento
→ Backend Waves
→ Pedido
→ Confirmação
→ Cozinha / KDS
→ Expedição
→ Entrega
→ Finalização
```

Após ser aceito pelo backend, o pedido deverá utilizar o mesmo fluxo
operacional independentemente de sua origem.

---

# 4. Estados principais do pedido

O fluxo operacional aprovado para o pedido considera os seguintes
estados:

1. Recebido
2. Confirmado
3. Em preparo
4. Pronto para despacho
5. Motoboy a caminho
6. Saiu para entrega
7. Entregue

Regras adicionais envolvendo cancelamento, retorno de estado ou
alteração de pedido permanecem registradas em `open-questions.md`
enquanto não forem formalmente decididas.

---

# 5. Áreas incluídas no MVP

A primeira versão deverá contemplar as seguintes áreas.

## 5.1 Usuários e permissões

Incluído:

- usuários internos;
- perfis de acesso;
- Administrador;
- Gestor;
- Cozinha;
- Expedição;
- Atendimento;
- Estoque.

Detalhes ainda não definidos devem permanecer em `open-questions.md`.

---

## 5.2 Clientes

Incluído:

- cadastro;
- identificação por CPF conforme regra funcional;
- consulta;
- histórico de pedidos;
- reconhecimento em compras futuras;
- segmentação em Ativo, Em risco e Inativo.

Regras sobre obrigatoriedade do CPF, cadastro e autenticação ainda
precisam de decisão.

---

## 5.3 Aplicativo Mobile do Cliente

Incluído no MVP.

O aplicativo deverá permitir, no mínimo:

- identificar ou cadastrar o cliente;
- visualizar o cardápio;
- consultar disponibilidade de produtos;
- montar o pedido;
- informar dados necessários para entrega;
- realizar ou iniciar o pagamento;
- enviar o pedido ao backend;
- acompanhar o andamento;
- acessar recursos de acompanhamento da entrega definidos para o MVP;
- consultar histórico básico de pedidos.

O aplicativo será um cliente da API e não deverá duplicar as regras
centrais de negócio do backend.

---

## 5.4 Produtos e cardápio

Incluído:

- cadastro de produtos;
- nome;
- descrição;
- preço;
- imagem;
- status;
- consulta de produtos;
- disponibilidade calculada com base no estoque.

---

## 5.5 Ingredientes e receitas

Incluído:

- cadastro de ingredientes;
- unidade de medida;
- estoque mínimo;
- receita / ficha técnica dos produtos;
- quantidade de cada ingrediente utilizada na produção.

---

## 5.6 Estoque

Incluído:

- controle de quantidade;
- movimentações;
- compras;
- vendas;
- desperdícios;
- ajustes autorizados;
- alertas de estoque mínimo.

O momento exato da baixa, reservas e comportamento em cancelamentos
permanecem como decisões em aberto.

---

## 5.7 Compras e fornecedores

Incluído:

- cadastro básico de fornecedores;
- registro de compras;
- entrada automática no estoque;
- custo médio;
- suporte ao cálculo de custo de produção.

Os campos exatos de fornecedores e documentos de compra ainda precisam
ser definidos.

---

## 5.8 Custo de produção

Incluído:

- custo médio de ingredientes;
- cálculo aproximado do custo atual de produção;
- utilização da receita como base do cálculo.

---

## 5.9 Desperdício

Incluído:

- registro de desperdício;
- redução correspondente do estoque.

Motivo obrigatório, permissões e detalhes do registro permanecem em
aberto.

---

## 5.10 Pedidos

Incluído:

- pedidos pelo Aplicativo Mobile;
- pedidos lançados manualmente pelo Atendimento;
- itens do pedido;
- quantidade;
- preço considerado na venda;
- observações;
- origem;
- situação atual;
- histórico de estados.

---

## 5.11 Cozinha / KDS

Incluído:

- fila de pedidos;
- ordem de chegada;
- visualização dos itens;
- observações;
- início do preparo;
- finalização do preparo;
- alerta visual de demora.

O tempo exato considerado atraso ainda precisa ser definido.

---

## 5.12 Expedição

Incluído:

- visualização de pedidos prontos para despacho;
- solicitação de entregador;
- consulta do custo antes da confirmação;
- acompanhamento dos estados relacionados à entrega.

O parceiro de entrega ainda precisa ser definido.

---

## 5.13 Entrega e rastreamento

Incluído:

- associação da entrega ao pedido;
- dados básicos da entrega;
- link de rastreamento quando disponibilizado pelo parceiro;
- disponibilização desse rastreamento pelos canais definidos para o MVP.

---

## 5.14 Atendimento

Incluído:

- criação manual de pedidos;
- consulta de clientes;
- acesso ao histórico necessário para atendimento.

---

## 5.15 WhatsApp básico

Incluído:

- dúvidas simples de cardápio;
- dúvidas simples de horário;
- direcionamento para o Aplicativo Mobile;
- envio do link de rastreamento quando aplicável.

IA avançada permanece fora do MVP.

---

## 5.16 Dashboard básico

Incluído:

### Vendas

- faturamento;
- ticket médio;
- produtos mais vendidos;
- horário de pico.

### Produção

- tempo médio de preparo;
- pedidos em andamento;
- situação dos pedidos.

### Logística

- tempo médio de entrega;
- pedidos entregues;
- pedidos cancelados caso a regra de cancelamento seja aprovada.

### Estoque

- ingredientes abaixo ou próximos do mínimo;
- produtos indisponíveis;
- custo médio dos ingredientes.

---

# 6. Funcionalidades formalmente fora do MVP

Neste momento, estão classificadas como pós-MVP:

- IA avançada de atendimento;
- campanhas de retenção;
- programa de fidelidade;
- promoções sofisticadas;
- automações não essenciais.

Essas funcionalidades não devem bloquear o desenvolvimento ou o
lançamento do MVP.

Qualquer inclusão futura deverá ser registrada em `post-mvp.md`.

---

# 7. Decisões ainda em aberto

A existência de dúvidas não invalida o escopo aprovado.

As decisões pendentes estão concentradas em `open-questions.md` e
deverão ser resolvidas antes de afetarem diretamente o desenvolvimento
de seus respectivos módulos.

Entre as decisões de maior impacto estão:

- momento da confirmação do pedido;
- regra de cancelamento;
- formas de pagamento;
- provedor de pagamento;
- obrigatoriedade do CPF;
- plataformas iniciais do Aplicativo Mobile;
- autenticação do cliente;
- parceiro de entrega;
- momento da baixa de estoque;
- estoque negativo;
- estoque em cancelamentos.

Nenhuma dessas decisões deve ser implementada por suposição.

---

# 8. Critério de sucesso do MVP

O MVP deverá ser capaz de executar o seguinte cenário de ponta a ponta:

1. Cadastrar ingredientes.
2. Registrar estoque.
3. Cadastrar um produto.
4. Criar sua receita.
5. Calcular sua disponibilidade.
6. Disponibilizar o produto no Aplicativo Mobile.
7. Identificar ou cadastrar um cliente.
8. Exibir o cardápio disponível.
9. Permitir que o cliente monte o pedido.
10. Obter os dados necessários para o pedido.
11. Realizar ou iniciar o processo de pagamento.
12. Enviar o pedido ao backend.
13. Registrar o pedido como Recebido.
14. Confirmar o pedido.
15. Enviar o pedido para a fila da cozinha.
16. Iniciar o preparo.
17. Finalizar o preparo.
18. Disponibilizar o pedido para expedição.
19. Solicitar ou associar um entregador.
20. Atualizar os estados da entrega.
21. Disponibilizar rastreamento quando existir.
22. Finalizar o pedido como Entregue.
23. Atualizar o estoque conforme as regras aprovadas.
24. Manter o histórico do pedido.
25. Manter o histórico do cliente.
26. Atualizar os indicadores básicos do Dashboard.

Também deverá ser possível criar um pedido manualmente pelo Atendimento
e fazê-lo percorrer o mesmo fluxo operacional.

---

# 9. Critério de proteção do escopo

Após a aprovação deste documento:

- nenhuma funcionalidade deve ser adicionada ao MVP sem avaliação;
- nenhuma funcionalidade aprovada deve ser removida apenas por
  dificuldade técnica;
- novas ideias devem ser classificadas como MVP, pós-MVP ou dúvida;
- alterações devem ser registradas na documentação;
- decisões de negócio devem ser aprovadas pelo responsável do projeto;
- o desenvolvedor não deve alterar regras silenciosamente.

---

# 10. Checklist de validação

- [x] O Documento de Requisitos foi revisado.
- [x] O `mvp.md` foi revisado.
- [x] O `post-mvp.md` foi revisado.
- [x] O `open-questions.md` foi revisado.
- [x] O Aplicativo Mobile está corretamente incluído no MVP.
- [x] O fluxo principal do pedido está correto.
- [x] Os sete estados principais do pedido estão corretos.
- [x] As áreas operacionais necessárias estão contempladas.
- [x] As funcionalidades pós-MVP estão corretamente separadas.
- [x] As principais dúvidas de negócio estão registradas.
- [x] Nenhuma decisão ainda aberta foi tratada como regra aprovada.
- [x] O critério de sucesso do MVP representa a operação desejada.
- [x] O responsável pelo projeto concorda com o escopo descrito.

---

# 11. Aprovação

## Status

`APROVADO`

## Responsável pela validação

Responsável pelo projeto — aprovação registrada durante a revisão do
escopo.

## Data

2026-09-09

## Observações

Escopo revisado e aprovado.

O Aplicativo Mobile do Cliente permanece formalmente incluído no MVP.

As decisões ainda registradas em `open-questions.md` continuam abertas
e deverão ser resolvidas no momento adequado, sem impedir a aprovação
do escopo geral.

---

# 12. Conclusão da etapa 0.1.6

A etapa `0.1.6 — Validar o escopo` está concluída.

Foram revisados e aprovados:

1. Documento de Requisitos;
2. `mvp.md`;
3. `post-mvp.md`;
4. `open-questions.md`;
5. fluxo operacional principal;
6. áreas incluídas no MVP;
7. funcionalidades pós-MVP;
8. processo para tratamento de decisões ainda abertas.

Com esta aprovação, o bloco:

```text
0.1 — Definição do escopo
```

está formalmente concluído.

O projeto está autorizado a seguir para a próxima etapa da Fase 0,
mantendo como regra que decisões ainda abertas deverão ser resolvidas
antes da implementação das funcionalidades que dependem delas.
