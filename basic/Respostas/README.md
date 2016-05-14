# Botafogo Espaço de Estudos

## Curso de Python

### Jogo da Forca: passo-a-passo


####Etapa 1: Jogo da forca básico para 2 jogadores

Vamos começar pensando em como o jogo funciona e no que é necessário para jogá-lo.

Tipicamente, um jogador (desafiante) *pensa em uma palavra* e *apresenta* uma linha pontilhada (*um traço para cada letra* da palavra) ao segundo jogador (desafiado). Ex: palavra pensada: "tecnologia"

Exibe-se "_ _ _ _ _ _ _ _ _ _"

Em termos de programação, até o momento, vemos necessidade de:  

1. Solicitar uma palavra ao jogador
2. Determinar o tamanho da palavra
3. Exibir um traço para cada caractere da palavra

Após isso, o jogador desafiado *tenta advinhar alguma letra* que esteja na palavra. *Caso ele acerte*, essa letra é colocada *no lugar do traço* que corresponde à sua posição na palavra *(quantas vezes ela ocorrer)*. *Caso ele erre*, o desafiante desenha uma parte do boneco enforcado.

Aqui, vemos a necessidade de:

1. Solicitar uma letra ao jogador
2. Verificar **se** a palavra armazenada contém a letra escolhida.
3. Se contém, deve-se identificar todas as posições que correspondem a esta letra e substituir (redesenhar o pontilhado)
4. Se não contém, deve-se desenhar o boneco, o que corresponde a diminuir o número de tentativas do desafiado

Você pode testar se um elemento pertence a uma lista ou a uma string com a palavra **in**.

Vemos que há a necessidade de, no começo do jogo, definir-se quantas chances de errar o desafiado possui, pois a cada erro, devemos subtrair 1 deste total.

O fluxo do jogo é uma *sucessão (repetição)* dos eventos descritos na última parte, *encerrando-se quando o desafiado preenche todas as letras* da palavra *ou não possui mais nenhuma chance* para errar.

Para finalizar, precisamos deixar o jogo em loop (repetição dos passos). O número de passos que serão repetidos é indefinido a priori, pois cada partida pode ter um número maior ou menor de rodadas, portanto o **for** não é uma opção. Neste caso, o **while** é a escolha adequada para o loop e as condições para continuar são **as letras não foram todas preenchidas e o desafiado ainda possui ao menos uma chance**. Quando o jogo terminar, por qualquer que seja a razão, é conveniente exibir uma mensagem aos jogadores para marcar que acabou e quem ganhou.

1. Presisamos envolver os passos da etapa anterior em um laço **while**
2. **While** deve verificar o valor verdade da expressão **as letras não foram todas preenchidas *e* o desafiado ainda possui ao menos uma chance**
3. Ao sair do **while** deve-se verificar quem ganhou e exibir a mensagem adequada.

**Observações: 

* Strings são imutáveis. Uma forma de contornar este problema para fazer substituições é lidar com listas. Uma string pode ser convertida em uma lista da seguinte forma:

  ```python
  word = "tecnologia"
  word_list = list(word)
  ```
* Listas podem ser aglutinadas para formar strings. Elas são aglutinadas e concatenadas ao final de alguma string. Portanto, para converter a lista em uma string novamente, use:

  ```python
  word_list = ['t', 'e', 'c', 'n', 'o', 'l', 'o', 'g', 'i', 'a']
  word = "".join(word_list)
  # aglutina a lista e concatena no final da string vazia, formando a palavra desejada
  ```

####Etapa 2: Jogo da Forca para 1 jogador

Nesta etapa, as coisas ficam ainda mais interessantes, pois precisaremos bolar uma maneira de gerar palavras para o jogador. Para prosseguir, é necessário que você já tenha visto como importar módulos e — para ficar legal mesmo — como lidar com arquivos.

**Primeira tentativa**

Uma coisa que talvez venha na sua mente é a necessidade de gerar resultados aleatórios. Isto é correto, pois queremos que cada partida seja diferente da anterior. Talvez, num primeiro momento, você até pense em tentar criar as palavras por algum método aleatório (por exemplo, gerar cada letra aleatoriamente). 

