# Lista de Exercícios Práticos para Laboratório
## Matrizes e Listas Bidimensionais em Python

**Tema:** Matrizes / listas bidimensionais em nível introdutório  
**Linguagem:** Python  
**Formato:** Laboratório prático  
**Carga sugerida:** 2 a 3 horas  
**Entrega sugerida:** arquivos `.py` organizados por exercício ou um único notebook com seções identificadas.

---

## 1. Objetivos da prática

Ao final desta lista, o estudante deverá ser capaz de:

- criar matrizes usando listas de listas;
- acessar valores por meio de índices duplos no formato `matriz[linha][coluna]`;
- alterar valores em posições específicas;
- percorrer matrizes com laços aninhados;
- calcular somas, médias, contagens, maiores e menores valores;
- representar boletins, grades de assentos, controle de presença e pequenas simulações;
- identificar erros comuns, como índice fora dos limites e matriz irregular.

---

## 2. Orientações para o laboratório

1. Crie uma pasta chamada `laboratorio_matrizes`.
2. Para cada exercício, crie um arquivo `.py` com nome padronizado, por exemplo: `ex01_criar_matriz.py`.
3. Execute o código após cada pequena alteração.
4. Use nomes de variáveis claros, como `linha`, `coluna`, `notas`, `sala`, `presencas`, `boletim`.
5. Evite copiar soluções prontas. O objetivo é praticar o raciocínio por linhas e colunas.
6. Ao final de cada exercício, escreva um comentário no código respondendo: **o que representa cada linha e cada coluna?**

---

## 3. Exercícios práticos

---

## Exercício 1 — Criando e exibindo uma matriz 3x3

**Objetivo:** criar uma matriz simples e exibir suas linhas.

Crie um programa chamado `ex01_criar_matriz.py` que:

1. Declare a matriz abaixo:

