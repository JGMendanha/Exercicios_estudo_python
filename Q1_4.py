s = float(input("Digite quanto ganha por hora trabalhada "))
t = int(input("Digite o numero de horas trabalhadas no mes "))

sb = s * t
qi = sb * 0.10
qs = sb * 0.02
ir = sb * 0.15
sl = sb - qi - qs - ir

print(f"Salario bruto = {sb}\nQuantia paga ao INSS = {qi}\nQuantia paga ao sindicato = {qs}\nSalario liquida = {sl}")