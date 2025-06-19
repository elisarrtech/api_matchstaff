from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Chatbot Matchstaff backend activo"

questions = [
  # ... tus preguntas ...
]

@app.route("/get_questions")
def get_questions():
  return jsonify(questions)

@app.route("/submit_answers", methods=["POST"])
def submit_answers():
  print(request.json)
  return jsonify({"message": "¡Gracias! Recibimos tus respuestas y pronto te contactaremos."})
