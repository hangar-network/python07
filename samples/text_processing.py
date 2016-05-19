import os


data_folder = "raw_data"
results_folder = "structured_data"
# lista com todas as marcações que desejamos ignorar
marks = [",", ";", ".", "!", "?", "\"", "\'", "%", "[", "]", "(", ")" ]
# A contrabarra é utilizada para sinalizar que a aspas utilizada faz parte da string
# e não está tentando fechá-la. Chamamos isso de "fazer escape do caractere".

def tokenize(filename, outputname = None):
    """ This function converts a raw text input into a file where each line
        contains a single word and no word is duplicated
    """

    # Ao final, esta lista vai conter todas as palavras separadas
    tokens = []
    inputfilename = filename
    # Se o arquivo não for encontrado no caminho passado, tentamos encontrá-lo
    # no diretorio padrão de dados (que definimos acima)
    if not os.path.exists(filename):
        inputfilename = os.path.join(data_folder, os.path.basename(filename))

    # abre o arquivo para leitura
    with open(inputfilename, 'r') as text_file:
        # a variável text_file existe apenas dentro deste bloco; ela é o nosso
        # ponto de acesso para qualquer operação no arquivo
        textline = text_file.readline()
        # textline contem uma string com o conteúdo de uma linha do arquivo
        while(textline != ""): #vamos ler o arquivo até o final, linha por linha
            # quebramos a string em várias strings e colocamos cada pedacinho em
            # uma lista; a quebra ocorre onde há espaços em branco " ".
            words = textline.split()
            # cada elemento em words contém uma palavra mais, possivelmente, algum
            # dos símbolos que demarcamos na lista "marks"; vamos formar uma nova
            # removendo estes símbolos de cada elemento de words.
            symbols_to_remove = "".join(marks)
            cleaned_words = [w.strip(symbols_to_remove) for w in words]
            # estende a lista tokens com os elementos da lista cleaned_words
            tokens.extend(cleaned_words)
            #lê a próxima linha do arquivo
            textline = text_file.readline()

    # remove todas as palavras que tem 3 ou menos letras
    # (tipicamente, mas nem sempre, removeremos artigos, preposições, conjunções etc)
    tokens = [t for t in tokens if len(t) > 3]
    # repare que a remoção se deu, na verdade, pela criação de uma nova lista e
    # a atribuição dessa nova lista à variável tokens (a lista antiga é perdida)

    # remove palavras duplicadas
    tokens = list(set(tokens)) # explicarei em sala de aula

    # Se nenhum nome foi dado ao arquivo de saída, criamos um nome baseado no
    # arquivo de entrada e salvamos no diretorio de resultados (definido acima)
    if outputname is None:
        outputname = os.path.join(results_folder ,"tokens_" + os.path.basename(filename))

    with open(outputname, "w") as token_file:
        for t in tokens:
            # concatena uma quebra de linha ao final de cada palavra
            token_file.write(t + "\n")
    print("Sucesso! Verifique o resultado em '{}' no diretório '{}'".format(
            os.path.basename(outputname), results_folder))


# chama a função e roda o código
tokenize(input("Digite o nome do arquivo a ser processado: "))
