from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')  # Serves index.html from the same folder

if __name__ == '__main__':
    app.run(debug=True)
