# Lista de Exercícios Práticos – Strings e Listas em Python

Este material reúne exercícios práticos sobre:

- manipulação de strings;
- listas;
- indexação;
- fatiamento;
- iteração com `for`;
- busca simples;
- modelagem inicial com coleções lineares.

## Objetivos

- praticar operações básicas com o tipo `str`;
- compreender como listas armazenam e organizam dados;
- usar índice e slicing para acessar partes de sequências;
- percorrer dados com `for`;
- resolver problemas simples de busca e filtragem;
- escolher entre string e lista de acordo com o problema.

## Organização sugerida do repositório

```text
.
├── README.md
├── exercicios/
│   ├── ex01_padronizacao_nomes.py
│   ├── ex02_split_join.py
│   ├── ex03_indexacao.py
│   ├── ex04_fatiamento.py
│   ├── ex05_percurso_for.py
│   ├── ex06_range_len.py
│   ├── ex07_busca_linear.py
│   ├── ex08_contagem.py
│   ├── ex09_append.py
│   ├── ex10_filtragem_notas.py
│   ├── ex11_presenca.py
│   ├── ex12_modelagem.py
│   ├── ex13_correcao_erros.py
│   └── ex14_projeto_integrador.py
└── respostas/
    └── (opcional)
```

## Exercícios

### 1. Limpeza e padronização de nomes

**Objetivo:** Aplicar strip() e title() para padronizar entradas textuais.

**Enunciado:** Dada a lista abaixo, crie um programa que gere uma nova lista com todos os nomes sem espaços sobrando nas extremidades e com inicial maiúscula em cada palavra.

**Dados sugeridos:**

```python
nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]
```

**Tarefas:**
1. Crie uma lista chamada nomes_padronizados.
1. Percorra a lista original com for.
1. Aplique as operações de limpeza e padronização.
1. Exiba a lista final.

**Desafio opcional:** Mostre também quantos nomes existem na lista final.

### 2. Separando e reunindo texto

**Objetivo:** Usar split() e join() em strings.

**Enunciado:** Leia o nome completo de uma pessoa em uma variável e produza duas saídas: uma lista com as partes do nome e outra string com as partes unidas por hífen.

**Dados sugeridos:**

```python
nome_completo = "Maria Clara Souza"
```

**Tarefas:**
1. Separe o texto em partes usando split().
1. Exiba a lista resultante.
1. Monte uma nova string usando join() com o separador "-".
1. Exiba o texto final.

**Desafio opcional:** Exiba também apenas o primeiro nome e o último sobrenome.

### 3. Indexação em strings e listas

**Objetivo:** Praticar acesso posicional em sequências.

**Enunciado:** Utilize indexação para acessar posições específicas em uma string e em uma lista.

**Dados sugeridos:**

```python
palavra = "algoritmo"
notas = [7.0, 8.5, 6.0, 9.0, 7.5]
```

**Tarefas:**
1. Mostre a primeira letra da palavra.
1. Mostre a quarta letra da palavra.
1. Mostre a primeira nota da lista.
1. Mostre a última nota da lista usando indexação.

**Desafio opcional:** Explique, em comentário, por que o primeiro índice é 0.

### 4. Fatiamento de sequências

**Objetivo:** Extrair partes de strings e listas com slicing.

**Enunciado:** Crie recortes de uma palavra e de uma lista de números para observar como o fatiamento funciona.

**Dados sugeridos:**

```python
palavra = "programacao"
valores = [10, 20, 30, 40, 50, 60]
```

**Tarefas:**
1. Exiba os 4 primeiros caracteres da palavra.
1. Exiba os caracteres da posição 4 até a 8.
1. Exiba os três primeiros elementos da lista.
1. Exiba os elementos da posição 2 até o final da lista.

**Desafio opcional:** Teste outros recortes e registre, em comentário, o que você observou.

### 5. Percurso simples com for

**Objetivo:** Percorrer sequências item a item.

**Enunciado:** Crie um programa que percorra uma lista de frutas e exiba uma mensagem para cada item.

**Dados sugeridos:**

```python
frutas = ["maçã", "banana", "uva", "pera"]
```

**Tarefas:**
1. Percorra a lista com for.
1. Exiba uma frase no formato: Eu gosto de <fruta>.
1. Ao final, exiba a quantidade de frutas percorridas.

**Desafio opcional:** Repita a ideia percorrendo cada letra da palavra "Python".

### 6. Percurso por índice

**Objetivo:** Combinar range() com len() para acessar posição e valor.

**Enunciado:** Mostre a posição e o conteúdo de cada elemento da lista de alunos.

**Dados sugeridos:**

```python
alunos = ["Ana", "Bruno", "Carla", "Daniel"]
```

**Tarefas:**
1. Use for com range(len(alunos)).
1. Exiba a posição e o nome do aluno correspondente.
1. Mantenha a saída organizada e legível.

**Desafio opcional:** Mostre a saída no formato: Índice 0 -> Ana.

### 7. Busca linear de um elemento

**Objetivo:** Implementar busca simples com for e condição.

**Enunciado:** Verifique se um nome procurado está presente em uma lista de estudantes.

**Dados sugeridos:**

```python
estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"
```

**Tarefas:**
1. Crie uma variável booleana para indicar se o nome foi encontrado.
1. Percorra a lista com for.
1. Compare cada item com o nome procurado.
1. Interrompa o laço quando encontrar o elemento.
1. Exiba o resultado final.

