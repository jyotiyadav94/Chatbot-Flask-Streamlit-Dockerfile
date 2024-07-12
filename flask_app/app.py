# app.py
import sys
import warnings
from pathlib import Path
from flask import Flask, request, jsonify
# Add src directory to Python path
sys.path.append(str(Path(__file__).parent / "RAG"))
from chat import query_model
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("<h1>Hello, Don't forget to check out my vlog channel<h1> <br>")

@app.route('/query', methods=['POST'])
def query_endpoint():
    data = request.json
    query_str = data.get('query')
    if query_str:
        response = query_model(query_str)
        return jsonify({'response': response})
    return jsonify({'response': 'No query provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
