import os

# A função a seguir extrai uma palavra-chave do nome do arquivo; neste exercício,
# as palavras-chaves estão entre subtraços.
def extract_place(nome_arquivo):
    return nome_arquivo.split("_")[1]

os.chdir("Photos")
originais = os.listdir()

lugares = []

for arquivos in originais:
    palavra_chave = extract_place(arquivos)
    lugares.append(palavra_chave)

print(lugares)    