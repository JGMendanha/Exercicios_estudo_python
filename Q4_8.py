def calc_mdc(a, b):
    if a >= b:
        me = b
    else:
        me = a
    for i in range(me):
        if a % (i + 1) == 0 and b % (i + 1) == 0:
            mdc = i + 1

    return mdc

a = int(input("Digite o primeiro número "))
b = int(input("Digite o segundo número "))
print(f"MDC dos dois numeros = {calc_mdc(a, b)}")
