from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from fetch import get_startup_news
from analyse import analyse_startups


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    industry = request.args.get("industry", "")
    location = request.args.get("location", "")
    role_type = request.args.get("role_type", "")
    interests = request.args.get("interests", "")

    if not industry or not location:
        return jsonify({"error": "Industry and location are required"}), 400

    articles = get_startup_news(industry, location)
    results = analyse_startups(articles, industry, location, role_type, interests)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)