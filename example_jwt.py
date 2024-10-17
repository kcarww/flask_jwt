from flask import Flask, jsonify, request
import jwt
from datetime import datetime, timedelta, timezone

app = Flask(__name__)


@app.route("/", methods=["POST"])
def login():
    token = jwt.encode(
        payload={
            "exp": datetime.now(timezone.utc) + timedelta(seconds=60),
        },
        key="minhaChve",
        algorithm="HS256"
    )
    return jsonify({"token": token}), 200


@app.route("/validate", methods=["POST"])
def validate():
    raw_token = request.headers.get("Authorization").split(" ")[1]
    print(raw_token)
    try:
        token_information = jwt.decode(
            jwt=raw_token,
            key="minhaChve",
            algorithms="HS256"
        )
    except Exception as error:
        return jsonify({"error": str(error)}), 400
    
    
    return jsonify({"meu": "segredo"}), 200


if __name__ == "__main__":
    app.run(debug=True)