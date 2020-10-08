from controller.funcoesGlobais import funcoesGlobais
from controller.constantes import constantes
import csv
from datetime import datetime


func = funcoesGlobais()
const = constantes()

dddEstado = const.get_dddEstado()
idBroker = const.get_idBroker()

mensagensValidas = []
logErros = []

ficheiro = open('exemplo.csv', 'r')
reader = csv.reader(ficheiro)
for linha in reader:
    dados = linha[0].split(';')
    idmensagem = dados[0]
    ddd = dados[1]
    celular = dados[2]
    operadora = dados[3]
    horario_envio = dados[4]
    mensagem = dados[5]
    numIdBroker = idBroker[operadora]
    msg_erro = ''
    
    
    if func.validaTelefone(ddd, celular, dddEstado) == False:
        msg_erro = msg_erro + 'Número de telefone inválido;'
    
    if func.validaEstadoSP(ddd, dddEstado) == False:
        msg_erro = msg_erro + 'DDD pertence a SP;'
    
    if func.consultaBlacklist(ddd, celular) == False:
        msg_erro = msg_erro + 'Telefone está na Blacklist;'
        
    if func.validaMensagem(mensagem) == False:
        msg_erro = msg_erro + 'Mensagem possui mais de 140 caracteres;'
    
    if func.validaHorario(horario_envio) == False:
        msg_erro = msg_erro + 'Envio da mensagem após às 19:59:59;'
    
    if msg_erro == '':
        temNoArray = False
        for regm in mensagensValidas:
            if regm[1] == ddd+celular:
                temNoArray = True
                now = datetime.now()
                horariocsv = now.replace(hour = int(horario_envio[0:2]), minute= int(horario_envio[3:5]), second=int(horario_envio[6:8]))
                horarioarray = now.replace(hour = int(regm[2][0:2]), minute= int(regm[2][3:5]), second=int(regm[2][6:8]))
                if horariocsv < horarioarray:
                    regm[0] = idmensagem
                    regm[2] = horario_envio
                    regm[3] = numIdBroker
        if temNoArray == False:                               
            mensagensValidas.append([idmensagem, ddd+celular, horario_envio, numIdBroker])   
    else:
        logErros.append([idmensagem, msg_erro])
        print('id_mensagem: '+ idmensagem+' erros: '+msg_erro)    
    
print('Mensagens válidas:')
print('id_mensagem; id_broker ')
for msgValidas in mensagensValidas:
    print(msgValidas[0]+';'+str(msgValidas[3]))

func.geraResultado(mensagensValidas)
func.geraLogErros(logErros)




