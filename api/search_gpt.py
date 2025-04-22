from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/search_gpt")
def search_gpt():
    query = request.args.get("query", "")
    mode = request.args.get("mode", "Residential")
    if "speaker" in query.lower() or "sound" in query.lower():
        return jsonify({
            "quote": [
                {"name": "Yamaha Ceiling Speaker", "price": 1799, "qty": 2},
                {"name": "WXA-50 Streaming Amplifier", "price": 6999, "qty": 1}
            ]
        })
    return jsonify({"quote": []})