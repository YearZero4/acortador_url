from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pyshorteners, os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    acortada = None
    error = None

    if request.method == 'POST':
        url = request.form['url']
        acortador = pyshorteners.Shortener()
        
        try:
            acortada = acortador.dagd.short(url)
        except Exception as e:
            error = str(e)

    return render_template('index.html', acortada=acortada, error=error)

@app.route('/acortar', methods=['POST'])
def acortar():
    url = request.json.get('url')
    acortador = pyshorteners.Shortener()
    try:
        acortada = acortador.dagd.short(url)
        return jsonify(acortada=acortada)
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))
