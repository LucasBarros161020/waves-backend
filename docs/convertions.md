# Convenções do Projeto — Waves Backend

## 1. Objetivo

Este documento registra as convenções adotadas no projeto
`waves-backend`.

O objetivo é garantir consistência entre desenvolvedores, branches,
commits, código, banco de dados, APIs e documentação.

As convenções técnicas serão preenchidas progressivamente ao longo da
Fase 0 e deverão ser seguidas durante o desenvolvimento.

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

### `fix`

Correção de bug.

Exemplo:

```text
fix(orders): prevent invalid status transition
```

### `docs`

Alteração apenas em documentação.

Exemplo:

```text
docs: add project scope validation
```

### `chore`

Configuração, manutenção ou tarefa técnica que não altera uma regra
de negócio.

Exemplo:

```text
chore: configure ruff
```

### `refactor`

Refatoração de código sem mudança intencional de comportamento.

Exemplo:

```text
refactor(orders): simplify order service
```

### `test`

Criação ou alteração de testes.

Exemplo:

```text
test(products): add product creation tests
```

### `perf`

Melhoria de desempenho.

Exemplo:

```text
perf(catalog): optimize product availability query
```

### `build`

Mudanças relacionadas a build, empacotamento ou dependências.

Exemplo:

```text
build: update project dependencies
```

### `ci`

Mudanças relacionadas a integração ou entrega contínua.

Exemplo:

```text
ci: add test workflow
```

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

## 4.1 Regra geral

O projeto utilizará nomes em **inglês** para código, banco de dados,
rotas, variáveis, classes e objetos técnicos.

A documentação de negócio pode permanecer em português.

Evitar misturar português e inglês no código.

Errado:

```python
customer_nome
pedido_status
get_cliente()
```

Correto:

```python
customer_name
order_status
get_customer()
```

---

## 4.2 Arquivos e módulos Python

Arquivos e módulos Python devem utilizar:

```text
snake_case
```

Exemplos:

```text
order_service.py
customer_repository.py
inventory_movement.py
product_availability.py
```

Evitar:

```text
OrderService.py
customerRepository.py
produto_service.py
```

---

## 4.3 Pacotes e diretórios Python

Pacotes e diretórios de código devem utilizar:

```text
snake_case
```

Exemplos:

```text
customers/
inventory/
order_items/
shared/
```

Quando o nome do domínio puder ser representado por uma única palavra,
preferir nomes simples:

```text
orders/
products/
customers/
inventory/
```

---

## 4.4 Classes

Classes devem utilizar:

```text
PascalCase
```

Exemplos:

```python
class Customer:
    ...

class OrderService:
    ...

class InventoryMovement:
    ...

class ProductRepository:
    ...
```

---

## 4.5 Funções e métodos

Funções e métodos devem utilizar:

```text
snake_case
```

Exemplos:

```python
def create_order():
    ...

def calculate_product_availability():
    ...

def get_customer_by_cpf():
    ...
```

Os nomes devem indicar claramente a ação executada.

Preferir:

```python
create_customer()
get_order_by_id()
update_order_status()
calculate_average_cost()
```

Evitar nomes genéricos como:

```python
process()
handle()
do_stuff()
execute()
```

quando um nome mais específico puder ser utilizado.

---

## 4.6 Variáveis

Variáveis devem utilizar:

```text
snake_case
```

Exemplos:

```python
customer_id
order_total
available_quantity
average_cost
```

Evitar abreviações desnecessárias.

Preferir:

```python
customer
ingredient
quantity
```

Evitar:

```python
cust
ing
qty
```

Abreviações amplamente reconhecidas pelo domínio ou tecnologia podem
ser utilizadas quando melhorarem a legibilidade, por exemplo:

```python
cpf
api
url
id
```

---

## 4.7 Constantes

Constantes devem utilizar:

```text
UPPER_SNAKE_CASE
```

Exemplos:

```python
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
DEFAULT_PREPARATION_TIME = 15
```

---

## 4.8 Enums

Classes de enum devem utilizar `PascalCase`.

Os valores persistidos ou expostos pela API devem utilizar
`lower_snake_case`.

Exemplo:

```python
from enum import StrEnum


class OrderStatus(StrEnum):
    RECEIVED = "received"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    READY_FOR_DISPATCH = "ready_for_dispatch"
    COURIER_ON_THE_WAY = "courier_on_the_way"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
```

Os membros Python devem utilizar:

```text
UPPER_SNAKE_CASE
```

---

## 4.9 Models SQLAlchemy

Classes que representam entidades persistidas devem utilizar nome
singular em `PascalCase`.

Exemplos:

```python
Customer
Product
Ingredient
Order
OrderItem
InventoryMovement
```

A classe deve representar uma entidade individual.

---

## 4.10 Tabelas do banco de dados

Tabelas devem utilizar:

```text
plural + snake_case
```

Exemplos:

```text
users
customers
products
ingredients
product_ingredients
inventory_movements
orders
order_items
order_status_history
```

Evitar:

```text
User
customer
OrderItems
tb_products
tbl_customer
```

Não utilizar prefixos como:

```text
tb_
tbl_
```

---

## 4.11 Colunas do banco de dados

Colunas devem utilizar:

```text
snake_case
```

Exemplos:

```text
id
customer_id
product_id
unit_price
available_quantity
created_at
updated_at
```

---

## 4.12 Chaves estrangeiras

Campos de chave estrangeira devem utilizar:

```text
<entity>_id
```

Exemplos:

```text
customer_id
order_id
product_id
ingredient_id
supplier_id
```

---

## 4.13 Tabelas de associação

Tabelas de associação devem utilizar nomes que representem claramente
as entidades relacionadas.

Exemplo:

```text
product_ingredients
```

Representando a relação entre:

```text
products
ingredients
```

Evitar nomes abstratos como:

```text
product_relation
product_map
links
```

---

## 4.14 Índices e constraints

Quando forem nomeados explicitamente, utilizar padrões previsíveis.

### Índices

```text
ix_<table>_<column>
```

Exemplo:

```text
ix_customers_cpf
ix_orders_status
```

### Unique constraints

```text
uq_<table>_<column>
```

Exemplo:

```text
uq_users_email
uq_customers_cpf
```

### Foreign keys

```text
fk_<table>_<column>_<referenced_table>
```

Exemplo:

```text
fk_orders_customer_id_customers
```

### Check constraints

```text
ck_<table>_<rule>
```

