def ocorre(s, c):
    o = 0
    for i in range(len(s)):
        if c == s[i]:
            o += 1
    return o

s = str(input("Digite a string "))
c = str(input("Digite a letra que quer saber a ocorrencia "))
print(f"Ocorrencia da letra {c} na string = {ocorre(s,c)}")