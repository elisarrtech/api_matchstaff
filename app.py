import os
import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Carga credenciales JSON desde archivo o variable de entorno
# Para Render puedes guardar el JSON como variable de entorno (por ejemplo, GOOGLE_CREDENTIALS_JSON)
# Aquí ejemplo leyendo archivo local
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Asegúrate subir este archivo en Render o adaptar

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

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

        # Suponiendo que data es lista de strings o similar
        sheet.append_row(data)
        return jsonify({"message": "Datos guardados correctamente en Sheets."})
    except Exception as e:
        print("Error al guardar en Sheets:", e)
        return jsonify({"message": "Error al guardar en Sheets.", "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
