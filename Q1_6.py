mb = float(input("Digite o tamanho do arquivo em MB "))
mbps = int(input("Digite a velocidade da internet em MBPS "))
mbpm = mbps * 60
t = mb / mbpm
print(f"O tempo necessario para baixar o arquivo em minutos e de = {t}")