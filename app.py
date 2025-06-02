# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_xr.html")
    # return render_template("initial.html")

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000, debug=True) # for http
    
    # local host
    # app.run(host='127.0.0.1', port=5000, debug=True, ssl_context=('cert.pem', 'key.pem')) # for https TODO
    
    # not local
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem')) # for https TODO

    #TODO: Is it OK? # openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 1 -nodes
    # FR # Auvergne-Rhône-Alpes # Saint-Étienne
    # TODO: I need to find a way to connect displayin device and the server with https. 
    # I need to make it webxr compatible and capable for updating scen continuously. 
    # mkcert is needed? need to sudo access
