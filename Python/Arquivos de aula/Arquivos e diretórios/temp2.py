import tempfile

arq = tempfile.TemporaryFile()

arq.write(b"Curso python para todos")

arq.seek(0)

print(arq.read())

arq.close()