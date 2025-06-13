# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # https://161.3.140.22:5000/ # access receiver first before access sender
def index():

    return render_template("receiver.html")


@app.route("/sender") # https://161.3.140.22:5000/sender 
def sender():
    return render_template("sender.html")





if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000, debug=True) # for http
    
    # local host
    # app.run(host='127.0.0.1', port=5000, debug=True, ssl_context=('cert.pem', 'key.pem')) 
    
    # not local
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem')) 