Exemplo:

```text
ck_order_items_quantity_positive
```

---

## 4.15 Schemas Pydantic

Schemas devem utilizar `PascalCase` e indicar claramente sua função.

Padrão recomendado:

```text
<Entity>Create
<Entity>Update
<Entity>Read
```

Exemplo:

```python
CustomerCreate
CustomerUpdate
CustomerRead

ProductCreate
ProductUpdate
ProductRead

OrderCreate
OrderRead
```

Quando houver um schema específico para listagem, filtros ou respostas
especializadas, o nome deve indicar essa finalidade.

Exemplos:

```python
OrderListItem
OrderFilter
ProductAvailabilityRead
```

---

## 4.16 Serviços

Classes de serviço devem utilizar:

```text
<Entity>Service
```

Exemplos:

```python
CustomerService
OrderService
InventoryService
ProductAvailabilityService
```

Arquivos correspondentes:

```text
customer_service.py
order_service.py
inventory_service.py
product_availability_service.py
```

---

## 4.17 Repositórios

Classes responsáveis pelo acesso aos dados devem utilizar:

```text
<Entity>Repository
```

Exemplos:

```python
CustomerRepository
OrderRepository
ProductRepository
```

Arquivos:

```text
customer_repository.py
order_repository.py
product_repository.py
```

---

## 4.18 Rotas da API

As rotas deverão utilizar:

- nomes em inglês;
- substantivos;
- plural para coleções;
- letras minúsculas;
- hífen (`-`) quando um segmento possuir mais de uma palavra.

Exemplos:

```text
/customers
/products
/orders
/inventory-movements
/order-status-history
```

Evitar verbos na URL quando a operação puder ser representada pelo
método HTTP.

Preferir:

```text
POST /customers
GET /customers/{customer_id}
PATCH /customers/{customer_id}
```

Evitar:

```text
POST /create-customer
GET /get-customer/{customer_id}
POST /update-customer/{customer_id}
```

A definição completa do padrão REST será feita na etapa de convenções
da API.

---

## 4.19 Parâmetros de rota e query string

Parâmetros devem utilizar:

```text
snake_case
```

Exemplos:

```text
/customer/{customer_id}

/orders?page=1&page_size=20

/products?active=true

/orders?customer_id=<id>
```

---

## 4.20 Campos JSON

Campos de entrada e saída da API devem utilizar:

```text
snake_case
```

Exemplo:

```json
{
  "customer_id": "uuid",
  "created_at": "2026-09-09T17:00:00Z",
  "total_amount": "42.90"
}
```

O backend não utilizará `camelCase` nos contratos JSON.

Caso um cliente externo precise de outro formato no futuro, essa
conversão deverá ser tratada explicitamente.

---

## 4.21 Testes

Arquivos de teste devem utilizar o prefixo:

```text
test_
```

Exemplos:

```text
test_customer_service.py
test_order_creation.py
test_inventory_movements.py
```

Funções de teste também devem utilizar nomes descritivos:

```python
def test_create_customer_with_valid_data():
    ...

def test_create_order_with_insufficient_stock():
    ...
```

Evitar:

```python
def test_1():
    ...

def test_customer():
    ...
```

---

## 4.22 Regra de consistência

Antes de criar um novo nome, verificar se já existe um termo adotado
para o mesmo conceito.

Exemplo:

Se o projeto utiliza:

```text
customer
```

não introduzir posteriormente:

```text
client
consumer
buyer
```

para representar a mesma entidade.

Da mesma forma:

```text
order
```

deve ser utilizado de forma consistente em vez de alternar entre:

```text
order
purchase
request
pedido
```

A consistência de domínio tem prioridade sobre preferências
individuais.

---


## 4.23 Cabeçalho padrão dos arquivos Python

Todos os arquivos Python do projeto deverão possuir um cabeçalho de
metadados padronizado.

Modelo:

```python
# -*- coding: utf-8 -*-
"""Descrição objetiva do módulo."""

__author__ = "Lucas Barros"
__version__ = "0.1.0"
__maintainer__ = "Lucas Barros"
__email__ = "lucasbarros2000@hotmail.com"
__status__ = "Development"
```

Regras:

- a declaração de encoding deverá permanecer na primeira linha;
- o módulo deverá possuir uma docstring curta e objetiva;
- os metadados deverão aparecer após a docstring e antes do código do módulo;
- `__version__` deverá utilizar string;
- enquanto o sistema estiver em desenvolvimento, utilizar `Development`;
- `Production` somente deverá ser utilizado quando a versão correspondente estiver efetivamente em produção;
- novos arquivos Python deverão nascer com esse padrão, incluindo arquivos `__init__.py`.

---

# 5. Identificadores

## 5.1 Estratégia padrão

O projeto utilizará **UUID** como identificador primário das entidades
persistidas.

A versão padrão adotada será:

```text
UUID v4
```

A escolha prioriza:

- simplicidade;
- geração independente do banco;
- baixa previsibilidade dos identificadores;
- facilidade de utilização em APIs;
- ausência de dependência de sequências numéricas;
- consistência entre módulos.

---

## 5.2 Tipo no PostgreSQL

Os identificadores deverão utilizar o tipo nativo:

```text
UUID
```

do PostgreSQL.

Evitar armazenar UUID como:

```text
VARCHAR
TEXT
CHAR(36)
```

quando o tipo nativo estiver disponível.

---

## 5.3 Tipo no Python

No código Python, utilizar:

```python
from uuid import UUID
```

para representar identificadores existentes.

Para gerar novos identificadores:

```python
from uuid import uuid4

entity_id = uuid4()
```

---

## 5.4 Chave primária

Por padrão, tabelas de domínio deverão possuir:

```text
id
```

como chave primária UUID.

Exemplo conceitual:

```text
customers
---------
id UUID PRIMARY KEY
name
cpf
created_at
updated_at
```

No SQLAlchemy, o identificador deverá ser mapeado para o tipo UUID
compatível com PostgreSQL.

---

## 5.5 Geração do identificador

A aplicação deverá ser capaz de gerar o UUID antes da inserção no banco.

Padrão:

```python
uuid4()
```

Não depender de uma sequência incremental para criar o identificador
principal da entidade.

---

## 5.6 Chaves estrangeiras

Chaves estrangeiras deverão utilizar o mesmo tipo UUID da entidade
referenciada.

Exemplo:

```text
orders.id          UUID
orders.customer_id UUID
customers.id       UUID
```