**Desafio opcional:** Troque o valor procurado por um nome inexistente e teste novamente.

### 8. Contagem de ocorrências

**Objetivo:** Trabalhar com repetição de valores em listas.

**Enunciado:** Descubra quantas vezes determinado item aparece em uma lista.

**Dados sugeridos:**

```python
itens = ["mouse", "teclado", "mouse", "monitor", "mouse", "teclado"]
```

**Tarefas:**
1. Conte quantas vezes "mouse" aparece.
1. Conte quantas vezes "teclado" aparece.
1. Exiba os resultados com frases completas.

**Desafio opcional:** Faça o mesmo com outro item de sua escolha.

### 9. Construção incremental de listas

**Objetivo:** Criar e preencher listas com append().

**Enunciado:** Monte uma lista de tarefas acadêmicas usando uma lista vazia e o método append().

**Dados sugeridos:**

```python
Sugestão de itens: estudar Python, resolver exercícios, revisar código, enviar atividade.
```

**Tarefas:**
1. Crie uma lista vazia.
1. Adicione pelo menos quatro tarefas.
1. Exiba a lista final.
1. Exiba também o total de tarefas cadastradas.

**Desafio opcional:** Adicione uma quinta tarefa escolhida por você.

### 10. Filtragem de notas

**Objetivo:** Usar for + if + append() para produzir uma nova coleção.

**Enunciado:** A partir da lista de notas, gere uma nova lista contendo apenas as notas maiores ou iguais a 7,0.

**Dados sugeridos:**

```python
notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]
```

**Tarefas:**
1. Crie uma lista chamada aprovados.
1. Percorra a lista de notas.
1. Adicione somente as notas aprovadas.
1. Exiba a lista final de aprovados.

**Desafio opcional:** Exiba também a quantidade de estudantes aprovados.

### 11. Cadastro simples de presença

**Objetivo:** Integrar strings, listas e busca linear em um problema aplicado.

**Enunciado:** Uma turma possui nomes digitados com inconsistências. Padronize os dados e verifique se um estudante específico está presente.

**Dados sugeridos:**

```python
presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"
```

**Tarefas:**
1. Crie uma nova lista com os nomes padronizados.
1. Padronize também o nome da consulta.
1. Verifique se o estudante consultado está na lista.
1. Exiba a lista final e a mensagem de presença ou ausência.

**Desafio opcional:** Teste o programa com outro nome de consulta que não esteja presente.

### 12. Modelagem inicial com coleções lineares

**Objetivo:** Decidir quando usar string e quando usar lista.

**Enunciado:** Analise cada situação abaixo e escreva, em comentário no código, se o dado deve ser modelado como string ou lista. Em seguida, crie uma variável de exemplo para cada caso.

**Dados sugeridos:**

```python
Situações: (a) nome completo de um aluno; (b) notas de quatro avaliações; (c) comentário escrito pelo professor; (d) tarefas de um projeto; (e) código de matrícula.
```

**Tarefas:**
1. Classifique cada item como string ou lista.
1. Crie uma variável de exemplo para cada situação.
1. Justifique sua escolha com um comentário curto.

**Desafio opcional:** Adicione duas novas situações criadas por você.

### 13. Erros comuns e correção

**Objetivo:** Reconhecer problemas frequentes ao manipular listas.

**Enunciado:** Analise os trechos abaixo, explique o problema e reescreva cada um corretamente.

**Dados sugeridos:**

```python
a) lista = [3, 1, 2]
   resultado = lista.sort()
   print(resultado)

b) nomes = ["Ana", "Bruno"]
   print(nomes[5])
```

**Tarefas:**
1. Explique por que o primeiro trecho imprime None.
1. Corrija o primeiro trecho.
1. Explique o erro do segundo trecho.
1. Reescreva o segundo trecho de forma segura.

**Desafio opcional:** Crie um terceiro exemplo de erro envolvendo listas ou strings e corrija-o.

### 14. Projeto integrador curto

**Objetivo:** Consolidar o conteúdo em uma atividade final mais completa.

**Enunciado:** Desenvolva um programa que: (1) padronize nomes de estudantes; (2) filtre notas aprovadas; (3) verifique a presença de um nome consultado; e (4) exiba um pequeno relatório final.

**Dados sugeridos:**

```python
Você pode reutilizar os dados dos exercícios anteriores ou criar novos conjuntos de exemplo.
```

**Tarefas:**
1. Organize o código em etapas bem identificadas.
1. Use pelo menos uma operação de string.
1. Use pelo menos uma lista criada ou preenchida no programa.
1. Use percurso com for.
1. Use busca simples ou filtragem.
1. Exiba um relatório final legível.

**Desafio opcional:** Inclua comentários explicando a lógica de cada etapa do programa.

## Critérios de revisão

Ao finalizar os exercícios, verifique se o seu código:

- executa sem erro;
- usa nomes de variáveis claros;
- apresenta saída coerente com o enunciado;
- aplica corretamente strings, listas e laços `for`;
- evita soluções desnecessariamente complexas.

## Sugestão de progressão

1. Resolva primeiro os exercícios 1 a 5 para fixar operações básicas.
2. Em seguida, faça os exercícios 6 a 10 para consolidar percurso, busca e filtragem.
3. Termine com os exercícios 11 a 14, que integram modelagem e aplicação prática.

## Licença de uso didático

Material preparado para apoio a aulas introdutórias de Python. Adapte livremente para fins educacionais.