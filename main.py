from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Madras Programmer Youtube Channel"

@app.route("/get_user_detail/<user_id>")
def get_user_details(user_id):
    if user_id == "1":
        return {
            "name": "Ranjith",
            "age": 26
        },200
    else:
        return {
            "data": "user data not found"
        },200

@app.route("/authenticate-user",methods=["POST"])
def authenticate_user():
    print(request.method)
    data = request.get_json()
    if "user_name" in data and data["user_name"] == "ranjith" and "password" in data and data["password"] == "madrasprogrammer":
        return {
            "status": "SUCCESS"
        }, 200
    else:
        return {
            "status": "FAILED"
        }, 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)