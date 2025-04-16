# api_b_weather.py
from flask import Flask, jsonify

app = Flask(__name__)

# Simulando um "banco de dados" simples de temperaturas por cidade
weather_data = {
    "SãoPaulo": 25,
    "RioDeJaneiro": 33,
    "Curitiba": 12,
    "Salvador": 28
}

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    temp = weather_data.get(city)
    if temp is not None:
        return jsonify({
            "city": city,
            "temp": temp,
            "unit": "Celsius"
        })
    else:
        return jsonify({"error": "Cidade não encontrada"}), 404

if __name__ == '__main__':
    app.run(port=5001)
