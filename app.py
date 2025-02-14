from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from scraper import scrape_articles
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['news_db']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/articles/<channel>', methods=['GET'])
def get_articles(channel):
    page = int(request.args.get('page', 1))
    per_page = 10
    collection = db[channel]
    total_articles = collection.count_documents({})
    articles = list(collection.find().skip((page - 1) * per_page).limit(per_page))
    for article in articles:
        article['_id'] = str(article['_id'])  # Convert ObjectId to string
    return jsonify({
        'articles': articles,
        'total_articles': total_articles,
        'page': page,
        'per_page': per_page
    })

if __name__ == '__main__':
    scrape_articles()  # Run the scraper to fetch new articles
    app.run(debug=True)