import os

def extract_place(nome_arquivo):
    primeira_parte = nome_arquivo.find("_")
    parcial = nome_arquivo[primeira_parte+1:]
    segunda_parte = parcial.find("_")
    definitivo = parcial[:segunda_parte]
    print(definitivo)

extract_place("2016-11-04_Berlin_09/42/22.jpg")    

# os.chdir("Photos")
# originals = os.listdir()

# print(originals)