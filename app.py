from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Aquí defines tu lista de preguntas
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

# Aquí va el endpoint para obtener las preguntas
@app.route("/get_questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

# Otros endpoints que tengas
@app.route("/submit_answers", methods=["POST"])
def submit_answers():
    print(request.json)
    return jsonify({"message": "¡Gracias! Recibimos tus respuestas y pronto te contactaremos."})

# Ruta para la raíz
@app.route("/")
def home():
    return "Chatbot Matchstaff backend activo"

# Bloque para ejecutar el servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