Nunca utilizar tipos diferentes entre a primary key e sua foreign key.

---

## 5.7 Nome das chaves estrangeiras

A nomenclatura permanece:

```text
<entity>_id
```

Exemplos:

```text
customer_id
order_id
product_id
ingredient_id
supplier_id
```

---

## 5.8 Identificadores nas rotas

Identificadores expostos nas URLs deverão utilizar UUID.

Exemplo:

```text
GET /customers/550e8400-e29b-41d4-a716-446655440000
```

Em FastAPI, o parâmetro deverá ser tipado como UUID.

Exemplo:

```python
from uuid import UUID
from fastapi import APIRouter

router = APIRouter()


@router.get("/customers/{customer_id}")
async def get_customer(customer_id: UUID):
    ...
```

Assim, valores inválidos poderão ser rejeitados antes de chegar à
regra de negócio.

---

## 5.9 Identificadores nos schemas

Schemas Pydantic deverão utilizar `UUID`, e não `str`, para IDs.

Preferir:

```python
from uuid import UUID
from pydantic import BaseModel


class CustomerRead(BaseModel):
    id: UUID
    name: str
```

Evitar:

```python
class CustomerRead(BaseModel):
    id: str
    name: str
```

quando o campo representa um UUID do domínio.

---

## 5.10 IDs externos

Identificadores recebidos de serviços externos não deverão substituir
a chave primária interna da entidade.

Exemplos:

- ID do provedor de pagamento;
- ID do parceiro de entrega;
- ID de mensagem do WhatsApp;
- ID de transação externa.

Esses valores deverão possuir campos próprios, por exemplo:

```text
provider_payment_id
delivery_provider_id
whatsapp_message_id
external_transaction_id
```

A entidade continuará possuindo seu:

```text
id UUID
```

interno.

---

## 5.11 IDs legados ou de negócio

Campos como:

- CPF;
- número do pedido exibido ao cliente;
- número de nota;
- código de rastreamento;

não devem ser utilizados como primary key.

Eles representam identificadores de negócio e podem possuir regras
próprias de unicidade, formato ou apresentação.

---

## 5.12 Número amigável do pedido

O UUID interno do pedido não precisa ser o mesmo identificador exibido
para o cliente.

O sistema poderá possuir futuramente um campo amigável, por exemplo:

```text
order_number
```

para exibição operacional ou ao cliente.

Exemplo:

```text
#10428
```

Essa decisão de formato e geração ainda deverá ser definida antes da
implementação de `orders`.

Independentemente disso:

```text
orders.id
```

continuará sendo UUID.

---

## 5.13 Tabelas de associação

Por padrão, relações que representem uma entidade própria do domínio
podem possuir seu próprio UUID.

Exemplo:

```text
product_ingredients
```

poderá possuir:

```text
id UUID
product_id UUID
ingredient_id UUID
quantity
```

Além disso, deverá ser utilizada uma constraint de unicidade quando a
regra exigir impedir relações duplicadas, por exemplo:

```text
UNIQUE(product_id, ingredient_id)
```

A decisão por chave composta somente deverá ser adotada explicitamente
quando trouxer benefício claro.

O padrão do projeto permanece favorecer uma chave primária UUID simples.

---

## 5.14 Não expor sequência interna

O projeto não deverá introduzir um identificador inteiro incremental
apenas para expô-lo publicamente.

Evitar padrões como:

```text
/customers/1
/customers/2
/customers/3
```

A API deverá utilizar o UUID da entidade.

---

## 5.15 UUID não é mecanismo de autorização

O fato de um UUID ser difícil de adivinhar não substitui controle de
acesso.

Todo endpoint deverá validar normalmente:

- autenticação;
- perfil;
- permissão;
- propriedade do recurso, quando aplicável.

UUID serve como estratégia de identificação, não como proteção de
segurança.

---

## 5.16 Regra oficial

Salvo decisão explícita e documentada em contrário:

```text
Primary key        → UUID v4
Tipo PostgreSQL    → UUID
Tipo Python        → UUID
Geração            → uuid4()
Foreign keys       → UUID
Parâmetro de rota  → UUID
Schema Pydantic    → UUID
Nome da PK         → id
Nome da FK         → <entity>_id
```

Qualquer exceção deverá ser justificada e registrada neste documento.

---

# 6. Datas e horários

## 6.1 Regra geral

O backend deverá trabalhar internamente com datas e horários de forma
consistente e independente do fuso horário da máquina onde estiver
executando.

A regra padrão do projeto será:

```text
Persistência no banco       → UTC
Processamento no backend    → UTC
Contratos da API            → ISO 8601 com timezone
Exibição para o usuário     → timezone da operação / cliente
```

Nenhum horário relevante do domínio deverá depender do timezone local
do servidor.

---

## 6.2 Timezone operacional

Para o MVP, o timezone operacional padrão da Waves será tratado como:

```text
America/Sao_Paulo
```

Esse timezone representa a referência utilizada para informações
operacionais locais, por exemplo:

- horário de funcionamento;
- agrupamento de vendas por dia;
- horário de pico;
- relatórios diários;
- datas exibidas para operadores;
- datas exibidas ao cliente.

O timezone operacional não altera a regra de persistência em UTC.

Caso a operação futuramente possua unidades em fusos diferentes, essa
convenção deverá ser revisada antes de implementar suporte multiunidade.

---

## 6.3 Datas e horários no PostgreSQL

Campos que representam um instante real no tempo deverão utilizar:

```text
TIMESTAMP WITH TIME ZONE
```

No PostgreSQL, normalmente representado por:

```text
timestamptz
```

Exemplos:

```text
created_at
updated_at
confirmed_at
preparation_started_at
ready_at
out_for_delivery_at
delivered_at
cancelled_at
```

Evitar:

```text
TIMESTAMP WITHOUT TIME ZONE
```

para eventos que representam um instante real.

---

## 6.4 Datas sem horário

Quando o domínio representar somente uma data, sem horário ou fuso,
utilizar o tipo:

```text
DATE
```

Exemplos possíveis:

```text
birth_date
purchase_document_date
```

Não utilizar `datetime` quando o dado de negócio representa apenas uma
data.

---

## 6.5 Horários sem data

Quando a regra representar apenas um horário recorrente, utilizar um
tipo adequado a horário sem data.

Exemplo:

```text
opening_time
closing_time
```

Esses campos representam horário operacional local e não um instante
UTC isolado.

