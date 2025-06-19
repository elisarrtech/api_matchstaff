import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

questions = [
    {"id": "nombre", "pregunta": "¿Cuál es tu nombre completo?"},
    {"id": "edad", "pregunta": "¿Qué edad tienes?"},
    {"id": "escolaridad", "pregunta": "¿Cuál es tu escolaridad?"},
    {"id": "colonia", "pregunta": "¿En qué colonia vives?"},
    {"id": "tiempo_kelloggs", "pregunta": "¿A cuánto tiempo está la empresa Kellogg’s desde tu casa? Por el momento no contamos con transporte."},
    {"id": "experiencia", "pregunta": "Cuéntame sobre tu experiencia laboral."},
    {"id": "ultimo_trabajo", "pregunta": "¿Dónde fue tu último trabajo y por qué se terminó?"},
    {"id": "sueldo_anterior", "pregunta": "¿Cuánto ganabas en tu último trabajo?"},
    {"id": "mayor_experiencia", "pregunta": "¿Cuál consideras que es tu mayor experiencia en la industria?"}
]

GOOGLE_SHEETS_WEBHOOK = "https://script.google.com/macros/s/AKfycbxo4FZDa9jGdOW01OwYkLDKIRWeDbZcqq9ZcMzyRDPauuYwn-jfr4r7Ydf4TbRRQR8ugQ/exec"  # <--- reemplaza con el tuyo

@app.route("/")
def home():
    return "Chatbot Matchstaff backend activo"

@app.route("/get_questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

@app.route("/guardar-en-sheets", methods=["POST"])
def guardar_en_sheets():
    data = request.json.get("data", [])
    print("Datos a guardar:", data)

    try:
        response = requests.post(GOOGLE_SHEETS_WEBHOOK, json={"data": data})
        if response.status_code == 200:
            return jsonify({"message": "Datos guardados correctamente en Sheets."})
        else:
            return jsonify({"message": "Error al guardar en Sheets."}), 500
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"message": "Fallo la conexión con Google Sheets."}), 500

@app.route("/submit_answers", methods=["POST"])
def submit_answers():
    print("Respuestas recibidas:", request.json)
    return jsonify({"message": "¡Gracias! Recibimos tus respuestas y pronto te contactaremos."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
