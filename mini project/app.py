from flask import Flask, render_template, request, jsonify
from converter import CurrencyConverter

app = Flask(__name__)
converter = CurrencyConverter(api_url="https://api.exchangerate-api.com/v4")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.get_json()
    amount = data['amount']
    from_currency = data['from_currency']
    to_currency = data['to_currency']
    result = converter.convert(amount, from_currency, to_currency)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
