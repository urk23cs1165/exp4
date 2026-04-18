from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Docker CI/CD is working 🚀"

@app.route('/health')
def health():
    return "OK - Service is running ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)