```python
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

2. Exiba a matriz linha por linha.
3. Ao final, imprima a quantidade de linhas e a quantidade de colunas.

**Saída esperada aproximada:**

```text
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
Linhas: 3
Colunas: 3
```

**Desafio extra:** exiba a matriz sem colchetes, no formato de tabela.

---

## Exercício 2 — Acessando posições específicas

**Objetivo:** praticar o acesso com `matriz[linha][coluna]`.

Usando a matriz do exercício anterior, crie um programa que exiba:

1. O valor da primeira linha e primeira coluna.
2. O valor da segunda linha e terceira coluna.
3. O valor da terceira linha e segunda coluna.
4. A segunda linha completa.

**Pergunta obrigatória no comentário final:** por que `matriz[1][2]` não representa a primeira linha e segunda coluna?

---

## Exercício 3 — Alterando valores da matriz

**Objetivo:** modificar valores em posições específicas.

Crie um programa que:

1. Declare a matriz:

```python
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0]
]
```

2. Exiba a matriz antes da alteração.
3. Altere `notas[1][0]` para `6.5`.
4. Altere `notas[2][2]` para `9.5`.
5. Exiba a matriz depois da alteração.

**Desafio extra:** peça ao usuário uma linha, uma coluna e um novo valor; atualize a célula informada.

---

## Exercício 4 — Percorrendo uma matriz por valor

**Objetivo:** usar laços aninhados sem índices explícitos.

Crie um programa que percorra a matriz abaixo e imprima todos os valores, um por linha:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Restrição:** neste exercício, não use `range(len(...))`.

**Saída esperada aproximada:**

```text
Valor: 1
Valor: 2
Valor: 3
...
```

---

## Exercício 5 — Percorrendo uma matriz por índice

**Objetivo:** exibir linha, coluna e valor de cada elemento.

Usando a matriz do exercício 4, crie um programa que imprima cada elemento no formato:

```text
Linha 0 Coluna 0 Valor 1
Linha 0 Coluna 1 Valor 2
Linha 0 Coluna 2 Valor 3
...
```

**Restrição:** use `range(len(matriz))` e `range(len(matriz[linha]))`.

**Pergunta obrigatória no comentário final:** em que situações o percurso por índice é mais útil que o percurso por valor?

---

## Exercício 6 — Soma total dos elementos

**Objetivo:** usar acumulador em uma matriz.

Crie um programa que calcule a soma de todos os valores da matriz:

```python
valores = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 8, 9]
]
```

O programa deve exibir:

```text
Soma total: 45
```

**Desafio extra:** calcule também a média geral dos elementos.

---

## Exercício 7 — Contando números pares e ímpares

**Objetivo:** aplicar condição dentro de laços aninhados.

Usando a matriz do exercício 6, crie um programa que conte:

1. Quantos números pares existem.
2. Quantos números ímpares existem.

**Saída esperada aproximada:**

```text
Pares: 4
Ímpares: 5
```

**Desafio extra:** armazene os pares em uma lista chamada `pares_encontrados`.

---

## Exercício 8 — Maior e menor valor da matriz

**Objetivo:** localizar extremos em uma lista bidimensional.

Crie um programa que encontre o maior e o menor valor da matriz:

```python
numeros = [
    [12, 5, 8],
    [9, 21, 3],
    [14, 6, 18]
]
```

O programa deve exibir:

```text
Maior valor: 21
Menor valor: 3
```

**Desafio extra:** exiba também a posição do maior e do menor valor.

---

## Exercício 9 — Maior valor e sua posição

**Objetivo:** combinar busca com controle de índices.

Usando a matriz do exercício 8, crie um programa que mostre:

1. O maior valor.
2. A linha em que ele está.
3. A coluna em que ele está.

**Saída esperada:**

```text
Maior valor: 21
Linha: 1
Coluna: 1
```

**Pergunta obrigatória no comentário final:** por que foi necessário usar índices neste exercício?

---

## Exercício 10 — Boletim: média de cada estudante

**Objetivo:** representar boletim com matriz de notas.

Crie um programa chamado `ex10_boletim_medias.py` com os dados:

```python
nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]
```

O programa deve calcular e exibir a média de cada estudante.

**Saída esperada aproximada:**

```text
Ana - Média: 8.17
Bruno - Média: 5.50
Carla - Média: 9.17
Diego - Média: 6.50
```

**Desafio extra:** formate todas as médias com duas casas decimais.

---

## Exercício 11 — Boletim: média e situação

**Objetivo:** aplicar decisão condicional a partir da média.

Amplie o exercício 10 para exibir a situação de cada estudante:

- média maior ou igual a `7.0`: `Aprovado`;
- média menor que `7.0`: `Recuperação`.

**Saída esperada aproximada:**

```text
Ana - Média: 8.17 - Aprovado
Bruno - Média: 5.50 - Recuperação
Carla - Média: 9.17 - Aprovado
Diego - Média: 6.50 - Recuperação
```

**Desafio extra:** adicione a situação `Reprovado` para média menor que `5.0`.

---

## Exercício 12 — Boletim: maior média da turma

**Objetivo:** identificar o estudante com melhor desempenho médio.

Usando os dados do boletim, crie um programa que:

1. Calcule a média de cada estudante.
2. Identifique a maior média.
3. Exiba o nome do estudante com maior média.

**Saída esperada:**

```text
Maior média: Carla - 9.17
```

**Desafio extra:** identifique também a menor média da turma.

---

## Exercício 13 — Média por avaliação

**Objetivo:** percorrer a matriz por coluna.

Usando a matriz de notas, calcule a média da turma em cada avaliação.

**Saída esperada aproximada:**

```text
Avaliação 0 - Média: 7.13
Avaliação 1 - Média: 7.25
Avaliação 2 - Média: 7.63
```

**Pergunta obrigatória no comentário final:** por que neste exercício o laço externo pode percorrer as colunas?

---

## Exercício 14 — Grade de assentos: contagem de estados

**Objetivo:** representar uma grade simples com estados textuais.

Considere a matriz:

```python
sala = [
    ["L", "O", "L"],
    ["O", "O", "L"],
    ["L", "L", "O"]
]
```

Em que:

- `"L"` representa assento livre;
- `"O"` representa assento ocupado.

Crie um programa que conte e exiba:

1. Quantos assentos estão livres.
2. Quantos assentos estão ocupados.

**Desafio extra:** exiba o percentual de ocupação da sala.

---

## Exercício 15 — Grade de assentos: reserva de posição

**Objetivo:** alterar uma célula da matriz com base em uma regra.

Usando a matriz `sala`, crie um programa que:

1. Peça ao usuário a linha desejada.
2. Peça ao usuário a coluna desejada.
3. Verifique se a posição está dentro dos limites da matriz.
4. Se o assento estiver livre (`"L"`), altere para ocupado (`"O"`) e exiba `Reserva realizada`.
5. Se o assento estiver ocupado, exiba `Assento indisponível`.
6. Exiba a matriz atualizada ao final.

**Exemplo de interação:**

```text
Digite a linha: 2
Digite a coluna: 1
Reserva realizada.
```

**Desafio extra:** permita que o usuário faça reservas repetidas até digitar `-1` para sair.

---

## Exercício 16 — Controle de presença em matriz

**Objetivo:** usar matriz para representar presença e falta.

Crie um programa com a matriz:

```python
presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]
```

O programa deve:

1. Contar o total de presenças.
2. Contar o total de faltas.
3. Exibir o resultado geral.

**Desafio extra:** calcule o percentual geral de presença.

---

## Exercício 17 — Faltas por estudante

**Objetivo:** calcular totais por linha.

Usando a matriz de presença do exercício 16, crie um programa que exiba quantas faltas cada estudante teve.

**Saída esperada aproximada:**

```text
Estudante 0 - Faltas: 1
Estudante 1 - Faltas: 2
Estudante 2 - Faltas: 1
Estudante 3 - Faltas: 2
```

**Desafio extra:** exiba também a situação `Frequência adequada` ou `Atenção à frequência`.

---

## Exercício 18 — Aula com mais faltas

**Objetivo:** calcular totais por coluna.

Usando a matriz de presença, descubra qual aula teve mais faltas.

O programa deve exibir:

```text
Aula com mais faltas: X
Quantidade de faltas: Y
```

**Dica:** neste exercício, cada coluna representa uma aula.

---

## Exercício 19 — Tabuleiro de jogo da velha

**Objetivo:** representar e exibir uma grade 3x3.

Crie uma matriz:

```python
tabuleiro = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]
```

Escreva um programa que exiba o tabuleiro no formato:

```text
X | O |  
---------
  | X | O
