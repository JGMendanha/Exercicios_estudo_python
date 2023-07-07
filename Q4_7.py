def vogais(s):
    v = 0 
    for i in range(len(s)):
        if s[i] == "a" or s[i] == "A":
            v += 1
        elif s[i] == "e" or s[i] == "E":
            v += 1
        elif s[i] == "i" or s[i] == "I":
            v += 1
        elif s[i] == "o" or s[i] == "O":
            v += 1
        elif s[i] == "u" or s[i] == "U":
            v += 1
    return v

v = vogais("Alemanha")
print(f"Numero de vogais na string = {v}")
        