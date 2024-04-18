from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hey buddy im new to docker....:)'

app.run(host='0.0.0.0', port=81, debug=True)