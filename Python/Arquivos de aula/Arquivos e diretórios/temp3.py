import tempfile

with tempfile.TemporaryFile() as arq:
    arq.write(b'Curso Python para todos')
    arq.seek(0)
    print(arq.read())