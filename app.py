import os
from flask import Flask, request, jsonify, render_template
import requests
from dotenv import load_dotenv
import openai

# Cargar variables de entorno desde el archivo .env
load_dotenv()
API_KEY = os.getenv('API_KEY')  # General API Key (if needed)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # OpenAI specific API Key

app = Flask(__name__)

@app.route('/')
def home():
    # Renderiza la página HTML principal para el chatbot
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    # Recibe el mensaje del usuario desde el cliente web
    data = request.json
    user_message = data.get('message')
    # Procesa el mensaje utilizando la función process_message
    response_message = process_message(user_message)
    # Devuelve la respuesta en formato JSON
    return jsonify({"response": response_message})

def process_message(message):
    # Decidir si se usa la API general o la de OpenAI según el contenido del mensaje
    if "advanced" in message:
        # Uso de OpenAI para respuestas más complejas
        return get_openai_response(message)
    else:
        # Uso de una API externa simple para otras consultas
        return get_simple_api_response(message)

def get_openai_response(message):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message['content']

def get_simple_api_response(message):
    api_url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": message
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return "Lo siento, no puedo procesar tu solicitud en este momento."

if __name__ == '__main__':
    app.run(debug=True)

