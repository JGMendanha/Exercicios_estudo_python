p = float(input("Digite seu peso "))
a = float(input("Digite sua altura em metros "))
imc = p / (a ** 2)
if imc < 18.5:
    print("Abaixo do peso")
elif imc > 25: 
    print("Sobrepeso")
elif imc > 18.5 and imc < 25:
    print("Peso normal")