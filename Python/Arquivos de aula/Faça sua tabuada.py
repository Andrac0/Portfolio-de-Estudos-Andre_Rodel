acertos = 0
erros = 0
n = int(input("Digite o número que deseja saber a tubuada: "))
for m in range (1,11):
    resultado = n * m
    resposta = int(input(f"Digite o valor de {n} * {m} = "))
    if resposta == resultado:
        print("Você fez a conta corretamente, parabéns!")
        acertos = acertos + 1
        m = m+1
    else:
        print(f"incorreto, o valor correto da multiplicação entre {n} e {m} é {resultado}")
        erros = erros + 1
        m = m+1
print(f"Você acertou {acertos} e errou {erros}")