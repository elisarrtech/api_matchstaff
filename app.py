import os
import json
import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Leer credenciales desde variable de entorno
credentials_json = os.getenv('GOOGLE_CREDENTIALS_JSON')
if not credentials_json:
    raise Exception("No se encontró la variable de entorno GOOGLE_CREDENTIALS_JSON")

info = json.loads(credentials_json)
creds = Credentials.from_service_account_info(info, scopes=SCOPES)
client = gspread.authorize(creds)

SPREADSHEET_ID = "1_4dlQIi1D4Ui_XejLz_GYTE3zc4hke54nBQ5KEkhnZs"
SHEET_NAME = "Hoja1"

questions = [
    {"id": "nombre", "pregunta": "¿Cuál es tu nombre completo?"},
    {"id": "edad", "pregunta": "¿Qué edad tienes?"},
    {"id": "escolaridad", "pregunta": "¿Cuál es tu escolaridad?"},
    {"id": "colonia", "pregunta": "¿En qué colonia vives?"},
    {"id": "tiempo_kelloggs", "pregunta": "¿A cuánto tiempo está la empresa Kellogg’s desde tu casa? Por el momento no contamos con transporte."},
    {"id": "experiencia", "pregunta": "Cuéntame sobre tu experiencia laboral."},
    {"id": "ultimo_trabajo", "pregunta": "¿Dónde fue tu último trabajo y por qué se terminó?"},
    {"id": "sueldo_anterior", "pregunta": "¿Cuánto ganabas semanalmente en tu último trabajo?"},
    {"id": "mayor_experiencia", "pregunta": "¿Cuál consideras que es tu mayor experiencia en la industria?"},
    {"id": "vacante_interes", "pregunta": "¿Qué vacante te interesa?"}
]

@app.route("/")
def home():
    return "Chatbot Matchstaff backend activo"

@app.route("/get_questions", methods=["GET"])
def get_questions():
    # Devuelve las preguntas menos 'nombre', 'tiempo_kelloggs' y 'vacante_interes' (que se manejan en frontend)
    filtered = [q for q in questions if q["id"] not in ["nombre", "tiempo_kelloggs", "vacante_interes"]]
    return jsonify(filtered)

@app.route("/guardar-en-sheets", methods=["POST"])
def guardar_en_sheets():
    try:
        data = request.json.get("data", [])
        print("Datos recibidos para guardar:", data)

        sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
        sheet.append_row(data)

        return jsonify({"message": "Datos guardados correctamente en Google Sheets."})
    except Exception as e:
        print("Error guardando en Sheets:", e)
        return jsonify({"message": "Error al guardar en Sheets.", "error": str(e)}), 500

@app.route("/submit_answers", methods=["POST"])
def submit_answers():
    print("Respuestas recibidas:", request.json)
    return jsonify({"message": "¡Gracias! Recibimos tus respuestas y pronto te contactaremos."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
