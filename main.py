from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "home2"

# @app.route("/get_user_detail/<user_id>")
# def get_user_details(user_id):
#     result = {
#         "name": user_id
#     }
#     return jsonify(result), 200

@app.route("/get-user-details",methods=["POST"])
def get_user_details():
    print(request.method)
    data = request.get_json()
    return jsonify(data),200 

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)