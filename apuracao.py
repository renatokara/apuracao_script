from urllib.error import HTTPError
from urllib.request import urlopen
import time
import json
import pandas as pd  
#url = "https://t.co/Dc1k2zUUQZ"
url = "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"

# Tempo de espera entre as requisicoes (em segundos)
TIME_REQ = 15 
print("iniciando")
while True:
    try :
        response = urlopen(url)
        data_json = json.loads(response.read())
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        candidates, votes = [], []
        for m in data_json['cand']:
             candidates.append(m['nm'])
             votes.append(m['pvap'])
        data ={'candidates':candidates, 'votes': votes }
        df = pd.DataFrame(data)  
        print("\n"*3)
        print("#"*33)
        print(f"atualizado em {t}")
        print(f"percentual urnas apuradas: {data_json['psi']}% \n" )
        print(df)
        print("#"*33)
        #for candidate in data_json['cand']:
        #    print("{} : {} ".format(candidate['nm'], candidate['pvap']))
    except HTTPError:
        print("HTTP Error")
    time.sleep(TIME_REQ)