from flask import Flask, request, jsonify
import bd
app = Flask(__name__)

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_NINJAS_KEY")

import requests


@app.route("/api/frase", methods=["GET"])
def obtener_frase():
    if not API_KEY:
        return jsonify({"error": "API key no configurada"}), 500

    url = "https://api.api-ninjas.com/v2/quotes"
    headers = {"X-Api-Key": API_KEY}

    respuesta = requests.get(url, headers=headers)

    if respuesta.status_code != 200:
        return jsonify({"error": "No se pudo consultar la API"}), 400

    return jsonify(respuesta.json()), 200



@app.route("/api/recursos", methods=["GET"])
def listar_recursos():
    return jsonify(bd.recursos), 200

@app.route("/api/recursos/<int:id>", methods=["GET"])
def obtener_recurso(id):
    if id not in bd.recursos:
        return jsonify({"error": "Recurso no encontrado"}), 404

    return jsonify(bd.recursos[id]), 200


@app.route("/api/recursos", methods=["POST"])
def crear_recurso():
    if not request.is_json:
        return jsonify({"error": "El cuerpo debe ser JSON"}), 400

    datos = request.get_json()

    if "nombre" not in datos:
        return jsonify({"error": "Falta el campo nombre"}), 400

    nuevo_id = max(bd.recursos.keys(), default=0) + 1
    bd.recursos[nuevo_id] = {"nombre": datos["nombre"]}

    return jsonify({"id": nuevo_id, "nombre": datos["nombre"]}), 201


@app.route("/api/recursos/<int:id>", methods=["PUT"])
def actualizar_recurso(id):
    if id not in bd.recursos:
        return jsonify({"error": "Recurso no encontrado"}), 404

    if not request.is_json:
        return jsonify({"error": "El cuerpo debe ser JSON"}), 400

    datos = request.get_json()

    if "nombre" not in datos:
        return jsonify({"error": "Falta el campo nombre"}), 400

    bd.recursos[id] = {"nombre": datos["nombre"]}

    return jsonify(bd.recursos[id]), 200


@app.route("/api/recursos/<int:id>", methods=["DELETE"])
def eliminar_recurso(id):
    if id not in bd.recursos:
        return jsonify({"error": "Recurso no encontrado"}), 404

    del bd.recursos[id]

    return jsonify({"mensaje": "Recurso eliminado"}), 200


if __name__ == "__main__":
    app.run(debug=True)
