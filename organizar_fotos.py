import os

# A função a seguir extrai uma palavra-chave do nome do arquivo; neste exercício,
# as palavras-chaves estão entre subtraços.
def extrair_palavra(nome_arquivo):
    return nome_arquivo.split("_")[1]

# A função a seguir cria um diretório de acordo com a palavra-chave extraída do
# nome do arquivo e anexada à lista "lugares".
def criar_diretorio(lugares):
    for lugar in lugares:
        os.mkdir(lugar)

#Esta função extrai a palavra-chave, cria o diretório de acordo com ela e move os
#arquivos para as pastas correspondentes.
def organizar_fotos(diretorio):    
    os.chdir(diretorio)
    originais = os.listdir()
    lugares = []
    for arquivos in originais:
        palavra_chave = extrair_palavra(arquivos)
        if palavra_chave not in lugares:
            lugares.append(palavra_chave)
    criar_diretorio(lugares)
    for arquivos in originais:
        lugar = extrair_palavra(arquivos)
        os.rename(arquivos, 
                 os.path.join(lugar, arquivos))

if __name__ == "__main__":
    organizar_fotos("Photos")