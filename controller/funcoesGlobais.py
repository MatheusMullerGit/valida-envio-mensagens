import requests
from datetime import datetime
import csv


class funcoesGlobais:
    def __init__(self):
        print('objeto de funções instanciado')
    
    
    def validaTelefone(self, ddd, celular, dddEstado):
        validaddd = False
        if not len(ddd) == 2:
            return False
        for reg in dddEstado:
            if ddd in dddEstado[reg]:
                validaddd = True
        if validaddd == False:
            return False
        if not len(celular) == 9:
            return False
        if not celular[0] == '9':
            return False
        if not int(celular[1]) > 6:
            return False
        return True
    
    
    def consultaBlacklist(self, ddd, celular):
        url = 'https://front-test-pg.herokuapp.com/blacklist/'+ddd+celular
        retorno = requests.get(url)
        if retorno.status_code == 200:
            return False
        return True
    
    
    def validaEstadoSP(self, ddd, dddEstado):
        if ddd in dddEstado['SP']:
            return False
        return True
    
    
    def validaHorario(self, horario):
        now = datetime.now()
        horariovalidar = now.replace(hour = int(horario[0:2]), minute= int(horario[3:5]), second=int(horario[6:8]))
        if horariovalidar > now.replace(hour=19, minute=59, second=59):
            return False
        return True
    
    
    def validaMensagem(self, mensagem):
        if len(mensagem) > 140:
            return False
        return True
    
        
    def geraLogErros(self, arrayErros):
        with open('logErros.csv', 'w', encoding='utf-8') as arquivo_csv:
            for reg in arrayErros:
                escrever = csv.writer(arquivo_csv, delimiter=';', lineterminator='\n')
                escrever.writerow([reg[0],reg[1]])
            print('LogErros gerado com sucesso')
            

    def geraResultado(self, array):
        with open('resultado.csv', 'w') as arquivo_csv:
            for reg in array:
                escrever = csv.writer(arquivo_csv, delimiter=';', lineterminator='\n')
                escrever.writerow([reg[0],reg[3]])
            print('Arquivo gerado com sucesso')

    
pass
