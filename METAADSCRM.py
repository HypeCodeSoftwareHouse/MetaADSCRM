import requests
import hashlib
import time

PIXEL_ID = '2376688635807875'
ACCESS_TOKEN = 'EAAGYpc3bMHEBOyodoZBAiTmI0jqG9QCe4dw5yfktqbdZCCEGe0q30LaAFfSlNOyqAZCrSz14vY3eWIjpJPE4BAZBkqDy0cDsfviKgJT7MyFKvS7M64r7RjJBiXpH2BuZBwCPfSAGam4xdWwYqzdaVw6ZC07RPlsVpfEaCOmR5IKtrGca2vM1oVZClw0e7ZB8TOv9tgZDZD'

def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def send_meta_event(event_name, user_data):
    url = f"https://graph.facebook.com/v12.0/{PIXEL_ID}/events"
    payload = {
        'data': [{
            'event_name': event_name,
            'event_time': int(time.time()),
            'user_data': user_data,
            'action_source': 'website',
        }],
        'access_token': ACCESS_TOKEN
    }
    response = requests.post(url, json=payload)
    return response.json()

def monitor_crm_and_trigger_event():
    # Código para monitorar o CRM e detectar quando um lead é movido para a coluna "agendados".
    # Isto pode variar dependendo de como você acessa os dados do CRM Exact Spotter.

    # Exemplo simplificado de dados do usuário:
    email = 'user@example.com'
    phone_number = '1234567890'

    user_data = {
        'em': hash_data(email),
        'ph': hash_data(phone_number)
    }

    response = send_meta_event('AddToCart', user_data)
    print(response)

if __name__ == "__main__":
    monitor_crm_and_trigger_event()
