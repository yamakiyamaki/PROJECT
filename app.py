# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_xr_llama copy.html")
    # return render_template("initial.html")

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000, debug=True) # for http
    
    # local host
    # app.run(host='127.0.0.1', port=5000, debug=True, ssl_context=('cert.pem', 'key.pem')) 
    
    # not local
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem')) 

#TODO: check index_xr_llama.html