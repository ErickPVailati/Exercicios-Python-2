numeros_pares = []


for numeros in range(1, 7):
        num = int(input(f"Digite {numeros} - Digite o {numeros}º número: "))
        if num % 2 == 0:
            numeros_pares.append(num)

print("\nOs números pares digitados foram:", numeros_pares)
