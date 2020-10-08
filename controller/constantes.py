


class constantes:
    def __init__(self):
        print('objeto constantes instanciado')
        self.__dddEstado = {  "AC": ["68"],
                            "AL": ["82"],
                            "AM": ["92", "97"],
                            "AP": ["96"],
                            "BA": ["71", "73", "74", "75", "77"],
                            "CE": ["85", "88"],
                            "DF": ["61"],
                            "ES": ["27", "28"],
                            "GO": ["62", "64"],
                            "MA": ["98", "99"],
                            "MG": ["31", "32", "33", "34", "35", "37", "38"],
                            "MS": ["67"],
                            "MT": ["65", "66"],
                            "PA": ["91", "93", "94"],
                            "PB": ["83"],
                            "PE": ["81", "87"],
                            "PI": ["86", "89"],
                            "PR": ["41", "42", "43", "44", "45", "46"],
                            "RJ": ["21", "22", "24"],
                            "RN": ["84"],
                            "RO": ["69"],
                            "RR": ["95"],
                            "RS": ["51", "53", "54", "55"],
                            "SC": ["47", "48", "49"],
                            "SE": ["79"],
                            "SP": ["11", "12", "13", "14", "15", "16", "17", "18", "19"],
                            "TO": ["63"]
                        },
        self.__idBroker = {
                            "VIVO": 1,
                            "TIM": 1,
                            "CLARO": 2,
                            "OI": 2,
                            "NEXTEL": 3           
                        }
    
    
    def get_dddEstado(self):
        return self.__dddEstado[0]
    
    
    def get_idBroker(self):
        return self.__idBroker


pass
        