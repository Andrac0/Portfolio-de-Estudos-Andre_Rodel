import tempfile

with tempfile.TemporaryDirectory() as tmpdirname:
    print("Diretório temporário:", tmpdirname)