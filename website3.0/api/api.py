import load_dotenv
import os

# Explicitly specify the .env file path
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

print("FLASK_APP:", os.getenv("FLASK_APP"))
print("FLASK_ENV:", os.getenv("FLASK_ENV"))

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)