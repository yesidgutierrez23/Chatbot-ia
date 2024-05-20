import os
import logging
from flask import Flask, request, jsonify, render_template, abort
import requests
from dotenv import load_dotenv
import openai

# Cargar variables de entorno desde el archivo .env
load_dotenv()
API_KEY = os.getenv('API_KEY')  # General API Key (if needed)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # OpenAI specific API Key

app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    # Renderiza la página HTML principal para el chatbot
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    if not request.json or 'message' not in request.json:
        abort(400, 'Bad Request: No message provided.')

    user_message = request.json['message']
    response_message = process_message(user_message)
    return jsonify({"response": response_message})

def process_message(message):
    if not message:
        return "No se ha proporcionado un mensaje válido."

    try:
        if "advanced" in message:
            return get_openai_response(message)
        else:
            return get_simple_api_response(message)
    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return "Error al procesar la solicitud."

def get_openai_response(message):
    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        logging.error(f"Error in OpenAI response: {e}")
        return "Error al obtener respuesta de OpenAI."

def get_simple_api_response(message):
    api_url = "https://api.openai.com/v1/asistentes"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": message
    }
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # Lanza un error para estados 4xx y 5xx
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP Error: {e}")
        return "Error al comunicarse con la API externa."

if __name__ == '__main__':
    app.run(debug=False)  # debug=False para producción
