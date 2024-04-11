import requests
import json

# text = "Uma rede neural é um método de inteligência artificial que ensina computadores a processar dados de uma forma inspirada pelo cérebro humano. É um tipo de processo de machine learning, chamado aprendizado profundo, que usa nós ou neurônios interconectados em uma estrutura em camadas, semelhante ao cérebro humano. A rede neural cria um sistema adaptativo que os computadores usam para aprender com os erros e se aprimorar continuamente. As redes neurais artificiais tentam solucionar problemas complicados, como resumir documentos ou reconhecer rostos com grande precisão."

def recebe_texto(text):
    # Substitua YOUR_API_KEY pela sua chave de API
    API_KEY = "YOUR_GOOGLE_API_KEY"
    url = "https://translation.googleapis.com/language/translate/v2"

    params = {
        'q': text,
        'source': 'pt',
        'target': 'en',
        'format': 'text',
        'key': API_KEY,
    }

    response = requests.post(url, params=params)
    result = response.json()

    if 'data' in result and 'translations' in result['data'] and len(result['data']['translations']) > 0:
        translated_text = result['data']['translations'][0]['translatedText']
        print(translated_text)
        return translated_text
    else:
        print("Não foi possível traduzir o texto.")
