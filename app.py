import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify

from Users import User
from openweaher_api import Weather

load_dotenv()

TOKEN_WEATHER_API = os.getenv('TOKEN_WEATHER_API')

weather = Weather(TOKEN_WEATHER_API)

db = User('users.db')
db.create_table()
db.add_test_user()

app = Flask(__name__)


@app.route('/change_balance_minus', methods=['POST'])
def change_balance_minus():
    """Вычитаем температуру из баланса"""
    request_data = request.get_json()

    if "userId" in request_data and "city" in request_data:
        city = request_data['city']
        user_id = int(request_data['userId'])
        balance = db.get_user_balance(user_id)
        temperature = str(weather.fetch_weather(city)).replace("-", "")
        new_balance = balance - int(temperature)
        if new_balance < 0:
            return {"text": f"У вас недостаточно средств {new_balance}"}
        else:

            db.update_user_balance(user_id, new_balance)
            balance = db.get_user_balance(user_id)
        return jsonify(balance)


@app.route('/change_balance_plus', methods=['POST'])
def change_balance_plus():
    """Прибавляем температуру к балансу"""
    request_data = request.get_json()

    if "userId" in request_data and "city" in request_data:
        city = request_data['city']
        user_id = int(request_data['userId'])
        balance = db.get_user_balance(user_id)
        temperature = str(weather.fetch_weather(city)).replace("-", "")
        new_balance = balance + int(temperature)
        db.update_user_balance(user_id, new_balance)
        balance = db.get_user_balance(user_id)
        return jsonify(balance)
    return jsonify(request_data)

if __name__ == '__main__':
    app.run(debug=True)
