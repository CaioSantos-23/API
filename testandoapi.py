import requests

link = "https://179dc84a-4887-4b11-a2e8-d1380c61e056-00-1zxonqapxu9iw.kirk.replit.dev/pegarvendas"

requisicao = requests.get(link)
print(requisicao)
print(requisicao.json())
