

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f'{self.dia:02}/{self.mes:02}/{self.ano:04}')
