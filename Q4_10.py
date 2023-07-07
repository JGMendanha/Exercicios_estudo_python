class Carro:
    def __init__(self, consumo:int, qnt_tank:float):
        self.consumo = consumo
        self.qnt_tank = qnt_tank
    
    def andar(self, dist):
        c =  dist / self.consumo
        self.qnt_tank -= c
    
    def abastecer(self,qtde):
        self.qnt_tank += qtde

c1 = Carro(10, 23)

c1.andar(57)
c1.abastecer(5.6)

print("Quantidade de gasolina restante no tanque do carro =", c1.qnt_tank)
