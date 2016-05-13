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
3. Exibir um traço para cada caractere na palavra.

Após isso, o jogador desafiado *tenta advinhar alguma letra* que esteja na palavra. *Caso ele acerte*, essa letra é colocada *no lugar do traço* que corresponde à sua posição na palavra *(quantas vezes ela ocorrer)*. *Caso ele erre*, o desafiante desenha uma parte do boneco enforcado.

Aqui, vemos a necessidade de:

1. Solicitar uma letra ao jogador
2. Verificar **se** a palavra armazenada contém a letra escolhida.
3. Se contém, deve-se identificar todas as posições que correspondem a esta letra e substituir
4. Se não contém, deve-se desenhar o boneco, o que corresponde a diminuir o número de tentativas do desafiado

Você pode testar se um elemento pertence a uma lista ou a uma string com a palavra **in**.

Vemos que há a necessidade de, no começo do jogo, definir-se quantas chances de errar o desafiado possui, pois a cada erro, devemos subtrair 1 deste total.

O fluxo do jogo é uma *sucessão (repetição)* dos eventos descritos na última parte, *encerrando-se quando o desafiado preenche todas as letras* da palavra *ou não possui mais nenhuma chance* para errar.

Para finalizar, precisamos deixar o jogo em loop (repetição dos passos). O número de passos que serão repetidos é indefinido a priori, pois cada partida pode ter um número maior ou menor de rodadas, portanto o **for** não é uma opção. Neste caso, o **while** é a escolha adequada para o loop e as condições para continuar são **as letras não foram todas preenchidas e o desafiado ainda possui ao menos uma chance**. Quando o jogo terminar, por qualquer que seja a razão, é conveniente exibir uma mensagem aos jogadores para marcar que acabou e quem ganhou.

1. Presisamos envolver os passos da etapa anterior em um laço **while**
2. **While** deve verificar o valor verdade da expressão **as letras não foram todas preenchidas *e* o desafiado ainda possui ao menos uma chance**
3. Ao sair do **while** deve-se verificar quem ganhou e exibir a mensagem adequada.


####Etapa 2: Jogo da Forca para 1 jogador



####Etapa 3: Modos de dificuldade



####Etapa 4: Pontuação
