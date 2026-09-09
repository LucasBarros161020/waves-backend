# Waves Backend

Backend do sistema operacional da Waves.

## Status

Projeto em fase inicial de estruturação.

O escopo funcional do MVP já foi levantado, documentado e aprovado.
As decisões de negócio ainda não definidas estão registradas em
`docs/open-questions.md`.

A implementação técnica do backend ainda não foi iniciada.

---

## Objetivo

Centralizar a operação da Waves em um único sistema, conectando:

- clientes;
- Aplicativo Mobile;
- pedidos;
- cardápio;
- produtos;
- ingredientes;
- receitas;
- estoque;
- compras;
- fornecedores;
- desperdícios;
- cozinha / KDS;
- expedição;
- entregas;
- atendimento;
- WhatsApp;
- dashboard operacional.

O backend será responsável por concentrar as regras de negócio e
fornecer os dados necessários para os diferentes canais e interfaces
do sistema.

---

## Fluxo principal do sistema

O fluxo operacional principal definido para o MVP é:

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

Também deverá existir o fluxo de pedidos criados manualmente pelo
Atendimento:

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

---

## Documentação

A documentação do projeto está localizada em `docs/`.

Estrutura atual:

```text
docs/
├── requirements/
│   └── system_requirements.docx
├── conventions.md
├── mvp.md
├── open-questions.md
├── post-mvp.md
└── scope-validation.md
```

### `docs/requirements/system_requirements.docx`

Documento de requisitos do sistema, elaborado a partir do Guia
funcional da Waves.

### `docs/mvp.md`

Define as funcionalidades que fazem parte da primeira versão do
sistema.

### `docs/post-mvp.md`

Registra funcionalidades e evoluções que ficaram deliberadamente fora
da primeira entrega.

### `docs/open-questions.md`

Registra decisões de negócio ainda não definidas.

O desenvolvedor não deve assumir silenciosamente uma regra que esteja
registrada como dúvida em aberto.

### `docs/scope-validation.md`

Formaliza a revisão e aprovação do escopo do MVP.

### `docs/conventions.md`

Será utilizado para registrar as convenções técnicas do projeto
durante a Fase 0.

---

## Escopo atual do MVP

O MVP contempla, entre outras áreas:

- usuários e perfis de acesso;
- clientes;
- Aplicativo Mobile do Cliente;
- produtos e cardápio;
- ingredientes e receitas;
- estoque;
- compras e fornecedores;
- custo médio e custo de produção;
- desperdícios;
- pedidos;
- cozinha / KDS;
- expedição;
- entrega e rastreamento;
- atendimento;
- WhatsApp básico;
- dashboard básico.

O detalhamento oficial está em `docs/mvp.md`.

---

## Tecnologias previstas

O backend será desenvolvido com:

- Python;
- FastAPI;
- PostgreSQL;
- SQLAlchemy;
- Alembic.

As versões, ferramentas auxiliares e demais decisões técnicas serão
definidas e documentadas nas próximas etapas da Fase 0.

---

## Estrutura do projeto

A estrutura técnica da aplicação ainda não foi criada.

Ela será adicionada progressivamente conforme as etapas de preparação
e fundação técnica forem concluídas.

Neste momento, o repositório contém principalmente a documentação
necessária para orientar o desenvolvimento.

---

## Regras para desenvolvimento

Durante o desenvolvimento:

- o escopo aprovado em `docs/mvp.md` deve ser respeitado;
- funcionalidades pós-MVP não devem bloquear a primeira entrega;
- dúvidas de negócio devem ser registradas e resolvidas antes de sua
  implementação;
- alterações de escopo devem ser documentadas;
- regras de negócio não devem ser inventadas pelo desenvolvedor;
- a documentação deve permanecer atualizada junto com o código.

---

## Repositórios relacionados

Este repositório contém o backend da Waves.

O Aplicativo Mobile do Cliente faz parte do MVP, mas deverá possuir seu
próprio projeto e consumir as APIs disponibilizadas por este backend.
