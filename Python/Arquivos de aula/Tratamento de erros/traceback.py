import traceback

try:
    nome_arquivo = input("Informe o nome do arquivo: ").strip()
    arquivo = open(nome_arquivo)
except:
    trace = traceback.format_exc()

    print("Ocorreu um erro:\n", trace)
    open('trace.log', 'a').write(trace)