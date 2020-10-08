## 📚  Descrição 

Aplicação que lê um arquivo 'exemplo.csv' contendo os campos:

_IDMENSAGEM;DDD;CELULAR;OPERADORA;HORARIO_ENVIO;MENSAGEM_

Exemplo:
```
bff58d7b-8b4a-456a-b852-5a3e000c0e63;12;996958849;NEXTEL;21:24:03;sapien sapien non mi integer ac neque duis bibendum
b7e2af69-ce52-4812-adf1-395c8875ad30;46;950816645;CLARO;19:05:21;justo lacinia eget tincidunt eget
e7b87f43-9aa8-414b-9cec-f28e653ac25e;34;990171682;VIVO;18:35:20;dui luctus rutrum nulla tellus in sagittis dui
c04096fe-2878-4485-886b-4a68a259bac5;43;940513739;NEXTEL;14:54:16;nibh fusce lacus purus aliquet at feugiat
d81b2696-8b62-4b8b-af82-586ce0875ebc;21;983522711;TIM;16:42:48;sit amet eros suspendisse accumsan tortor quis turpis sed ante
g81b2696-8b62-4b8b-af82-586ce0875ebc;00;983522711;TIM;16:42:48;sit amet eros suspendisse accumsan tortor quis turpis sed ante
h81b2696-8b62-4b8b-af82-586ce0875ebc;24;986722083;TIM;16:42:48;sit amet eros suspendisse accumsan tortor quis turpis sed ante
j81b2696-8b62-4b8b-af82-586ce0875ebc;24;986722083;TIM;16:42:48;sit amet eros suspendisse accumsan tortor quis turpis sed ante dui luctus rutrum nulla tellus in sagittis dui sapien sapien non mi integer ac neque duis bibendum
p7b87f43-9aa8-414b-9cec-f28e653ac25e;34;990171682;VIVO;18:29:20;dui luctus rutrum nulla tellus in sagittis dui
e7b87f43-9aa8-414b-9cec-f28e653ac25e;34;990171682;VIVO;18:45:20;dui luctus rutrum nulla tellus in sagittis dui
```
e retorna um arquivo 'resultado.csv', com as mensagens aptas para envio contendo os campos:

_IDMENSAGEM;IDBROKER_

Exemplo:
```
p7b87f43-9aa8-414b-9cec-f28e653ac25e;1
d81b2696-8b62-4b8b-af82-586ce0875ebc;1
```
e um arquivo 'logErros.csv' contendo as mensagens inaptas para envio, e os motivos de cada mensagem ter sido bloqueada, contendo os campos:

_IDMENSAGEM;MENSAGEM_ERRO_
Exemplo:
```
bff58d7b-8b4a-456a-b852-5a3e000c0e63;"DDD pertence a SP;Envio da mensagem após às 19:59:59;"
b7e2af69-ce52-4812-adf1-395c8875ad30;"Número de telefone inválido;Telefone está na Blacklist;"
c04096fe-2878-4485-886b-4a68a259bac5;"Número de telefone inválido;"
g81b2696-8b62-4b8b-af82-586ce0875ebc;"Número de telefone inválido;"
h81b2696-8b62-4b8b-af82-586ce0875ebc;"Telefone está na Blacklist;"
j81b2696-8b62-4b8b-af82-586ce0875ebc;"Telefone está na Blacklist;Mensagem possui mais de 140 caracteres;"
```

## 🚀 Tecnologias Usadas 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">

Desenvolvido em Python 3.8.0
SO utilizado: Windows 10
IDE utilizada: VSCode

## 📌 Estrutura do Projeto 
    |-- controller
       |-- constantes.py
       |-- funcoesGlobais.py
    |-- exemplo.csv
    |-- logErros.csv
    |-- main.py
    |-- README.md
    |-- requirements.txt
    |-- resultado.csv    
    
main.py -> Arquivo principal que contém a execução do projeto.

constantes.py -> Dicionários contendo o IDBroker e o dddEstado.

funcoesGlobais.py -> Arquivo contendo a classe funcoesGlobais com as funções necessárias para validação das mensagens no arquivo principal. 

exemplo.csv -> Arquivo CSV contendo as mensagens para validação. 

logErros.csv -> Arquivo gerado na execução do código main.py, contendo as mensagens bloqueadas e os motivos do bloqueio. 

resultado.csv -> Arquivo gerado na execução do código main.py, contendo as mensagens válidas para envio.

requirements.txt -> Bibliotecas utilizadas no python 

## 📢 Como executar

Requisitos:

Python 3.8.0<br>

Instalar todas as dependências do python usando o arquivo requirements.txt que está no projeto:  

```bash 
pip install  -r requirements.txt
 ```  
Ao executar o comando acima, será feita a instalação das seguintes bibliotecas:

```
certifi==2020.6.20
chardet==3.0.4
idna==2.10
python-dateutil==2.8.1
pytz==2020.1
requests==2.24.0
six==1.15.0
urllib3==1.25.10
```

 Executar o main.py no cmd com o comando:

```bash 
python main.py
 ```  

## 🔓 Licença 
MIT © [Matheus Muller](https://www.linkedin.com/in/matheus-herrera-bezerra-muller/)
