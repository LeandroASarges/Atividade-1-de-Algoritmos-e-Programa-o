controle_notas = []

for i in range(6):
    while True:
        nota = float(input(f"Digite a nota do {i + 1}º aluno (0 a 10): "))

        if 0.0 <= nota <= 10.0:
            controle_notas.append(nota)
            break
        else:
            print("Nota inválida! Digite outra nota (0 a 10): ")

media = sum(controle_notas) / len(controle_notas)
maior_nota = max(controle_notas)
menor_nota = min(controle_notas)

acima_media = 0
for nota in controle_notas:
    if nota >= 7:
        acima_media += 1

abaixo_media = 0
for nota in controle_notas:
    if nota < 7:
        abaixo_media += 1

print("\n---------------- Notas ----------------")
print(f"Média dos alunos antes da recuperação: {media:.2f}")
print("Notas dos alunos antes da recuperação:", controle_notas)
print(f"Maior nota: {maior_nota:.2f}")
print(f"Menor nota: {menor_nota:.2f}")
print("Alunos acima ou igual a média:", acima_media)
print("Alunos abaixo da média:", abaixo_media)


for i in range(len(controle_notas)):
    if controle_notas[i] < media:
        print(f"\nO {i + 1}º aluno ficou abaixo da média (Nota atual: {controle_notas[i]}).")

        while True:
            nota_recuperacao = float(input(f"Digite a nota de recuperação do {i + 1}º aluno: "))
            if 0.0 <= nota_recuperacao <= 10.0:
                break
            else:
                print("Nota inválida! Digite outra nota (0 a 10): ")

        if nota_recuperacao > controle_notas[i]:
            controle_notas[i] = nota_recuperacao
            print("Nota atualizada com sucesso!")
        else:
            print("Nota de recuperação menor ou igual à original. Mantendo nota antiga.")

print("\n--- Resultado Final ---")
print("Notas após a recuperação:", controle_notas)