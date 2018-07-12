#!flask/bin/python
import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/card_actions/<card_number>')
def card_actions(card_number):
    return redirect("http://www.example.com", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)