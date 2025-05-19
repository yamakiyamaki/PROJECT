# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_xr.html")
    # return render_template("initial.html")

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True) # for http
    # app.run(ssl_context=('cert.pem', 'key.pem')) # for https TODO

    #TODO: Is it OK? # openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 1 -nodes
    # FR # Auvergne-Rhône-Alpes # Saint-Étienne
