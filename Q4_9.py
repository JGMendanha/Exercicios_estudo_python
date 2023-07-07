class Funcionario:
    def __init__(self, n:str, s:float):
        self.n = n
        self.s = s
    
f1 = Funcionario("Joao", 35000.50)
print("Nome:", f1.n, "\nSalario:", f1.s)
