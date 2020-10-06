from heroi import Heroi

#homem_aranha = Heroi()
#homem_aranha.lanca_teia = True 

miranha = Heroi(False, False, True, "")
miranha.detalhar()

#arqueiro_verde = Heroi()
#arqueiro_verde.possui_arma = True

arqueiro_verde = Heroi(False, True, False, "")
arqueiro_verde.detalhar()
arqueiro_verde.falar()

#he_man = Heroi()
#he_man.frase_comum = "Eu tenho a força"

he_man = Heroi(False, True, False, "Eu tenho a força.")
he_man.detalhar()
he_man.falar()