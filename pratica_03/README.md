### Lista Pratica de Laboratorio 03: Funcoes, Modularizacao, Depuracao e Testes

Esta lista foi elaborada com base nos conteudos do **Capitulo 7 - Funcoes, Modularizacao e Depuracao no Desenvolvimento Estruturado**, contemplando **definicao de funcao**, **parametros e argumentos**, **return**, **escopo basico**, **boas praticas de decomposicao**, **tipos de erro**, **estrategias de depuracao**, **teste de mesa** e **casos de teste simples**.

---

#### Instrucoes gerais

- Crie **um arquivo `.py` para cada exercicio** (`ex01.py`, `ex02.py`, ...).
- Antes de chamar o professor, **teste sua solucao** com pelo menos **2 entradas diferentes**.
- Sempre que o exercicio pedir funcao, **evite colocar toda a logica no programa principal**.
- Quando houver erro, tente identificar se e:
  - **erro sintatico**;
  - **erro de execucao**;
  - **erro logico**.
- Ao final, envie os arquivos seguindo o fluxo de repositorio combinado em aula.

---

## Exercicios praticos

#### 1) Saudacao modular
Crie uma funcao chamada `saudacao(nome)` que receba o nome de uma pessoa e **retorne** uma mensagem de boas-vindas.

**Requisitos:**
- a funcao deve usar `return`;
- o programa principal deve chamar a funcao pelo menos **3 vezes** com nomes diferentes.

**Exemplo esperado:**
```python
print(saudacao("Ana"))
# Bem-vindo(a), Ana!
```

---

#### 2) Soma com parametros
Crie uma funcao chamada `somar(a, b)` que receba dois numeros e retorne a soma.

**Requisitos:**
- testar com numeros inteiros;
- testar com um caso usando zero;
- testar com um caso usando numero negativo.

**Objetivo:** praticar parametros, argumentos e retorno.

---

#### 3) Media de aluno
Crie uma funcao `calcular_media(n1, n2)` que receba duas notas e retorne a media aritmetica.

**Depois:**
- peca ao usuario duas notas;
- chame a funcao;
- exiba a media retornada.

**Desafio extra:** formatar a media com uma casa decimal.

---

#### 4) Situacao do aluno
Crie uma funcao `verificar_situacao(media)` que:
- retorne `"Aprovado"` se `media >= 7`;
- retorne `"Reprovado"` caso contrario.

Depois, integre essa funcao com a funcao do exercicio anterior.

**Objetivo:** dividir calculo e decisao em partes diferentes.

---

#### 5) Boletim simples com modularizacao
Crie um programa para um boletim simples, obrigatoriamente dividido em funcoes.

**O programa deve ter, no minimo, estas funcoes:**
- `ler_notas()`
- `calcular_media(n1, n2)`
- `verificar_situacao(media)`
- `exibir_resultado(nome, media, situacao)`

**Objetivo:** praticar decomposicao do problema em partes menores e reutilizaveis.

---

#### 6) Escopo basico na pratica
Analise o codigo abaixo:

```python
x = 10

def teste():
    y = 5
    return x + y

print(teste())
```

**Faca o seguinte:**
1. Identifique qual variavel e **global**.
2. Identifique qual variavel e **local**.
3. Explique o que acontece se tentarmos usar `y` fora da funcao.
4. Crie um exemplo parecido feito por voce.

**Objetivo:** compreender escopo local e global.

---

#### 7) Refatorando codigo monolitico
Transforme o codigo abaixo em uma solucao modular:

```python
n1 = 8
n2 = 6
media = (n1 + n2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

**Requisitos:**
- criar pelo menos **2 funcoes**;
- uma funcao deve calcular a media;
- outra funcao deve verificar a situacao.

**Objetivo:** perceber a diferenca entre codigo monolitico e codigo modular.

---

#### 8) Depuracao de erro sintatico
O codigo abaixo contem erro:

```python
def saudacao(nome)
    print("Ola,", nome)
```

**Sua tarefa:**
- corrigir o codigo;
- dizer qual era o erro;
- explicar por que o programa nao executava.

**Objetivo:** praticar leitura e correcao de erro sintatico.

---

#### 9) Depuracao de erro de execucao
Analise o codigo:

```python
def dividir(a, b):
    return a / b

print(dividir(10, 0))
```

**Faca o seguinte:**
1. Explique que erro acontece.
2. Diga por que ele ocorre.
3. Reescreva o programa para evitar esse problema.

**Desafio extra:** mostrar uma mensagem amigavel quando `b == 0`.

---

#### 10) Teste de mesa + caso de teste
Considere o codigo abaixo:

```python
def calcular_total(preco, quantidade):
    subtotal = preco * quantidade
    desconto = subtotal * 0.1
    total = subtotal - desconto
    return total
```

**Parte A - Teste de mesa**
Monte uma tabela com os valores de:
- `preco`
- `quantidade`
- `subtotal`
- `desconto`
- `total`

Use a chamada:
```python
calcular_total(50, 2)
```

**Parte B - Casos de teste**
Crie pelo menos:
- 2 casos normais;
- 1 caso limitrofe;
- 1 caso extremo.

**Objetivo:** praticar validacao de funcoes por analise e teste.

---

## Desafio final opcional

Se terminar antes, crie um programa completo de cadastro de aluno que:
- leia o nome do aluno;
- leia duas notas;
- calcule a media usando funcao;
- determine a situacao usando funcao;
- exiba um pequeno relatorio final.

**Requisito:** usar pelo menos **4 funcoes**.

---

## Checklist antes de entregar

Verifique se voce:
- criou funcoes com nomes claros;
- usou `return` quando necessario;
- separou calculo e exibicao;
- testou com mais de uma entrada;
- corrigiu possiveis erros com atencao as mensagens do interpretador.

---

## Dica do professor

Ao resolver cada exercicio, pense sempre em 3 perguntas:

1. **O que entra na funcao?**
2. **O que a funcao faz?**
3. **O que ela devolve?**

Se essas tres respostas estiverem claras, sua solucao tende a ficar mais organizada, mais facil de testar e mais facil de corrigir.

---