O timezone ao qual o horário pertence deverá ser conhecido pelo
contexto da operação.

---

## 6.6 Python

No Python, utilizar objetos `datetime` conscientes de timezone
(*timezone-aware*).

Preferir:

```python
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
```

Evitar:

```python
from datetime import datetime

now = datetime.now()
```

e:

```python
datetime.utcnow()
```

O projeto não deverá utilizar `datetime` sem informação de timezone
para eventos persistidos.

---

## 6.7 SQLAlchemy

Campos que representam instantes deverão utilizar configuração com
timezone habilitado.

Exemplo conceitual:

```python
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    nullable=False,
)
```

A definição exata dos defaults será realizada quando a base dos models
for implementada.

---

## 6.8 Pydantic e contratos da API

Schemas devem utilizar:

```python
datetime
```

para valores de data e hora.

As respostas da API deverão utilizar representação ISO 8601.

Exemplo em UTC:

```text
2026-09-09T17:30:00Z
```

Também é válida uma representação equivalente com offset:

```text
2026-09-09T17:30:00+00:00
```

O backend não deverá devolver datas ambíguas como:

```text
09/09/2026 14:30
```

nos contratos da API.

Formatação amigável é responsabilidade da camada de apresentação.

---

## 6.9 Entrada de datas pela API

Quando um endpoint receber um instante no tempo, o valor deverá possuir
timezone ou offset explícito.

Aceitável:

```text
2026-09-09T14:30:00-03:00
```

ou:

```text
2026-09-09T17:30:00Z
```

Evitar aceitar como instante:

```text
2026-09-09 14:30:00
```

sem informação de timezone.

---

## 6.10 Conversão para UTC

Valores recebidos com timezone válido deverão ser normalizados para UTC
antes de serem utilizados como referência interna ou persistidos.

Exemplo:

```text
Entrada:
2026-09-09T14:30:00-03:00

Equivalente em UTC:
2026-09-09T17:30:00Z
```

A conversão não altera o instante representado.

---

## 6.11 Exibição no Aplicativo Mobile e interfaces internas

Interfaces poderão converter valores UTC para o timezone adequado antes
de exibi-los.

Para a operação padrão:

```text
America/Sao_Paulo
```

Exemplo:

```text
API:
2026-09-09T17:30:00Z

Interface:
09/09/2026 14:30
```

O backend deverá manter o valor original de referência em UTC.

---

## 6.12 Cálculo de duração

Durações operacionais deverão ser calculadas a partir de instantes
persistidos, e não de strings formatadas.

Exemplo:

```text
preparation_time =
ready_at - preparation_started_at
```

Isso será utilizado em métricas como:

- tempo de confirmação;
- tempo de preparo;
- tempo aguardando despacho;
- tempo de entrega;
- tempo total do pedido.

---

## 6.13 Histórico de status

Cada mudança relevante de status deverá possuir seu próprio instante de
ocorrência.

Exemplo conceitual:

```text
order_status_history
--------------------
id
order_id
from_status
to_status
changed_at
```

O campo:

```text
changed_at
```

deverá seguir a mesma regra de UTC e timezone-aware.

---

## 6.14 `created_at` e `updated_at`

Entidades persistidas deverão utilizar, quando aplicável:

```text
created_at
updated_at
```

Ambos deverão representar instantes UTC.

Regras:

```text
created_at
→ definido na criação

updated_at
→ atualizado quando a entidade sofrer alteração persistida
```

Não utilizar esses campos para representar eventos específicos do
domínio.

Por exemplo, não inferir:

```text
delivered_at = updated_at
```

O evento de entrega deve possuir informação própria quando necessária.

---

## 6.15 Horário de funcionamento

Horários de funcionamento são regras operacionais locais.

Exemplo:

```text
opening_time = 18:00
closing_time = 23:30
timezone = America/Sao_Paulo
```

Eles não devem ser convertidos e armazenados como um instante UTC fixo,
pois se repetem em dias diferentes.

A modelagem definitiva será decidida no módulo responsável pelas
configurações da operação.

---

## 6.16 Agrupamentos por dia

Relatórios como:

```text
faturamento do dia
pedidos de hoje
horário de pico
```

não devem simplesmente utilizar o dia UTC.

Primeiro deverá ser considerado o timezone operacional:

```text
America/Sao_Paulo
```

e depois determinado o intervalo UTC correspondente ao período local.

Isso evita que pedidos próximos da meia-noite sejam contabilizados no
dia operacional incorreto.

---

## 6.17 Testes relacionados a tempo

Testes não devem depender desnecessariamente do relógio real da máquina.

Quando uma regra depender do horário atual, preferir uma estratégia que
permita controlar ou injetar a referência temporal durante o teste.

Casos importantes a testar futuramente:

- mudança de dia;
- horários próximos da meia-noite;
- conversão entre UTC e timezone operacional;
- segmentação de clientes por quantidade de dias;
- métricas de preparação e entrega.

---

## 6.18 Regra oficial

Salvo decisão explícita e documentada em contrário:

```text
Timezone interno              → UTC
Timezone operacional padrão   → America/Sao_Paulo
PostgreSQL para instantes     → TIMESTAMPTZ
Python para instantes         → datetime timezone-aware
Formato da API                → ISO 8601
Datas sem horário             → DATE
Horários recorrentes locais   → horário + contexto de timezone
Formatação para usuário       → camada de apresentação
```

Qualquer exceção deverá ser justificada e registrada neste documento.

---

# 7. Padrões da API

## 7.1 Objetivo

Esta seção define padrões gerais de construção da API que não estão
cobertos pelas seções de Erros (`8`) e de Paginação, filtros e
ordenação (`9`).

O objetivo é evitar que cada módulo adote uma convenção diferente para
verbos HTTP, códigos de sucesso, formato de resposta de um recurso
único, autenticação e eventos em tempo real.

---

## 7.2 Verbos HTTP

O projeto utilizará os verbos HTTP de acordo com sua semântica padrão.

```text
GET     → leitura, sem efeito colateral, idempotente
POST    → criação de um recurso, ou execução de uma ação que não se
          encaixa nos demais verbos
PATCH   → atualização parcial de um recurso existente
DELETE  → remoção de um recurso
```

O projeto não utilizará `PUT`.

Atualizações, mesmo quando substituem múltiplos campos, deverão
utilizar `PATCH`.

Exemplo:

```text
POST   /customers
GET    /customers/{customer_id}
PATCH  /customers/{customer_id}
DELETE /customers/{customer_id}
```

