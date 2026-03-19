def contadorVogais():
    palavra = str(input("Digite uma palavra: "))

    vogais = ["a", "e", "i", "o", "u"]
    
    contador = 0
    
    for letra in palavra:
        for vogal in vogais:
            if(letra == vogal):
                contador += 1
                
                print(f"A Palavra: ", palavra, "Tem ", contador, "vogais")

    