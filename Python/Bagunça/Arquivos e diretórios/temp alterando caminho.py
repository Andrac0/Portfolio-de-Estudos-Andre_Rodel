import tempfile

print("Diretório temporário corrente:", tempfile.gettempdir())

tempfile.tempdir = "C:\\temp"
print("Diretório temporário após a alteração:", tempfile.gettempdir())

with tempfile.TemporaryFile() as arq:
    print("Nome do arquivo:", arq.name)