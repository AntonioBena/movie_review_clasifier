from flask import Flask
from flask import Blueprint, request, jsonify

from app.service import classify_and_sort_reviews

review_blueprint = Blueprint('review', __name__)

@review_blueprint.route('/classify', methods=['POST'])
def classify_reviews():
    request_data = request.json
    reviews = request_data.get('reviews', [])

    if not reviews or not isinstance(reviews, list):
        return jsonify({"error": "Invalid input, no reviews provided"}), 400
    try:
        sorted_reviews = classify_and_sort_reviews(reviews)
        return jsonify({"sorted_reviews": sorted_reviews}), 200
    except Exception as exception:
        return jsonify({"error": str(exception)}), 500