---

## 7.3 Códigos de sucesso

```text
200 OK         → leitura ou atualização concluída com corpo de resposta
201 Created    → criação de um novo recurso
204 No Content → operação concluída sem corpo de resposta
```

Regras:

- toda criação bem-sucedida (`POST`) deverá responder `201` e devolver
  o recurso criado no corpo;
- toda remoção bem-sucedida (`DELETE`) deverá responder `204`, sem
  corpo;
- ações que não representam criação nem remoção, mas não possuem corpo
  relevante para devolver, também poderão utilizar `204`.

---

## 7.4 Formato do recurso único

Diferente da resposta de coleção (ver seção `9`), a resposta de um
recurso único não deverá utilizar um envelope adicional.

Os campos do recurso deverão aparecer diretamente na raiz da resposta.

Exemplo:

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Example Customer",
  "created_at": "2026-09-09T17:30:00Z"
}
```

Evitar:

```json
{
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  }
}
```

O envelope com `items`, `page`, `page_size`, `total` e `pages` é
exclusivo de respostas de coleção paginada, conforme definido na
seção `9`.

---

## 7.5 Idempotência

Endpoints de criação que representem uma operação sensível a
duplicação — por exemplo, criação de pedido — poderão aceitar um
cabeçalho de idempotência.

Exemplo conceitual:

```text
Idempotency-Key: <valor único gerado pelo cliente>
```

Quando esse cabeçalho for adotado por um endpoint, uma nova requisição
com a mesma chave deverá devolver o resultado da requisição original,
em vez de criar um novo recurso.

A adoção desse mecanismo é opcional e deverá ser decidida módulo a
módulo, conforme o risco de duplicação da operação.

Regras de negócio específicas sobre duplicidade de pedido continuam
registradas em `open-questions.md` e não são substituídas por esta
convenção técnica.

---

## 7.6 Versionamento da API

Para o MVP, a API não utilizará prefixo de versão.

```text
/customers
/orders
/products
```

em vez de:

```text
/v1/customers
```

Caso uma mudança incompatível seja necessária após o lançamento, a
estratégia de versionamento deverá ser definida naquele momento e
registrada nesta seção.

---

## 7.7 Autenticação

Endpoints que exigem usuário interno autenticado deverão aceitar o
token de acesso no cabeçalho padrão:

```text
Authorization: Bearer <token>
```

O token será um JWT, conforme dependência já definida no projeto
(`pyjwt`).

Requisições sem token válido para um endpoint protegido deverão
resultar no erro `UNAUTHORIZED` (`401`), conforme seção `8`.

A estratégia de autenticação do cliente final no Aplicativo Mobile
ainda não está definida e permanece registrada como dúvida aberta em
`open-questions.md` (`Q-APP-002`). Esta seção trata apenas da
autenticação dos usuários internos (Administrador, Gestor, Cozinha,
Expedição, Atendimento, Estoque).

---

## 7.8 Eventos em tempo real

O Guia funcional exige que informações operacionais estejam
disponíveis em tempo real (`RNF-001`).

O canal técnico adotado para isso será WebSocket.

Toda mensagem enviada pelo servidor deverá seguir um envelope comum:

```json
{
  "event": "order.status_changed",
  "data": {},
  "occurred_at": "2026-09-09T17:30:00Z"
}
```

Campos:

```text
event        → nome do evento, no formato <entidade>.<ação>
data         → conteúdo específico do evento
occurred_at  → instante do evento, UTC, ISO 8601
```

Nomes de evento deverão utilizar `snake_case` para a ação, e ponto
(`.`) para separar entidade e ação.

Exemplos:

```text
order.created
order.status_changed
ingredient.below_minimum
```

A definição de quais eventos existirão, e quais telas os consumirão,
será detalhada durante a implementação de cada módulo. Esta seção
define apenas o formato comum da mensagem.

---

## 7.9 Health check

O endpoint:

```text
GET /health
```

não deverá exigir autenticação e deverá responder rapidamente,
indicando que a aplicação está no ar.

Exemplo:

```json
{
  "status": "ok"
}
```

Este endpoint é utilizado por mecanismos de verificação de
disponibilidade da infraestrutura (ex.: Railway) e não deverá executar
verificações custosas, como testar a conexão com serviços externos,
salvo decisão explícita em contrário.

---

## 7.10 Regra oficial

Salvo decisão explícita e documentada em contrário:

```text
Verbos permitidos     → GET, POST, PATCH, DELETE
Verbo evitado         → PUT
Criação               → 201 + corpo do recurso criado
Remoção               → 204 sem corpo
Recurso único         → campos na raiz, sem envelope "data"
Coleção               → envelope definido na seção 9
Idempotência          → opcional, via header Idempotency-Key
Versionamento no MVP  → nenhum (sem prefixo /v1/)
Autenticação interna  → Authorization: Bearer <token> (JWT)
Autenticação do app   → pendente (Q-APP-002)
Tempo real            → WebSocket, envelope { event, data, occurred_at }
Nome de evento        → <entidade>.<acao_em_snake_case>
Health check          → GET /health, sem autenticação
```

Qualquer exceção deverá ser justificada e registrada neste documento.

---

# 8. Erros da API

## 8.1 Objetivo

Todos os erros retornados pela API deverão possuir um formato
previsível.

O frontend, o Aplicativo Mobile e integrações não deverão precisar
interpretar diferentes formatos de erro dependendo do endpoint.

A estrutura padrão será:

```json
{
  "code": "ERROR_CODE",
  "message": "Mensagem legível.",
  "details": null
}
```

Campos obrigatórios:

```text
code
message
details
```

---

## 8.2 Campo `code`

`code` representa um identificador estável e legível por máquina.

Deverá utilizar:

```text
UPPER_SNAKE_CASE
```

Exemplos:

```text
CUSTOMER_NOT_FOUND
PRODUCT_NOT_FOUND
INSUFFICIENT_STOCK
INVALID_ORDER_STATUS_TRANSITION
CUSTOMER_CPF_ALREADY_EXISTS
PAYMENT_NOT_APPROVED
FORBIDDEN
UNAUTHORIZED
```

O frontend poderá utilizar `code` para decidir comportamentos
específicos.

Exemplo:

```text
code = INSUFFICIENT_STOCK
→ informar ao cliente que o item não está mais disponível
```

A lógica do frontend não deverá depender do texto de `message`.

---

## 8.3 Campo `message`

`message` deverá possuir uma descrição legível do problema.

Para o MVP, as mensagens retornadas pela API poderão ser escritas em
português brasileiro.

Exemplo:

```json
{
  "code": "PRODUCT_NOT_FOUND",
  "message": "Produto não encontrado.",
  "details": null
}
```

Mensagens devem:

- ser objetivas;
- não conter stack trace;
- não expor informações internas;
- não expor SQL;
- não expor segredos;
- não expor detalhes desnecessários da infraestrutura.

Evitar mensagens como:

```text
sqlalchemy.exc.IntegrityError...
relation "customers" does not exist...
KeyError at app/modules/orders/service.py line 87...
```

---

## 8.4 Campo `details`

`details` deverá carregar informações adicionais quando forem úteis
para entender ou tratar o erro.

Quando não houver informação adicional:

```json
{
  "code": "PRODUCT_NOT_FOUND",
  "message": "Produto não encontrado.",
  "details": null
}
```

Quando houver:

```json
{
  "code": "INSUFFICIENT_STOCK",
  "message": "Estoque insuficiente para concluir o pedido.",
  "details": {
    "ingredient_id": "550e8400-e29b-41d4-a716-446655440000",
    "required": 5,
    "available": 2
  }
}
```

O conteúdo de `details` poderá variar conforme o erro, mas deverá
continuar serializável em JSON.

---

## 8.5 Erros de validação de entrada

Erros gerados pela validação dos schemas deverão ser normalizados para
o padrão da Waves.

Exemplo:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Os dados enviados são inválidos.",
  "details": [
    {
      "field": "quantity",
      "message": "O valor deve ser maior que zero."
    }
  ]
}
```

