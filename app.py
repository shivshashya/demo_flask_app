from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    name = os.getenv("APP_NAME", "Azure App Service")
    return f"Hello from {name}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
