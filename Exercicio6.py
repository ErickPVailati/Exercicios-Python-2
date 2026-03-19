nomes: list[str] = []
for i in range(3):
    nome = str(input(f" Digite o {i+1}º nome: "))
    nomes.append(nome)

nomes.sort()
print("\nOs nomes digitados foram:", nomes )
