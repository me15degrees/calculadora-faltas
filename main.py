aulas = int(input("Digite a quantidade de horas da carga horária: "))
max_faltas = (aulas * 25) // 100
faltas = int(input("Digite quantas aulas você faltou: "))
_faltas = (faltas * 100) // aulas

if faltas > max_faltas:
    print(f"Você já extrapolou. O número máximo de faltas é {max_faltas} e você teve {faltas} faltas. \nIsso corresponde a {_faltas}%")
elif faltas == max_faltas: 
    print("Não falte mais nenhum dia!")
else:
    faltas_restantes = max_faltas - faltas
    print(f"Você está dentro do limite. Você pode faltar mais {faltas_restantes} aulas para atingir o limite máximo de faltas, que é {max_faltas}.")
