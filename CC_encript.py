import time

alfa_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç"]
LINE_LENGTH = 94

def encripta_frase(frase, alfa_array, int_saltos):
    frase_encriptada = ""
    for caractere in frase:
        if caractere.isalpha():
            if caractere in alfa_array:
                index = alfa_array.index(caractere)
                novo_index = (index + int_saltos) - len(alfa_array)
                frase_encriptada += alfa_array[novo_index]
            else:
                frase_encriptada += caractere
        else:
            frase_encriptada += caractere
    return frase_encriptada

def obter_input_inteiro(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("ATENÇÃO! Digite apenas valores inteiros...")

while True:
    print(LINE_LENGTH * "=")
    print("Entre com a palavra a ser tratada pela cifra de César, e em seguida a quantidade de saltos.")
    txt_frase = input().strip()
    int_saltos = obter_input_inteiro("Digite o número de saltos: ")

    print("Iniciando algoritmo de criptografia...")
    time.sleep(0.8)
    frase_encriptada = encripta_frase(txt_frase, alfa_array, int_saltos)

    print(f"\nCífra de César: {frase_encriptada}")
    print(LINE_LENGTH * "=")
    escolha = input("Deseja encriptar outra frase? S/N...").strip().upper()

    if escolha == "N":
        print("Encerrado...")
        break


 