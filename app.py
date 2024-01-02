from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = "Sheetal Chakravarthy" 
    usn = "1BM20IS142"   
    return f"Hello, {name} ({usn})!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
