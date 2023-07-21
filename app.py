from flask import Flask, request, jsonify
from datetime import datetime
app = Flask(__name__)

crate = {
    "drinks": [
        {
            "name": "Grape", 
            "description": "Delicious grape fruit drink",
            "date": datetime.now()
            },
            {
            "name": "Lemon", 
            "description": "Undiluted lemon fruit drink",
            "date": datetime.now()
            },
            {
            "name": "Mango", 
            "description": "This is a mango fruit",
            "date": datetime.now()
            }
    ]
} 

@app.route("/", methods=["GET"])
def index():
        return jsonify({"message":"Welcome To My Drinks API"}), 200

@app.route('/drinks', methods=["GET"])
def get_drinks():
    return crate

@app.route("/description", methods=["GET"])
def get_description():
    data = request.get_json()
    requested_drink = data.get("requested_drink")

    if not requested_drink:
        return jsonify({"error": "Provide drink to check description"}), 400
    
    for drink in crate["drinks"]:
        if drink["name"] == requested_drink:
            return jsonify({"description":drink["description"]}), 200
        
        return jsonify({"error": "The drink you've requested is not available at this time."}), 404


if __name__ == "__main__":
    app.debug = True
    app.run()