O formato interno padrão do FastAPI/Pydantic não deverá vazar
diretamente caso seja diferente do contrato definido pelo projeto.

---

## 8.6 Códigos HTTP

O status HTTP deverá representar corretamente a categoria do erro.

### `400 Bad Request`

Utilizar quando a requisição é inválida de forma geral e não existe um
status mais específico.

Exemplo:

```text
INVALID_REQUEST
```

---

### `401 Unauthorized`

Utilizar quando não existe autenticação válida.

Exemplo:

```json
{
  "code": "UNAUTHORIZED",
  "message": "Autenticação necessária.",
  "details": null
}
```

---

### `403 Forbidden`

Utilizar quando o usuário está autenticado, mas não possui permissão
para executar a ação.

Exemplo:

```json
{
  "code": "FORBIDDEN",
  "message": "Você não possui permissão para executar esta ação.",
  "details": null
}
```

---

### `404 Not Found`

Utilizar quando um recurso solicitado não existe ou não pode ser
localizado.

Exemplos:

```text
CUSTOMER_NOT_FOUND
ORDER_NOT_FOUND
PRODUCT_NOT_FOUND
INGREDIENT_NOT_FOUND
```

---

### `409 Conflict`

Utilizar quando a operação entra em conflito com o estado atual do
recurso ou com uma restrição de unicidade/regra já existente.

Exemplos:

```text
CUSTOMER_CPF_ALREADY_EXISTS
USER_EMAIL_ALREADY_EXISTS
INVALID_ORDER_STATUS_TRANSITION
ORDER_ALREADY_CANCELLED
```

---

### `422 Unprocessable Entity`

Utilizar para erros de validação semântica dos dados enviados quando a
estrutura da requisição é válida, mas os valores não podem ser aceitos.

Exemplos:

```text
VALIDATION_ERROR
INVALID_QUANTITY
INVALID_DATE_RANGE
```

Também será o status normalizado para erros de validação de entrada
produzidos pelo FastAPI/Pydantic.

---

### `500 Internal Server Error`

Utilizar somente para falhas inesperadas que não foram tratadas por uma
regra conhecida.

Resposta pública:

```json
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Ocorreu um erro interno inesperado.",
  "details": null
}
```

O erro técnico completo deverá ser registrado nos logs, e não devolvido
ao cliente.

---

## 8.7 Exceções de domínio

A aplicação deverá possuir exceções próprias para representar erros
esperados do domínio.

Exemplos conceituais:

```python
class DomainError(Exception):
    ...

class NotFoundError(DomainError):
    ...

class ConflictError(DomainError):
    ...

class BusinessRuleError(DomainError):
    ...
```

As regras de negócio não deverão levantar diretamente exceções de
framework como forma principal de controle.

Preferir:

```python
raise NotFoundError(
    code="PRODUCT_NOT_FOUND",
    message="Produto não encontrado.",
)
```

em vez de espalhar:

```python
raise HTTPException(...)
```

por toda a camada de serviço.

A conversão da exceção de domínio para HTTP deverá acontecer na camada
da API / tratamento global de exceções.

---

## 8.8 Separação entre domínio e HTTP

Services e regras de negócio não deverão conhecer detalhes
desnecessários do protocolo HTTP.

Exemplo conceitual:

```text
OrderService
    ↓
levanta BusinessRuleError
    ↓
exception handler
    ↓
transforma em HTTP 409
    ↓
resposta JSON padronizada
```

Isso permite reutilizar a regra de negócio fora de um endpoint HTTP no
futuro.

---

## 8.9 Tratamento global

O FastAPI deverá possuir handlers globais para transformar erros
conhecidos no contrato padrão.

Deverão ser normalizados pelo menos:

- erros de domínio;
- recurso não encontrado;
- conflitos;
- erros de validação Pydantic/FastAPI;
- autenticação;
- autorização;
- falhas inesperadas.

Não deverá ser necessário repetir a construção da resposta de erro em
cada endpoint.

---

## 8.10 Erros de banco de dados

Erros técnicos do PostgreSQL ou SQLAlchemy não deverão ser enviados
diretamente ao cliente.

Exemplo:

Uma violação de unicidade de CPF poderá ocorrer tecnicamente como uma
constraint do banco.

A API deverá convertê-la para algo como:

```json
{
  "code": "CUSTOMER_CPF_ALREADY_EXISTS",
  "message": "Já existe um cliente cadastrado com este CPF.",
  "details": null
}
```

O cliente da API não deverá precisar conhecer PostgreSQL, SQLAlchemy ou
nomes internos de constraints para interpretar o problema.

---

## 8.11 Erros de integrações externas

Falhas de serviços externos deverão ser traduzidas para erros do
domínio da Waves.

Exemplos futuros:

