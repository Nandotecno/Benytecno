class Televisao():

    def _init_(self):
        self.ligada = False
        self.canal = 2

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1

if __name__ == '_main_':
    tv = Televisao()
    print('Canal inicial:', tv.canal)
    print('Ligada:', tv.ligada)

    tv.ligada = True
    tv.canal = 5

    print('Ligada:', tv.ligada)
    print('Canal inicial:', tv.canal)
    tv.muda_canal_para_cima()
    print('Canal +', tv.canal)
    tv.muda_canal_para_cima()
    print('Canal +', tv.canal)
    tv.muda_canal_para_baixo()
    print('Canal -', tv.canal)