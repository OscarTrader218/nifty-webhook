from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/livefeed', methods=['POST'])
def live_feed():
    data = request.json
    print("🔔 Received from TradingView:", data)

    rsi = float(data.get("rsi", 50))
    macd = float(data.get("macd", 0))
    trend = data.get("supertrend", "")

    decision = "WAIT"
    if rsi < 30 and macd < 0 and trend == "-1":
        decision = "📉 Buy PUT Option"
    elif rsi > 70 and macd > 0 and trend == "1":
        decision = "📈 Buy CALL Option"

    print("📊 Trade Suggestion:", decision)
    return jsonify({"decision": decision})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