---------
O |   | X
```

**Desafio extra:** crie uma função chamada `exibir_tabuleiro(tabuleiro)`.

---

## Exercício 20 — Jogada simples no jogo da velha

**Objetivo:** validar e alterar uma posição da matriz.

Usando o tabuleiro do exercício 19, crie um programa que:

1. Peça linha e coluna da jogada.
2. Peça o símbolo (`X` ou `O`).
3. Verifique se a posição está vazia.
4. Se estiver vazia, realize a jogada.
5. Se estiver ocupada, exiba `Jogada inválida`.
6. Exiba o tabuleiro atualizado.

**Desafio extra:** impeça símbolos diferentes de `X` e `O`.

---

## Exercício 21 — Depuração: índice fora dos limites

**Objetivo:** identificar e corrigir erro de acesso.

Analise o código:

```python
dados = [
    [1, 2],
    [3, 4]
]

print(dados[2][0])
```

No arquivo `ex21_debug_indice.py`, responda em comentários:

1. Qual erro ocorre?
2. Por que o erro ocorre?
3. Quais são os índices válidos de linha?
4. Corrija o código para exibir o valor `3`.

---

## Exercício 22 — Depuração: matriz irregular

**Objetivo:** percorrer matriz com linhas de tamanhos diferentes.

Analise:

```python
dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

