def teste(nome, sobrenome):
    print(f"O nome é: {nome}")
    print(f"O sobrenome é: {sobrenome}")

dic = {'nome':'André', 'sobrenome':'Wolkers'}
print(*dic)
teste(**dic)