import os
import json
import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Cargar credenciales desde variable de entorno GOOGLE_CREDENTIALS_JSON
creds_dict = json.loads(os.environ.get('GOOGLE_CREDENTIALS_JSON', '{}'))
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
client = gspread.authorize(creds)

# ID de tu Google Sheet ya incorporado
SPREADSHEET_ID = "1_4dlQIi1D4Ui_XejLz_GYTE3zc4hke54nBQ5KEkhnZs"
SHEET_NAME = "Hoja1"

@app.route("/")
def home():
    return "Chatbot Matchstaff backend activo"

@app.route("/guardar-en-sheets", methods=["POST"])
def guardar_en_sheets():
    data = request.json.get("data", [])
    print("Datos a guardar:", data)

    try:
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

        fila = []
        for item in data:
            if isinstance(item, dict) and "respuesta" in item:
                fila.append(item["respuesta"])
            else:
                fila.append(str(item))

        sheet.append_row(fila)
        return jsonify({"message": "Datos guardados correctamente en Sheets."})
    except Exception as e:
        print("Error al guardar en Sheets:", e)
        return jsonify({"message": "Error al guardar en Sheets.", "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
