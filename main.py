from controller.funcoesGlobais import funcoesGlobais
from controller.constantes import constantes
import csv


func = funcoesGlobais()
const = constantes()

dddEstado = const.get_dddEstado()
idBroker = const.get_idBroker()

mensagensValidas = []

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
        mensagensValidas.append([idmensagem, ddd+celular, horario_envio, numIdBroker])   
        
    print(msg_erro)
        
    