Infelizmente, essa não é uma boa solução. Gerar letra por letra aleatoriamente não nos garante que teremos uma palavra (algo que esteja no dicionário da nossa língua) ao final do processo. Elaborar um procedimento para gerar palavras dicionarizadas aleatoriamente seria uma tarefa extremamente difícil!

**Segunda Tentativa**

Ok, não podemos gerar uma palavra aleatoriamente, o que faremos, então? Ao invés de gerar, podemos *escolher* uma palavra aleatoriamente. 

A ideia consiste em ter um conjunto de palavras previamente selecionadas armazenadas em algum lugar e, então, escolher uma delas aleatoriamente para jogar. Vamos começar bem simples.

Imagine que você cria em seu programa uma *lista* que contém várias palavras da língua portuguesa (ou outro idioma escolhido pro jogo): 

```python
  palavras_validas = ["estudar", "programação", "amizade", "matemática", "livro"]
```

Agora, podemos escolher aleatoriamente uma palavra da lista **palavras_validas** . Para isso, precisaremos importar o *módulo random*. Poderíamos gerar um índice (número) aleatório entre **0*** e **len(palavras_validas) - 1** e, então, acessar a palavra correspondente a esse índice. No entanto, Python nos permite fazer as coisas de uma forma mais direta:

```python
  import random
  palavras_validas = ["estudar", "programação", "amizade", "matemática", "livro"]
  palavra_selecionada = random.choice(palavras_validas)
```

O módulo *'random'* possui uma função chamada *'choice'*, que recebe uma lista de quaisquer elementos e retorna uma escolha aleatória de um elemento da lista. Armazenamos o resultado deste retorno na variável palavra_selecionada.

Pronto! Assim já temos uma maneira de jogar contra o computador. 

— "Ah, mas eu vou ter que escrever palavra por palavra em uma lista?!" 

Desgastante, né? Além de desgastante, é uma estrutura pouco flexível, difícil de expandir e não é uma boa prática de programação manter dados grandes direto no código. Vamos ver como solucionar esse problema.

**Base de dados de Palavras**

Nós iremos manter uma base de dados (não é um banco de dados) externa ao nosso código: *um arquivo de texto com palavras válidas*.

O ideal seríamos ter vários arquivos com todas as palavras dicionarizadas do idioma (separadas por vírgula, ou uma em cada linha etc). Como nós não temos isso disponível, vamos fazer algo menor, porém na mesma ideia! **Vamos pegar dados não estruturados e transformá-los em dados estruturados**.

**Coleta de dados**

Para simplificar, não vamos fazer o programa que captura os dados, apenas o que trata os dados. Desta forma, você deve, manualmente copiar e colar alguns textos da internet em um arquivo de texto. Sugiro pegar um artigo da [wikipedia](https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal) que não trate de um anglicismo.

Salve este arquivo com algum nome tipo: *"texto_comum.txt"*.

**Tratamento dos dados**

Selecionar uma palavra do texto que pegamos seria bem complicado, precisamos de um arquivo que seja mais fácil de lidar. O ideal seria um arquivo em que as palavras estivessem bem demarcadas, por exemplo, separadas por vírgulas, uma em cada linha etc. Além disso, temos que eliminar pontuação, artigos, conjunções etc... 

O tratamento completo do dado manualmente pode ser bastante extenso (por exemplo, você quer aceitar plural? Flexões de verbos? Flexões de gênero?) e seria assunto para um curso de *Processamento de Linguagem Natural* (NLP). Meu objetivo com este exercício é apenas que você **reflita sobre essas dificuldades de um programa real** e, principalmente, pratique técnicas básicas usando Python: abrir arquivo, processar uma string, escrever arquivo. 

Assim, nós vamos efetuar "apenas" as seguintes operações:

1. ler o texto completo
2. separar as palavras
3. remover as pontuações
4. remover palavras duplicadas
5. escrever uma palavra por linha

Talvez você se sinta apto a implementar uma ou todas as etapas acima. Dessa forma, deixarei o [código comentado neste link](https://github.com/espacodeestudosbotafogo/python07/blob/master/samples/text_processing.py), caso queira tentar e depois verificar.

####Etapa 3: Modos de dificuldade



####Etapa 4: Pontuação
