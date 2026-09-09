# Convenções do Projeto — Waves Backend

## 1. Objetivo

Este documento registra as convenções adotadas no projeto
`waves-backend`.

O objetivo é garantir consistência entre desenvolvedores, branches,
commits, código, banco de dados, APIs e documentação.

As convenções técnicas ainda serão preenchidas progressivamente ao
longo da Fase 0.

---

# 2. Estratégia de branches

## 2.1 Branch principal

A branch principal do projeto é:

```text
main
```

A `main` representa a versão estável do repositório.

Não deve ser utilizada diretamente para desenvolvimento de novas
funcionalidades.

---

## 2.2 Branches de trabalho

Cada tarefa deve ser desenvolvida em uma branch própria.

Padrões adotados:

```text
feature/*
fix/*
docs/*
chore/*
```

### `feature/*`

Utilizada para novas funcionalidades.

Exemplos:

```text
feature/customer-auth
feature/order-status
feature/inventory-movements
```

### `fix/*`

Utilizada para correções de bugs.

Exemplos:

```text
fix/negative-stock
fix/order-total
```

### `docs/*`

Utilizada para alterações exclusivamente de documentação.

Exemplos:

```text
docs/project-initialization
docs/update-mvp
docs/add-api-conventions
```

### `chore/*`

Utilizada para tarefas de configuração, manutenção ou infraestrutura
que não representam uma funcionalidade de negócio.

Exemplos:

```text
chore/setup-ruff
chore/update-dependencies
```

---

## 2.3 Fluxo de trabalho

Fluxo esperado:

```text
main
  ↓
nova branch
  ↓
desenvolvimento
  ↓
commits
  ↓
push
  ↓
Pull Request
  ↓
revisão
  ↓
merge em main
```

Exemplo:

```bash
git checkout -b feature/customer-registration
```

Após concluir a tarefa:

```bash
git push -u origin feature/customer-registration
```

A integração com `main` deve ocorrer por Pull Request.

---

# 3. Padrão de commits

O projeto utiliza o padrão **Conventional Commits**.

Formato:

```text
<type>(<optional-scope>): <description>
```

O escopo é opcional.

Exemplos:

```text
docs: add MVP documentation

feat(customers): add customer registration

feat(inventory): add stock movements

fix(orders): prevent invalid status transition

test(products): add product service tests

chore: configure linting
```

---

## 3.1 Tipos permitidos

### `feat`

Nova funcionalidade.

Exemplo:

```text
feat(customers): add customer registration
```

---

### `fix`

Correção de bug.

Exemplo:

```text
fix(orders): prevent invalid status transition
```

---

### `docs`

Alteração apenas em documentação.

Exemplo:

```text
docs: add project scope validation
```

---

### `chore`

Configuração, manutenção ou tarefa técnica que não altera uma regra
de negócio.

Exemplo:

```text
chore: configure ruff
```

---

### `refactor`

Refatoração de código sem mudança intencional de comportamento.

Exemplo:

```text
refactor(orders): simplify order service
```

---

### `test`

Criação ou alteração de testes.

Exemplo:

```text
test(products): add product creation tests
```

---

### `perf`

Melhoria de desempenho.

Exemplo:

```text
perf(catalog): optimize product availability query
```

---

### `build`

Mudanças relacionadas a build, empacotamento ou dependências.

Exemplo:

```text
build: update project dependencies
```

---

### `ci`

Mudanças relacionadas a integração ou entrega contínua.

Exemplo:

```text
ci: add test workflow
```

---

### `revert`

Reversão de uma alteração anterior.

Exemplo:

```text
revert: revert customer authentication changes
```

---

## 3.2 Regras para mensagens de commit

As mensagens devem seguir estas regras:

1. Escrever em inglês.
2. Utilizar letras minúsculas no início da descrição.
3. Não terminar a descrição com ponto final.
4. Descrever objetivamente o que o commit faz.
5. Manter cada commit pequeno e logicamente coeso.
6. Não misturar assuntos diferentes no mesmo commit.
7. Utilizar escopo quando ele ajudar a identificar o módulo alterado.

Evitar mensagens como:

```text
changes
update files
final version
fix stuff
alterações projeto
```

Preferir:

```text
docs: add initial project documentation
feat(inventory): add stock movements
fix(customers): prevent duplicate cpf
```

---

# 4. Nomenclatura

A definir durante a etapa correspondente da Fase 0.

---

# 5. Identificadores

A definir durante a etapa correspondente da Fase 0.

---

# 6. Datas e horários

A definir durante a etapa correspondente da Fase 0.

---

# 7. Padrões da API

A definir durante a etapa correspondente da Fase 0.

---

# 8. Erros da API

A definir durante a etapa correspondente da Fase 0.

---

# 9. Paginação, filtros e ordenação

A definir durante a etapa correspondente da Fase 0.

---

# 10. Observação

Este documento é evolutivo.

Sempre que uma nova convenção for aprovada para o projeto, ela deve ser
registrada aqui antes de ser tratada como padrão obrigatório pela equipe.
