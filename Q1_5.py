from math import ceil
a = float(input("Digite a area quadrada a ser pintada "))
l = a / 3 
lt = l / 18
lti =  ceil(lt) 
p = lti * 80 
print(f"Quantidade de latas = {lti}\nPreço = {p}")