from flask import Flask, render_template, request
from scripts.download_data import download

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    context = {
        'symb': 'None', 'price': 'off', 'volume': 'off', 'num-price': '0', 'num-volume': '0'
    }

    if request.method == "POST":
        settings = request.form
        if settings['symb'] != 'None':
            data = download(settings['symb'], "1d")["Open"].to_list()
            context = {
                "data": data,
                "symb": settings['symb']
            }
            return render_template('index.html', name="home", **context)
    return render_template('index.html', name="home") 

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)