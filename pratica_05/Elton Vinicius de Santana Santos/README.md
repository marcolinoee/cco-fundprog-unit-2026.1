# README_respostas

## Exercício 13 - Média por avaliação

Esse exercício foi mais difícil porque foi necessário percorrer a matriz por colunas. Cada coluna representava uma avaliação e cada linha representava um estudante. Foi preciso somar os valores de uma mesma coluna para calcular a média da turma em cada prova.

## Exercício 18 - Aula com mais faltas

Nesse exercício também foi necessário percorrer as colunas da matriz. Cada coluna representava uma aula. O objetivo era descobrir qual aula possuía a maior quantidade de faltas.

## Exercício 23 - Inicialização incorreta

O código usando `[[0] * 3] * 3` cria linhas compartilhando a mesma referência na memória. Por isso, ao alterar uma célula, várias linhas eram modificadas ao mesmo tempo. A solução foi utilizar compreensão de listas para criar linhas independentes.

## Exercício 24 - Sistema de boletim

Esse exercício integrou vários conceitos estudados anteriormente: matrizes, laços de repetição, cálculo de médias e estruturas condicionais. Foi necessário calcular a média de cada estudante e determinar sua situação final.

## Exercício 25 - Mapa de ocupação do laboratório

Esse exercício simulou um cenário real utilizando matrizes. Foi necessário contar estados diferentes, validar posições informadas pelo usuário e atualizar a matriz de acordo com as regras do sistema.
