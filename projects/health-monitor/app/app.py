# Boiler plate
from flask import Flask
app = Flask(__name__)

@app.route('/metrics')
def metrics():
    return "your data here"

app.run(host='0.0.0.0', port=5000)