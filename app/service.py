import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

def classify_and_sort_reviews(reviews):
    classified_reviews = []
    for review in reviews:
        ai_sentiment = call_openai_api(review)
        classified_reviews.append((review, ai_sentiment))
    sentiment_order = {"positive": 1, "negative": 2, "neutral": 3}
    classified_reviews.sort(key=lambda r: sentiment_order[r[1]])
    return [review for review, sentiment in classified_reviews]


def call_openai_api(review_text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a text reviews, and your task is to classify its sentiment as positive, neutral, or negative."
            },
            {
                "role": "user",
                "content": f"'{review_text}'"
            }
        ],
        temperature=1,
        max_tokens=20,
        top_p=1
    )
    sentiment = response.choices[0].text.strip()
    return sentiment