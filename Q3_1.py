while(True):
    nome = str(input("Digite seu nome "))
    idade = int(input("Digie sua idade "))
    salario = float(input("Digite seu salario "))
    sexo = str(input("Digite seu sexo (M ou F) "))
    e_civil = str(input("Digite seu estado civil (S, C, V, D) "))
    if len(nome) >= 3 and idade >= 0 and idade <= 150 and salario > 0 and (sexo == "F" or sexo == "M") and (e_civil == "S" or e_civil == "C" or e_civil == "V" or e_civil == "D"): 
        print("Tudo certo com as informações ")
        break 
    else:
        print("Digite informações validas")