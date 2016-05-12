# Botafogo Espaço de Estudos

## Curso de Python

### Objetivo prático do curso básico

Neste curso, iremos praticar vários recursos básicos da linguagem desenvolvendo um **Jogo da Forca**.

**Por que Jogo da Forca?**

Com o Jogo da Forca, iremos praticar:
1. Estruturas condicionais
2. Estruturas de repetição
3. Manipulação de listas e strings
4. Leitura e escrita de arquivos
5. Importação de módulos
6. Geração de resultados aleatórios

Além, disso, lidar com a concepção e construção de soluções para um problema bem conhecido — e que ainda assim tem várias alternativas — do início ao fim, é uma excelente maneira de adquirir auto-confiança para prosseguir na solução de problemas desconhecidos.

Para estimular o seu raciocínio na concepção de problemas de software, a descrição do projeto será feita completamente em prosa. Isso deixará, intencionalmente, muitos pontos ambíguos. *Computadores são máquinas determinísticas e não lidam com ambiguidades*. Converter o pedido de um cliente em uma estrutura livre de ambiguidades e passível de implementação é uma das partes cruciais de um engenheiro de software (e onde muitos projetos pecam, gerando stress e desperdício de recursos). Portanto, praticaremos isso desde já :)

*Se você tiver dificuldade, por conta da inexperiência, é normal. Deixarei uma versão "passo-a-passo" neste diretório, você pode consultá-la quando cansar.*

**Incrementaremos o jogo por etapas para contemplar cada vez mais recursos da linguagem e adequá-lo a práticas profissionais de desenvolvimento de software.**

####Etapa 1: Jogo da forca básico para 2 jogadores

Nesta primeira etapa, o jogo funcionará de maneira muito similar ao que fazemos com papel e caneta: um jogador (desafiante) pensa em uma palavra e o outro jogador (desafiado), conhecendo o tamanho da palavra, tenta advinhar quais letras estão presentes. Se o desafiado fizer um palpite correto, a letra é preenchida no(s) espaço(s) correspondente(s). Se o palpite estiver errado, o desafiado "perde uma vida". O jogo acaba quando o desafiado não tem mais vidas a perder ou quando ele advinha a palavra correta.

####Etapa 2: Jogo da Forca para 1 jogador

Nesta segunda etapa, será possível escolher entre jogar com 2 jogadores ou com apenas 1. No modo "1 jogador", o computador deve escolher a palavra a ser advinhada pelo jogador.

####Etapa 3: Modos de dificuldade

Nesta terceira etapa, o modo "1 jogador" deve permitir a escolha de 3 níveis de dificuldade diferentes.

####Etapa 4: Pontuação

Nesta quarta etapa, adicionaremos uma medida de pontuação e um ranking *persistente* para o jogo. Ao encerrar cada partida,você deve exibir um ranking com as N maiores pontuações já registradas (o valor de N fica a seu critério).
