# api_a_recommendation.py
from flask import Flask, jsonify
import requests
from functools import lru_cache

app = Flask(__name__)

# Simples cache com LRU para armazenar as últimas 32 cidades consultadas
@lru_cache(maxsize=32)
def get_weather_from_api_b(city):
    try:
        response = requests.get(f'http://localhost:5001/weather/{city}')
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException:
        return None

@app.route('/recommendation/<city>', methods=['GET'])
def get_recommendation(city):
    weather = get_weather_from_api_b(city)
    
    if not weather:
        return jsonify({"error": "Não foi possível obter dados da cidade"}), 404

    temp = weather["temp"]

    if temp > 30:
        recommendation = "Está muito quente! Beba bastante água e use protetor solar."
    elif 15 < temp <= 30:
        recommendation = "O clima está agradável. Aproveite o dia!"
    else:
        recommendation = "Está frio! Não esqueça de usar um casaco."

    return jsonify({
        "city": weather["city"],
        "temperature": weather["temp"],
        "unit": weather["unit"],
        "recommendation": recommendation
    })

if __name__ == '__main__':
    app.run(port=5000)
