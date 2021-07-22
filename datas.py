

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        # print(f'{self.dia:02}/{self.mes:02}/{self.ano:04}')
        print('{0:02d}/{1:02d}/{2:04d}'.format(self.dia, self.mes, self.ano))
        # Tenho que ver como corrigir o problema de digitar 08 exemplo:
        # d = Data(26, 08, 1986)
        # File "<input>", line 1
        # d = Data(26, 08, 1986)
        #               ^
        # SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers