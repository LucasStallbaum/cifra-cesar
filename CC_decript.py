import json
import time

file_json = "palavras-latinas.json"
LINE_LENGTH = 94

# Carregar o arquivo JSON
with open(file_json, 'r', encoding='utf-8') as file:
    dados = json.load(file)

alfa_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç"]

def decripta_frase(texto, alfa_array, deslocamento):
    frase_decriptada = ""
    for caractere in texto:
        if caractere in alfa_array:
            index = alfa_array.index(caractere)
            novo_index = (index - deslocamento) % len(alfa_array)
            novo_caractere = alfa_array[novo_index]
            frase_decriptada += novo_caractere
        else:
            frase_decriptada += caractere  # mantem caracteres inalterados
    return frase_decriptada

while True:
    print(LINE_LENGTH * "=")
    print("Digite a frase encriptada pela cifra de César.")
    texto_encriptado = input().strip().lower()
    texto_final = ""
    
    # tenta diferentes deslocamentos
    encontrou_palavra = False
    for deslocamento in range(1, len(alfa_array)):  
        texto_decriptado = decripta_frase(texto_encriptado, alfa_array, deslocamento)
        
        # Criar uma lista de palavras com a frase decriptada, para consultar no dic separadamente
        texto_repartido = []
        for palavra in texto_decriptado.split():
            palavra_separada = "'" + palavra + "'"
            texto_repartido.append(palavra_separada)

        # Verificar cada palavra isolada no dicionario, caso ache, agrupa na vvariavel final
        for palavra_isolada in texto_repartido: 
            # remove as aspas simples para a verificar no dic
            palavra_sem_aspas = palavra_isolada.strip("'")
            if palavra_sem_aspas in dados:
                texto_final += palavra_sem_aspas + " "
        
        if texto_final != "":
            time.sleep(0.8)
            print(f"\nNúmero de Saltos usados {deslocamento}: texto decriptado: {texto_final}")
            encontrou_palavra = True
            break

    if not encontrou_palavra:
        print("Nenhuma correspondência encontrada para a frase fornecida com os deslocamentos testados.")
    
    print(LINE_LENGTH * "=")
    escolha = input("Deseja decriptar outra cifra? S/N...").strip().upper()

    if escolha == "N":
        print("Encerrado...")
        break
