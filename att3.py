notas_do_aluno = []
while True:
    valor = input("Digite uma nota (0 a 10) ou 'fim' para encerrar: ")
    if valor.lower() == "fim":
        break
    nota = float(valor.replace(',','.'))
    if 0 <= nota <= 10:
        notas_do_aluno.append(nota)
    else:
        print("digite entre 0 e 10")

if len(notas_do_aluno) > 0:
    media = sum(notas_do_aluno) / len(notas_do_aluno)
    print(f"Média do aluno: {media:.2f}")
    if media >= 7:
        print("Aluno APROVADO")
    else:
        print("Aluno REPROVADO")
else:
    print("informe uma nota.")