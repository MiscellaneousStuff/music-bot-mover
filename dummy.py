from flask import Flask

# Flask Dummy
app = Flask(__name__)

@app.route('/')
def helloIndex():
    return "Woi"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)