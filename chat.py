from time import sleep
import requests

print(r"""
=================================================================
  _____                       _                       _     ___ 
 |_   _|  ___   _ _   _ __   (_)  _ _    __ _        /_\   |_ _|
   | |   / -_) | '_| | '  \  | | | ' \  / _` |  _   / _ \   | | 
   |_|   \___| |_|   |_|_|_| |_| |_||_| \__,_| (_) /_/ \_\ |___|
=================================================================
""")
sleep(1.5)
print(
    'Usuário: Aprendiz\n'
    'Modelo: Pattonico\n'
    'Digite "sair" para encerrar\n'
    )
sleep(1.5)

while True:
    prompt = input('Aprendiz -> ')
    if prompt.lower() in ['sair', 'exit', 'quit', 'q']:
        break

    try:
        response = requests.post('http://localhost:8000/generate', json={'prompt': prompt})
        result = response.json()['response'].strip()
        print('Pattonico -> ', result + '/n')
    except Exception as e:
        print('Erro ao se comunicar com a API: ', e)