```text
PAYMENT_PROVIDER_UNAVAILABLE
PAYMENT_NOT_APPROVED
DELIVERY_PROVIDER_UNAVAILABLE
DELIVERY_QUOTE_FAILED
WHATSAPP_PROVIDER_UNAVAILABLE
```

Não devolver diretamente ao Aplicativo Mobile a resposta bruta do
provedor externo.

---

## 8.12 Catálogo de códigos de erro

Cada módulo poderá possuir seu conjunto de códigos, mantendo nomes
claros e não ambíguos.

Exemplo:

### Clientes

```text
CUSTOMER_NOT_FOUND
CUSTOMER_CPF_ALREADY_EXISTS
```

### Pedidos

```text
ORDER_NOT_FOUND
INVALID_ORDER_STATUS_TRANSITION
ORDER_CANNOT_BE_CANCELLED
```

### Estoque

```text
INGREDIENT_NOT_FOUND
INSUFFICIENT_STOCK
INVALID_STOCK_ADJUSTMENT
```

### Produtos

```text
PRODUCT_NOT_FOUND
PRODUCT_UNAVAILABLE
```

Evitar códigos genéricos quando o domínio puder ser identificado.

Evitar:

```text
NOT_FOUND
INVALID
ERROR
FAILED
```

quando um código mais específico puder ser utilizado.

---

## 8.13 Consistência entre endpoints

O mesmo erro conceitual deverá utilizar o mesmo `code`,
independentemente do endpoint que o produziu.

Exemplo:

Se um produto não existe:

```text
PRODUCT_NOT_FOUND
```

deve ser utilizado de forma consistente em:

```text
GET /products/{product_id}
POST /orders
PATCH /products/{product_id}
```

quando a causa real for a mesma.

---

## 8.14 Logs

Erros inesperados deverão ser registrados nos logs com informações
suficientes para diagnóstico.

Os logs poderão conter informações técnicas que não são devolvidas ao
cliente.

Segredos, senhas, tokens completos e dados sensíveis não deverão ser
registrados em logs.

A estratégia completa de logging será definida na fundação técnica.

---

## 8.15 Regra oficial

Salvo decisão explícita e documentada em contrário:

```text
Formato do erro      → code + message + details
code                  → UPPER_SNAKE_CASE
message               → legível e segura
details               → null, objeto ou lista JSON
Validação             → 422
Não autenticado       → 401
Sem permissão         → 403
Não encontrado        → 404
Conflito              → 409
Erro inesperado       → 500
Domínio               → exceções próprias
HTTPException         → evitar nas regras de negócio
Stack trace no cliente→ nunca
```

Qualquer exceção deverá ser justificada e registrada neste documento.

---

# 9. Paginação, filtros e ordenação

## 9.1 Objetivo

Endpoints que retornam coleções deverão seguir um padrão único para:

- paginação;
- filtros;
- ordenação;
- metadados da resposta.

O objetivo é evitar que cada módulo implemente listagens de forma
diferente.

---

## 9.2 Paginação padrão

A paginação padrão da API será baseada em:

```text
page
page_size
```

Exemplo:

```http
GET /customers?page=1&page_size=20
```

Regras:

```text
page       → começa em 1
page_size  → quantidade de itens por página
```

Não utilizar índice de página começando em `0` na API pública.

---

## 9.3 Valores padrão

Quando os parâmetros não forem informados:

```text
page       → 1
page_size  → 20
```

Limite máximo inicial:

```text
MAX_PAGE_SIZE → 100
```

Portanto:

```http
GET /customers
```

deverá ser equivalente a:

```http
GET /customers?page=1&page_size=20
```

---

## 9.4 Validação da paginação

Os parâmetros deverão respeitar:

```text
page >= 1
1 <= page_size <= 100
```

Valores inválidos deverão retornar erro de validação no padrão definido
na seção de erros da API.

Exemplo:

```http
GET /customers?page=0
```

deverá resultar em um erro de validação.

---

## 9.5 Estrutura da resposta paginada

A resposta padrão deverá seguir:

```json
{
  "items": [],
  "page": 1,
  "page_size": 20,
  "total": 0,
  "pages": 0
}
```

Campos:

```text
items      → registros da página atual
page       → página atual
page_size  → tamanho solicitado da página
total      → total de registros após aplicação dos filtros
pages      → quantidade total de páginas
```

Exemplo:

```json
{
  "items": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "Example Customer"
    }
  ],
  "page": 1,
  "page_size": 20,
  "total": 43,
  "pages": 3
}
```

---

## 9.6 Cálculo de páginas

A quantidade de páginas deverá considerar:

```text
pages = ceil(total / page_size)
```

Quando:

```text
total = 0
```

a resposta deverá utilizar:

```text
pages = 0
```

---

## 9.7 Nome do schema paginado

Quando forem criados schemas reutilizáveis, utilizar nomes claros.

Exemplo conceitual:

```python
PaginatedResponse[CustomerRead]
```

ou uma abordagem equivalente compatível com Pydantic.

O formato público da resposta deverá permanecer:

```text
items
page
page_size
total
pages
```

independentemente da implementação interna escolhida.

---

## 9.8 Filtros

Filtros deverão ser enviados por query parameters.

Exemplos:

```http
GET /products?active=true
GET /orders?customer_id=<uuid>
GET /orders?status=preparing
GET /ingredients?below_minimum=true
```

Os nomes dos filtros deverão utilizar:

```text
snake_case
```

---

## 9.9 Filtros opcionais

Por padrão, filtros serão opcionais.

Quando um filtro não for informado, ele não deverá restringir a
consulta.

Exemplo:

```http
GET /orders
```

não deverá assumir silenciosamente:

```text
status=received
```

a menos que um endpoint específico seja explicitamente projetado para
essa finalidade.

---

## 9.10 Filtros por múltiplos campos

Quando necessário, diferentes filtros poderão ser combinados.

Exemplo:

```http
GET /orders?status=delivered&customer_id=<uuid>
```

A regra padrão será:

```text
filtro A AND filtro B
```

Ou seja, o registro deverá atender aos filtros informados
simultaneamente.

Comportamentos diferentes deverão ser documentados no endpoint.

---

## 9.11 Busca textual

Quando um recurso possuir busca textual, utilizar o parâmetro:

```text
search
```

Exemplo:

```http
GET /customers?search=lucas
```

A interpretação exata da busca deverá ser definida pelo módulo.

Exemplos possíveis:

