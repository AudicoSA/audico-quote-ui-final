
from flask import Flask, request, jsonify
import openai
import requests
import os
import json

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/search_gpt")
def search_gpt():
    query = request.args.get("query", "")
    mode = request.args.get("mode", "Residential")

    prompt = f"""
You are an AV assistant. The customer request is: "{query}".
Identify the type of products they need (e.g. ceiling speakers, amplifier), the number of zones/rooms, and any key features (e.g. Bluetooth, outdoor).
Return your response as JSON like this:
{{
  "products": ["ceiling speakers", "amplifier"],
  "zones": 3,
  "features": ["Bluetooth"]
}}
"""

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AV assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        gpt_response = completion.choices[0].message.content
        parsed = json.loads(gpt_response)

        search_term = parsed['products'][0]
        zones = parsed.get('zones', 1)

        product_api = f"https://audico-quotes-api.onrender.com/products?search={search_term}"
        product_data = requests.get(product_api).json()

        results = []
        for item in product_data[:3]:
            results.append({
                "name": item.get("name"),
                "sku": item.get("sku"),
                "price": float(item.get("price", 0)),
                "qty": zones
            })

        return jsonify({ "quote": results })

    except Exception as e:
        print("Error:", e)
        return jsonify({ "quote": [], "error": str(e) })
