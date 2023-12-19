# Conversor de moeda estrangeira em real

import requests

def getCotacao(codMoeda):
    try:
        requisicao - requests.get(f'https://economia.awesomeapi.com.br/json/last/:{codMoeda}-BRL')

        dic = requisicao.json()

        cotacao = dic[f'{codMoeda}BRL']['bid']

        return cotacao

    except:
          print('Codigo da moeda invalido.')
          return None

# Teste

print(f'USD 1.00 = R$ {getCotacao("USD")}')