for i in range(len(dados)):
    for j in range(3):
        print(dados[i][j])
```

Crie uma versão corrigida que percorra todas as linhas com segurança, usando o tamanho real de cada linha.

**Pergunta obrigatória no comentário final:** por que `range(3)` não é seguro nesse caso?

---

## Exercício 23 — Depuração: inicialização incorreta

**Objetivo:** compreender referência compartilhada em listas internas.

Execute o código:

```python
matriz = [[0] * 3] * 3
matriz[0][0] = 1
print(matriz)
```

Depois:

1. Observe o resultado.
2. Explique em comentário o que aconteceu.
3. Crie a mesma matriz usando compreensão de listas:

```python
matriz = [[0 for coluna in range(3)] for linha in range(3)]
```

4. Altere `matriz[0][0]` novamente e verifique se apenas uma célula foi alterada.

---

## Exercício 24 — Mini-projeto: sistema simples de boletim

**Objetivo:** integrar criação, percurso, média, decisão e relatório.

Crie um programa completo que:

1. Armazene nomes de 5 estudantes.
2. Armazene 4 notas para cada estudante usando matriz.
3. Calcule a média de cada estudante.
4. Classifique cada estudante conforme as regras:
   - média maior ou igual a `7.0`: `Aprovado`;
   - média maior ou igual a `5.0` e menor que `7.0`: `Recuperação`;
   - média menor que `5.0`: `Reprovado`.
5. Exiba um relatório final com nome, média e situação.
6. Exiba a maior média da turma.
7. Exiba a menor média da turma.

**Entrega:** arquivo `ex24_miniprojeto_boletim.py`.

---

## Exercício 25 — Mini-projeto: mapa de ocupação de laboratório

**Objetivo:** aplicar matriz em uma pequena simulação.

Crie um programa para representar um laboratório com 4 fileiras e 5 computadores por fileira.

Use:

- `"L"` para livre;
- `"O"` para ocupado;
- `"M"` para manutenção.

O programa deve:

1. Exibir o mapa completo do laboratório.
2. Contar computadores livres, ocupados e em manutenção.
3. Permitir ocupar uma posição livre informada pelo usuário.
4. Impedir ocupar uma posição em manutenção.
5. Informar se a posição digitada está fora dos limites.
6. Exibir o mapa atualizado.

**Entrega:** arquivo `ex25_miniprojeto_laboratorio.py`.

---

## 4. Critérios de avaliação sugeridos

| Critério | Descrição | Pontuação sugerida |
|---|---|---:|
| Criação correta de matrizes | Usa listas de listas de forma coerente | 2,0 |
| Acesso por índices | Usa `matriz[linha][coluna]` corretamente | 2,0 |
| Laços aninhados | Percorre linhas e colunas sem erros | 2,0 |
| Resolução dos problemas | Calcula médias, contagens, buscas e atualizações | 2,0 |
| Clareza do código | Usa bons nomes, comentários úteis e organização | 1,0 |
| Depuração | Identifica e corrige erros de índice, irregularidade e inicialização | 1,0 |

---

## 5. Entrega final sugerida

Ao final do laboratório, entregue:

1. Os arquivos `.py` dos exercícios resolvidos.
2. Um arquivo `README_respostas.md` com breve explicação dos exercícios mais difíceis.
3. Um comentário final respondendo:
   - O que cada linha representa nos principais exercícios?
   - O que cada coluna representa?
   - Em qual exercício o uso de matriz foi mais útil?

---

## 6. Observação final

Antes de programar qualquer solução com matriz, faça três perguntas:

1. O problema tem linhas e colunas de forma natural?
2. A posição do dado importa?
3. Vou precisar percorrer, alterar, buscar ou calcular valores por linha ou coluna?

Se a resposta for sim, uma lista bidimensional provavelmente é uma boa escolha.
