from flask import Flask, jsonify, request
from flask_cors import CORS

from fetch import get_startup_news
from analyse import analyse_articles


app = Flask(__name__)


@app.route("/")
def home():
    return "Startup Scanner is running"

@app.route("/search")
def search():
    query = request.args.get("query","London startup funding")
    results = get_startup_news(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)