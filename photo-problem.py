import os

os.chdir("Photos")
originais = os.listdir()

# A função a seguir extrai uma palavra-chave do nome do arquivo; neste exercício,
# as palavras-chaves estão entre subtraços.
def extract_place(nome_arquivo):
    return nome_arquivo.split("_")[1]
    
extract_place("2016-11-04_Berlin_09/42/22.jpg")    