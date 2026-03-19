notas = []

for i in range(4):
        nota = float(input(f"Nota {i} - Digite a {i}º nota: "))
        notas.append(nota)
        
media = sum(notas)/len(notas)

print("\nA média das notas eh: ", {media})