- nome;
- e-mail;
- telefone;
- CPF, quando apropriado e permitido.

O endpoint deverá documentar quais campos são pesquisados.

Não criar parâmetros diferentes sem necessidade, como:

```text
q
query
term
keyword
search_text
```

para representar a mesma operação.

O padrão será:

```text
search
```

---

## 9.12 Filtros por datas

Filtros por intervalo de datas deverão possuir nomes claros.

Padrão recomendado:

```text
created_from
created_to
```

Exemplo:

```http
GET /orders?created_from=2026-09-01T00:00:00-03:00&created_to=2026-09-30T23:59:59-03:00
```

Os valores deverão seguir as convenções de datas e horários deste
documento.

Quando o domínio exigir outro campo temporal, utilizar o mesmo padrão.

Exemplo:

```text
delivered_from
delivered_to
```

---

## 9.13 Intervalos de datas

Por padrão:

```text
*_from → limite inicial inclusivo
*_to   → limite final inclusivo ou semanticamente documentado pelo endpoint
```

Antes da implementação dos filtros temporais, a regra exata de borda
deverá ser consistente no projeto e coberta por testes.

Para filtros de períodos de dashboard, poderá ser utilizada uma
abordagem específica desde que documentada.

---

## 9.14 Ordenação

A ordenação deverá utilizar o parâmetro:

```text
sort
```

Exemplo ascendente:

```http
GET /products?sort=name
```

Exemplo descendente:

```http
GET /products?sort=-created_at
```

Regra:

```text
campo        → ascendente
-campo       → descendente
```

---

## 9.15 Campos permitidos para ordenação

Cada endpoint deverá possuir uma lista explícita de campos permitidos.

Exemplo para pedidos:

```text
created_at
updated_at
total_amount
status
```

Não permitir que o cliente envie arbitrariamente qualquer nome de
coluna do banco.

Isso evita:

- comportamento imprevisível;
- acoplamento ao schema interno;
- problemas de segurança;
- consultas desnecessariamente caras.

---

## 9.16 Ordenação inválida

Caso o cliente solicite um campo não permitido:

```http
GET /orders?sort=internal_secret_column
```

a API deverá retornar erro de validação.

Exemplo conceitual:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Os dados enviados são inválidos.",
  "details": [
    {
      "field": "sort",
      "message": "Campo de ordenação não permitido."
    }
  ]
}
```

---

## 9.17 Ordenação padrão

Cada listagem deverá possuir uma ordenação padrão determinística.

Exemplos possíveis:

```text
customers → created_at desc
products  → name asc
orders    → created_at desc
```

A ordenação padrão de cada recurso deverá ser definida no módulo.

Não depender da ordem natural retornada pelo PostgreSQL.

---

## 9.18 Critério de desempate

Quando o campo principal de ordenação puder possuir valores repetidos,
utilizar um critério adicional determinístico.

Exemplo conceitual:

```text
ORDER BY created_at DESC, id DESC
```

Isso evita alterações imprevisíveis entre páginas.

---

## 9.19 Combinação de paginação, filtros e ordenação

Os três mecanismos deverão funcionar em conjunto.

Exemplo:

```http
GET /orders?status=delivered&sort=-created_at&page=2&page_size=20
```

A sequência conceitual será:

```text
consulta base
→ aplicar filtros
→ calcular total
→ aplicar ordenação
→ aplicar paginação
→ retornar resposta
```

O campo:

```text
total
```

deverá representar o total **depois dos filtros** e **antes da
paginação**.

---

## 9.20 Paginação de coleções pequenas

Mesmo que uma coleção seja pequena no início do projeto, endpoints de
listagem que possam crescer deverão adotar paginação desde sua criação.

Exemplos:

```text
customers
orders
products
ingredients
suppliers
purchases
inventory_movements
```

Isso evita mudanças de contrato no futuro.

---

## 9.21 Endpoints sem paginação

Coleções pequenas, fechadas ou de natureza configuracional poderão
retornar listas sem paginação quando houver justificativa clara.

Exemplos possíveis:

- enumerações;
- opções fixas;
- listas muito pequenas e limitadas por regra de negócio.

A exceção deverá ser intencional, não resultado de esquecimento.

---

## 9.22 Limites de `page_size`

O cliente não poderá solicitar quantidades ilimitadas.

Padrão:

```text
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
```

Esses valores deverão ser centralizados para evitar números diferentes
espalhados pelo código.

---

## 9.23 Performance

Listagens deverão ser projetadas para evitar:

- carregar todos os registros em memória antes de paginar;
- N+1 queries;
- ordenação por campos não indexáveis sem necessidade;
- filtros não controlados;
- consultas excessivamente amplas.

A paginação deverá acontecer no banco sempre que os dados forem
persistidos no PostgreSQL.

---

## 9.24 Índices

Campos frequentemente utilizados em:

- filtros;
- ordenação;
- busca;
- foreign keys;

deverão ser avaliados para criação de índices.

A criação de índice não será automática para todo filtro.

Cada índice deverá considerar:

- frequência da consulta;
- cardinalidade;
- custo de escrita;
- tamanho da tabela.

---

## 9.25 Regra para endpoints do Dashboard

Endpoints analíticos do Dashboard poderão possuir contratos diferentes
de uma listagem CRUD.

Exemplo:

```http
GET /dashboard/sales
```

poderá retornar métricas agregadas em vez de:

```text
items + page + page_size + total + pages
```

Isso não viola a convenção, pois não representa uma coleção paginada de
entidades.

Filtros de período desses endpoints deverão continuar utilizando
parâmetros consistentes.

---

## 9.26 Regra oficial

Salvo decisão explícita e documentada em contrário:

```text
Página inicial             → 1
Tamanho padrão             → 20
Tamanho máximo             → 100
Parâmetro da página        → page
Parâmetro do tamanho       → page_size
Busca textual              → search
Ordenação                  → sort
Ascendente                 → sort=field
Descendente                → sort=-field
Campos JSON                → snake_case
Resposta paginada          → items, page, page_size, total, pages
Filtros                    → query parameters
Múltiplos filtros          → AND
Ordenação padrão           → determinística
Paginação                  → realizada no banco
```

Qualquer exceção deverá ser justificada e registrada neste documento.

---

# 10. Observação

Este documento é evolutivo.

Sempre que uma nova convenção for aprovada para o projeto, ela deve ser
registrada aqui antes de ser tratada como padrão obrigatório pela equipe.
